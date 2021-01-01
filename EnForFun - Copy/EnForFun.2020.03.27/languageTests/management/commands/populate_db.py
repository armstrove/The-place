# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from languageTests.models import Topic, LanguageTest, Excersise, Answer
import docx 
import re

class Parser():
    def __init__(self,sentences,language_test,debug=False):
        self.sentences=sentences        
        self.language_test=language_test
        self.sentences_list=[]
        self.answers_list=[]
        self.excersises_list=[]

        
        self.split_sentences()
        self.parse()
        

        
        
    def create_excersise(self, exercise_type, text):
        excersise=Excersise(exercise_type=exercise_type,
                            text=text,
                            language_test=self.language_test)
        
        #excersise.save()
        return excersise
    
    
    def create_answer(self, answer_string, possible_answers, excersise):
        answer=Answer(answer_string=answer_string,
                      possible_answers=possible_answers,
                      excersise=excersise
                      )
        self.answers_list.append(answer)
        #answer.save()
        return answer
    
    def save(self):
        for excersise in self.excersises_list:
            print(excersise.text)
            excersise.save()
        for answer in self.answers_list:
            print(answer.answer_string)
            answer.save()
    
    def extract_text_from_sentence(self,sentence):
        return sentence
    
    def extract_explanation_from_sentence(self,sentence):
        return sentence
    
    def extract_answers_from_sentence(self,sentence):
        return [self.return_answer_dict("","possible_answer")]
    
    def clean_sentence(self,sentence):
        return sentence.strip()
    
    def return_answer_dict(self,asnwer,possible_answer):
        return {"answer":asnwer,"possible_answer":possible_answer}
    
    def parse(self):
        for sentence in self.sentences_list:
            print("_"*100 + "\n<{}>".format(sentence.strip()))

            text       =self.extract_text_from_sentence(sentence)
            #explanation=self.extract_explanation_from_sentence(sentence)
            excersise=self.create_excersise(
                    exercise_type="t",
                    text=text
            )

            self.excersises_list.append(excersise)
            sentence=self.clean_sentence(sentence)
            answers=self.extract_answers_from_sentence(sentence)
            for answer in answers:
                self.create_answer(answer_string=answer["answer"],
                                   possible_answers=answer["possible_answer"],
                                   excersise=excersise)
            #self.save()    
        
    
    def split_sentences(self):
        self.sentences_list=self.sentences.split("$end")[:-1]

class Parse_type_the_word(Parser):
    pass    
    
    def extract_text_from_sentence(self,sentence):
        return re.sub(r"\$\$\$\(.*?\)","$$$",sentence)
    
    def extract_answers_from_sentence(self,sentence):
        answer_regexp     = re.compile(r"\$\$\$\((.*?)\)")
        extracted_answers = answer_regexp.finditer(sentence)
        output_answers=[]
        for answer in extracted_answers:
                asnwer_str=answer.group(1)
                print("     '{}'".format(asnwer_str))
                output_answers.append(self.return_answer_dict(asnwer_str,"*"))
                #answer=self.create_answer(answer_string=asnwer_str,possible_answers="None",excersise=excersise)
        return output_answers      
    
class Parse_choose_the_word(Parser):  
    
    def extract_text_from_sentence(self,sentence):
        return re.sub(r"\$\$\$\(.*?\)","$$$",sentence)
    
    def extract_answers_from_sentence(self,sentence):
        answer_regexp     = re.compile(r"\$\$\$\((.*?)\)")
        extracted_answers = answer_regexp.finditer(sentence)
        output_answers=[]
        for answer in extracted_answers:
                asnwer_str=answer.group(1)
                possible_answers=re.sub(r"\$",r"",asnwer_str)
                asnwer_str="/".join([ans[1:] for ans in asnwer_str.split("/") if ans[0] == "$"])
                print("     '{}'  possible '{}'".format(asnwer_str,possible_answers))
                output_answers.append(self.return_answer_dict(asnwer_str,possible_answers))
                #answer=self.create_answer(answer_string=asnwer_str,possible_answers="None",excersise=excersise)
        return output_answers 
     
        
        asnwer_str=answer.group(1)
                
                
                
    
    
