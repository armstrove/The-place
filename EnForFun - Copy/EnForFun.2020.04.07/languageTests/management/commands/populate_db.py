# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from languageTests.models import Topic, LanguageTest, Excersise, Answer
import docx 
import re

class Parser():
    excersise_type=""
    
    def __init__(self,sentences,language_test,debug=False):
        self.sentences=sentences        
        self.language_test=language_test
        self.sentences_list=[]
        self.answers_list=[]
        self.excersises_list=[]
        self.keywords=["\$inter","\$neg","\$expl","\$end","$"]
        #self.keywords=["\$expl","\$end"]
        self.keyword_regexp="(" + "|".join(self.keywords) + ")" 
        self.split_sentences()
        self.parse()
        
    def create_excersise(self, exercise_type, text):
        excersise=Excersise(exercise_type=exercise_type,
                            text=text,
                            language_test=self.language_test)
        return excersise
    
    
    def create_answer(self, answer_string, possible_answers, explanation_string, excersise):
        answer=Answer(answer_string=answer_string,
                      possible_answers=possible_answers,
                      explanation_string=explanation_string,
                      excersise=excersise
                      )
        self.answers_list.append(answer)
        return answer
    
    def save(self):
        for excersise in self.excersises_list:
            #print("text='{}'".format(excersise.text))
            excersise.save()
        for answer in self.answers_list:
            #print(answer.answer_string)
            answer.save()
    def format_text_from_sentence(self,sentence):        
        return re.sub(r"\$\$\$\s*\(.*?\)","$$$",sentence)
    
    def extract_text_from_sentence(self,sentence):
        print(r"(.*?){}.*".format(self.keyword_regexp))
        print("text=<%s>" % sentence)
        text = re.search(r"(.*?){}".format(self.keyword_regexp),sentence,re.DOTALL)
        if text:
            #return re.sub(r"\$\$\$\s*\(.*?\)","$$$",text.group(1))
            return self.format_text_from_sentence(text.group(1))
        else:
            print("Error: was not able to parse %s" % sentence)
    
    def extract_explanation_from_sentence(self,sentence):
        explanations = []
        explanation = re.search(r"\$expl(.*)".format(self.keyword_regexp),sentence,re.DOTALL)
        if explanation:
            explanations=explanation.group(1).split("$|")
            return explanations
        else:
            return [""]    
    
    def extract_answers_from_sentence(self,sentence):
        # requires string as an input  
        # provides dict of an answer and possible answer
        return [self.return_answer_dict(answer="",possible_answer="possible_answer")]
    
    def clean_sentence(self,sentence):
        # requires string
        # provides clean(withou whitespaces at the ends) string
        #sentence=sentence.rstrip("\n")
        
        sentence=re.sub(r"\s+",r" ",sentence)
        sentence=sentence.strip()
        return sentence
    
    def return_answer_dict(self,answer,possible_answer):
        return {"answer":answer,"possible_answer":possible_answer}
    
    def parse(self):
        for sentence in  self.sentences_list:
            text         =self.extract_text_from_sentence(sentence)
            text         =self.clean_sentence(text)
            explanations =self.extract_explanation_from_sentence(sentence)
            print("extrated_sent=<{}>".format(sentence.strip()))
            print("extrated_text=<{}>".format(text))
            print("extrated_expl=<{}>".format(explanations))
            print("-"*99)
            excersise=self.create_excersise(
                    exercise_type=self.excersise_type,
                    text=text
            )

            self.excersises_list.append(excersise)
            sentence=self.clean_sentence(sentence)
            answers=self.extract_answers_from_sentence(sentence)
            print("answers=%s" % answers)
            if len(answers) != len(explanations):
                print("ERROR: there are {} answers but {} explanations".format(len(answers),len(explanations)))
                return 0
            for index,answer in enumerate(answers):
                self.create_answer(answer_string=answer["answer"],
                                   possible_answers=answer["possible_answer"],
                                   explanation_string=explanations[index],
                                   excersise=excersise)

    
    def split_sentences(self):
        self.sentences_list=self.sentences.split("$end")[:-1]




class Parse_type_the_word(Parser):    
    excersise_type="t"
    
    def extract_answers_from_sentence(self,sentence):
        answer_regexp     = re.compile(r"\$\$\$\s*\((.*?)\)")
        extracted_answers = answer_regexp.finditer(sentence)
        output_answers=[]
        for answer in extracted_answers:
                asnwer_str=answer.group(1)
                #print("     '{}'".format(asnwer_str))
                output_answers.append(self.return_answer_dict(answer=asnwer_str,possible_answer="*"))

        return output_answers      

