# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from languageTests.models import Topic, LanguageTest, Excersise, Answer


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'


    def get_text(self,filename):
        doc = docx.Document(filename)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)

    #def add_arguments(self, parser):
    #    parser.add_argument('file_path',metavar='file_path', help='file path to parse from')
    #    parser.add_argument('topic',metavar='topic', help='name of the topic')
        
    def handle(self, *args, **options):
        
        all_topics=Topic.objects.all()
        for topic in all_topics:
            print("deleted topic:{}".format(topic.title))       
            topic.delete()

            
        all_language_tests=LanguageTest.objects.all()
        for language_test in all_language_tests:
            pass
            print("deleted labguage_test:{}".format(language_test.number))
            language_test.delete()
            
            
        all_excersises= Excersise.objects.all()
        for excersise in all_excersises:
            pass
            print("deleted excersise:{}".format(excersise.text))
            excersise.delete()
            
        all_answers=Answer.objects.all()
        for answer in all_answers:
            pass
            print("deleted answer:{}".format(answer.answer_string))
            answer.delete()
        
        