from django.test import TestCase

from languageTests.models import LanguageTest, Topic, Language



class LanguageTestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Topic.objects.create(title='New Topic',level='b')
        Language.objects.create(name='English')
        topic    = Topic.objects.get(id=1)
        language = Language.objects.get(id=1)
        LanguageTest.objects.create(task='Choose the right words', number=1, topic=topic, language=language)

    def setUp(self):
        #print("setUp: Run once for every test method to setup clean data.")
        pass
    
    def test_task_label(self):
        language_test = LanguageTest.objects.get(id=1)
        field_label = language_test._meta.get_field('task').verbose_name
        self.assertEquals(field_label, 'task')

    def test_number_label(self):
        language_test = LanguageTest.objects.get(id=1)
        field_label = language_test._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'number')
        
    def test_topic_label(self):
        language_test = LanguageTest.objects.get(id=1)
        field_label = language_test._meta.get_field('topic').verbose_name
        self.assertEquals(field_label, 'topic')     
        
    def test_language_label(self):
        language_test = LanguageTest.objects.get(id=1)
        field_label = language_test._meta.get_field('language').verbose_name
        self.assertEquals(field_label, 'language')   
        
        
    def test_get_absolute_url(self):
        language_test = LanguageTest.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(language_test.get_absolute_url(), '/languageTests/languagetest/1')     

        
        
class TopicTestModelTest(TestCase):
    pass