class Parse_type_the_word_faded(Parser):
    excersise_type="tf"
    
    def format_text_from_sentence(self,sentence):
        return re.sub(r"\(.*?\)\s*\$\$\$\s*\(.*?\)","$$$",sentence)
    
    
    def extract_answers_from_sentence(self,sentence):
        answer_regexp     = re.compile(r"\((.*?)\)\$\$\$\s*\((.*?)\)")
        extracted_answers = answer_regexp.finditer(sentence)
        output_answers=[]
        for answer in extracted_answers:
                possible_answer=answer.group(1)
                asnwer_str=answer.group(2)
                #print("     '{}'".format(asnwer_str))
                output_answers.append(self.return_answer_dict(answer=asnwer_str,possible_answer=possible_answer))

        return output_answers 
    
class Parse_choose_the_word(Parser):  
    excersise_type="w"

    def extract_answers_from_sentence(self,sentence):
        answer_regexp     = re.compile(r"\$\$\$\s*\((.*?)\)")
        extracted_answers = answer_regexp.finditer(sentence)
        output_answers=[]
        for answer in extracted_answers:
                asnwer_str=answer.group(1)
                possible_answers=re.sub(r"\$",r"",asnwer_str)
                asnwer_str="/".join([re.sub(r"\$",r"",ans) for ans in asnwer_str.split("/") if re.search(r"\$",ans)])
                #print("     '{}'  possible '{}'".format(asnwer_str,possible_answers))
                output_answers.append(self.return_answer_dict(asnwer_str,possible_answers))
                #answer=self.create_answer(answer_string=asnwer_str,possible_answers="None",excersise=excersise)
        return output_answers 
     
        asnwer_str=answer.group(1)


class Parse_click_the_correct_option(Parse_choose_the_word):
    excersise_type="cco"


class Parse_construct_the_sentence(Parser):
    excersise_type="s"
    
    
class Parse_type_sentences(Parser):
    excersise_type="ts"
    
    def extract_answers_from_sentence(self,sentence):
        answer_regexp     = re.compile(r"\$\$\$\s*\((.*?)\)")
        extracted_answers = answer_regexp.finditer(sentence)
        output_answers=[]
        for answer in extracted_answers:
                asnwer_str=answer.group(1)
                #print("     '{}'".format(asnwer_str))
                output_answers.append(self.return_answer_dict(answer=asnwer_str,possible_answer="*"))
    
        return output_answers 
    
class Parse_type_sentences_inline(Parse_type_sentences):  
    excersise_type="tsi"
    
    def format_text_from_sentence(self,sentence):        
        return re.sub(r"\$\$\$\s*\(.*?\)","",sentence)
        
    
    
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
    
    def parse(self,type,sentences,language_test):
        parser=self.Parsers[type](sentences,language_test)
        parser.save()
    
    def parse_tests_from_docx(self,filepath,topicName):
        topic         = self.create_topic(topicName)
        full_text     = self.get_text(filepath)
        parse_regexp  = re.compile(r"\$task:\s*(.*?)\$type:\s*(\w+)\s*(.*?)(?=\$task|$)", re.DOTALL|re.IGNORECASE)
        exercise_objs = parse_regexp.finditer(full_text)
        num=1
        for ex_obj in exercise_objs:            
            task=ex_obj.group(1)
            print(task)
            type=ex_obj.group(2)
            sentences=ex_obj.group(3)
            language_test = self.create_language_test(task,num,topic) 
            self.parse(type,sentences,language_test)
            print("-"*100)
            self.stdout.write("task=<{}>".format(task.strip()))
            self.stdout.write("type=<{}>".format(type.strip()))
            self.stdout.write("sentences={}".format(sentences))
            num+=1
            
        
    def handle(self, *args, **options):

        self.parse_tests_from_docx(options['file_path'],options['topic'])
        

    
    Parsers = {
            "type_the_word":Parse_type_the_word,
            "type_the_word_faded":Parse_type_the_word_faded,
            "type_sentences":Parse_type_sentences,
            "type_sentences_inline":Parse_type_sentences_inline,
            "choose_the_word":Parse_choose_the_word,
            "construct_the_sentence":Parse_construct_the_sentence,
            "click_the_correct_option":Parse_click_the_correct_option
             } 
        