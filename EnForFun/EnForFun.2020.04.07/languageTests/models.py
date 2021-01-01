from django.db import models
import uuid # Required for unique excersises 
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.
from accounts.models import User

class Explanation(models.Model):
    """Model representing explanation for wrong answers"""
    answer       = models.ForeignKey('Answer',on_delete=models.CASCADE, null=True, help_text='Explanation of the answer')
    language     = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    explain_text = models.TextField(max_length=1000, default="", help_text='Explanation text for the answer')
    wrong_answer = models.CharField(max_length=200, null=True, help_text='Expected wrong answer')

class Answer(models.Model):
    """Model representing answer for excersise"""
    excersise = models.ForeignKey('Excersise',on_delete=models.CASCADE, null=True, help_text='Answer of excersise')
    explanation_string = models.TextField(max_length=1000, null=True,help_text="Enter the explanation")
    answer_string = models.CharField(max_length=100,help_text="Enter the answer")
    possible_answers = models.CharField(max_length=100, null=True, help_text="Enter the possible answers")

class Language(models.Model):
    """Model respresenting language""" 
    name = models.CharField(max_length=100,help_text="Enter the language (e.g. English, French, Japanese etc.)")
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class TutorialComponent(models.Model):
    TYPES = (
        ('e','Explanation'),
        ('p','Picture'),
        ('c','Chart'),
        ('x','Example')
    ) 
    
    component_type = models.CharField(
        max_length=1,
        choices=TYPES,
        blank=True,
        default='e',
        help_text='Component type',
    )
    
    component_text = models.TextField(max_length=10000, default="", blank=True, help_text='Explanation text')
    
    tutorial = models.ForeignKey('Tutorial',on_delete=models.CASCADE, null=True, blank=True, help_text='Tutorial')
    

    
class Tutorial(models.Model):
    LEVELS = (
        ('b', 'Beginner'),
        ('i', 'Intermediate'),
        ('e', 'Expert'),
    )
    tutorial_title = models.CharField(max_length=200, help_text='Enter a Tutorial Name (e.g. Present simple #1)')
    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        blank=True,
        default='b',
        help_text='Tutorial level',
    )
                                                                                        
    def __str__(self):
        """String for representing the Model object."""
        return f'' + self.tutorial_title
    
    def return_level_str(self):
        dict_levels=dict(self.LEVELS)
        return dict_levels[self.level]
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        #return reverse('languagetest_detail', args=[str(self.id)]) 
        return reverse('tutorial', args=[str(self.id)]) 
    
    
class Excersise(models.Model):
    LEVELS = (
        ('b', 'Beginner'),
        ('i', 'Intermediate'),
        ('e', 'Expert'),
    )

    TYPES = (
        ('w'  ,'Choose the word'),
        ('s'  ,'Construct a sentance'),
        ('t'  ,'Type the word'),
        ('tf' ,'Type the word faded'),
        ('ts' ,'Type the sentence'),
        ('tsi','Type the sentence inline'),
        ('cco','Click the correct option')
    )  
    
    #level = models.CharField(
    #    max_length=1,
    #    choices=LEVELS,
    #    blank=True,
    #    default='b',
    #    help_text='Excersise level',
    #)

    exercise_type = models.CharField(
        max_length=3,
        choices=TYPES,
        blank=True,
        default='w',
        help_text='Tests type',
    )
    
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular excersise')
    text = models.TextField(max_length=1000, default="", null=True, help_text='Text of the excersise')
    
    
    language_test = models.ForeignKey('LanguageTest',on_delete=models.CASCADE, null=True, help_text='Unique test')
    #language_test_group = models.ForeignKey('LanguageTestGroup',on_delete=models.SET_NULL, null=True, help_text='Unique test')
    chars_to_display = 80
    
    def __str__(self):
        """String for representing the Model object."""
        #return f'Ex#:{self.id}' + self.display_text()
        return f'Ex:' + self.display_text()
    
    def display_text(self):
        output_text=self.text
        if len(self.text) > self.chars_to_display:
            output_text=output_text[:self.chars_to_display] + "..."
        return output_text
    
    def display_language_test(self):
        return self.language_test.title
    
class Topic(models.Model):
    LEVELS = (
        ('b', 'Beginner'),
        ('i', 'Intermediate'),
        ('e', 'Expert'),
    )

    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        blank=True,
        default='b',
        help_text='Tests level',
    )   
    
    #language_test = models.ForeignKey('LanguageTest',on_delete=models.SET_NULL, null=True, blank=True, help_text='Unique test')
    title = models.CharField(max_length=200, help_text='Enter a Test Name (e.g. Test #1)')
    
    def return_level_str(self):
        dict_levels=dict(self.LEVELS)
        return dict_levels[self.level]    
    
    def __str__(self):
        """String for representing the Model object."""
        return str(self.title)
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        #return reverse('languagetest_detail', args=[str(self.id)]) 
        return reverse('topic', args=[str(self.id)]) 
    
class LanguageTest(models.Model):
    """Model representing a Language Test."""
    
    #answers = models.CharField(default="", max_length=1024)
    task   = models.CharField(default="", null=True, max_length=1024)
    number = models.IntegerField(null=True)
    #user   = models.OneToOneField(User, blank=True, null=True,on_delete=models.CASCADE)
    #LEVELS = (
    #    ('b', 'Beginner'),
    #    ('i', 'Intermediate'),
    #    ('e', 'Expert'),
    #)

    #level = models.CharField(
    #    max_length=1,
    #    choices=LEVELS,
    #    blank=True,
    #    default='b',
    #    help_text='Tests level',
    #)                                                           
                                                                           
    def __str__(self):
        """String for representing the Model object."""
        return str(self.number)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        #return reverse('languagetest_detail', args=[str(self.id)]) 
        return reverse('take_a_test', args=[str(self.id)]) 
       
    
    #def return_level_str(self):
    #    dict_levels=dict(self.LEVELS)
    #    return dict_levels[self.level]
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE, null=True, help_text='Unique test')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    #native_language = models.ForeignKey('Language', on_delete=models.SET_NULL)
    #excersise       = models.ManyToManyField(Excersise, help_text='Select excersises for current Test')  