class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def get_text(self,filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)

    def add_arguments(self, parser):
        parser.add_argument('file_path',metavar='file_path', help='file path to parse from')
        parser.add_argument('topic',metavar='topic', help='name of the topic')
    
    def create_topic(self, topicName):
        topic = Topic(title=topicName,level="b")
        topic.save()
        return topic
    
    def create_language_test(self, task, number, topic):
        language_test=LanguageTest(task=task,number=number,topic=topic)
        language_test.save()
        return language_test
    
    def create_excersise(self, exercise_type, text, language_test):
        excersise=Excersise(exercise_type=exercise_type,
                            text=text,
                            language_test=language_test)
        excersise.save()
        return excersise
    
    def create_answer(self, answer_string, possible_answers, excersise):
        answer=Answer(answer_string=answer_string,
                      possible_answers=possible_answers,
                      excersise=excersise
                      )
        answer.save()
        return answer
    
    def parse_type_the_word(self,sentences,language_test):
        sentenc_list=sentences.split("$end")
        for sentence in sentenc_list[:-1]:
            print("_"*100 + "\n<{}>".format(sentence.strip()))
            text=re.sub(r"\$\$\$\(.*?\)","$$$",sentence)
            excersise=self.create_excersise(exercise_type="t",text=text,language_test=language_test)
            sentence=sentence.strip()
            answer_regexp=re.compile(r"\$\$\$\((.*?)\)")
            answers_list=answer_regexp.finditer(sentence)
            for answer in answers_list:
                asnwer_str=answer.group(1)
                print("     '{}'".format(asnwer_str))
                answer=self.create_answer(answer_string=asnwer_str,possible_answers="None",excersise=excersise)

    def parse_choose_the_word(self,sentences,language_test):
        sentenc_list=sentences.split("$end")
        for sentence in sentenc_list[:-1]:
            print("_"*100 + "\n<{}>".format(sentence.strip()))
            text=re.sub(r"\$\$\$\(.*?\)","$$$",sentence)
            excersise=self.create_excersise(exercise_type="w",text=text,language_test=language_test)
            sentence=sentence.strip()
            answer_regexp=re.compile(r"\$\$\$\((.*?)\)")
            answers_list=answer_regexp.finditer(sentence)
            for answer in answers_list:
                asnwer_str=answer.group(1)
                possible_answers=re.sub(r"\$",r"",asnwer_str)
                asnwer_str="/".join([ans[1:] for ans in asnwer_str.split("/") if ans[0] == "$"])
                print("     '{}'  possible '{}'".format(asnwer_str,possible_answers))
                answer=self.create_answer(answer_string=asnwer_str,possible_answers=possible_answers,excersise=excersise)
                
    
    def parse(self,type,sentences,language_test):
        #self.parsers[type](self,sentences,language_test)
        parser=self.Parsers[type](sentences,language_test)
        parser.save()
    
    def parse_tests_from_docx(self,filepath,topicName):
        topic         = self.create_topic(topicName)
        full_text     = self.get_text(filepath)
        parse_regexp  = re.compile(r"\$task:(.*?)\$type:\s*(\w+)\s*(.*?)(?=\$task|$)", re.DOTALL)
        #parse_regexp  = re.compile(r"\$task:(.*?)\$type:(.*?)(?=\$task|$)", re.DOTALL)
        exercise_objs = parse_regexp.finditer(full_text)
        num=1
        for ex_obj in exercise_objs:
            task=ex_obj.group(1)
            type=ex_obj.group(2)
            sentences=ex_obj.group(3)
            #print(sentences.strip())
            #print(ex_obj.group(3))
            language_test = self.create_language_test(task,num,topic) 
            
        
            self.parse(type,sentences,language_test)
            print("-"*100)
            self.stdout.write("task=<{}>".format(task.strip()))
            self.stdout.write("type=<{}>".format(type.strip()))
            self.stdout.write("sentences={}".format(sentences))
            num+=1
            
        
    def handle(self, *args, **options):
        #for key in options:
        #    self.stdout.write("{} {}".format(key,options[key]))
        self.parse_tests_from_docx(options['file_path'],options['topic'])
        

        
        #self.stdout.write(self.style.SUCCESS('Successfully opened file "%s"' % options['file_path']))
        
    #parsers = {
    #        "type_the_word":parse_type_the_word,
    #        "choose_the_word":parse_choose_the_word
    #         }  
    
    
    Parsers = {
            "type_the_word":Parse_type_the_word,
            "choose_the_word":Parse_choose_the_word
             } 
        