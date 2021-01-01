from django.db import models
import uuid # Required for unique excersises 
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.


class Explanation(models.Model):
    """Model representing explanation for wrong answers"""
    answer       = models.ForeignKey('Answer',on_delete=models.SET_NULL, null=True, help_text='Explanation of the answer')
    language     = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    explain_text = models.TextField(max_length=1000, default="", help_text='Explanation text for the answer')
    wrong_answer = models.CharField(max_length=200, null=True, help_text='Expected wrong answer')

class Answer(models.Model):
    """Model representing answer for excersise"""
    excersise = models.ForeignKey('Excersise',on_delete=models.SET_NULL, null=True, help_text='Answer of excersise')
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
 

class Excersise(models.Model):
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
        help_text='Excersise level',
    )
    
    id   = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular excersise')
    text = models.TextField(max_length=1000, default="", help_text='Text of the excersise')
    language_test = models.ForeignKey('LanguageTest',on_delete=models.SET_NULL, null=True, help_text='Unique test')
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
    
        
class LanguageTest(models.Model):
    """Model representing a Language Test."""
    title = models.CharField(max_length=200, help_text='Enter a Test Name (e.g. Test #1)')
    answers = models.CharField(default="", max_length=1024)
                                                                       
    
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
                                                                       
                                                                           
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        #return reverse('languagetest_detail', args=[str(self.id)]) 
        return reverse('take_a_test', args=[str(self.id)]) 
       
    
    def return_level_str(self):
        dict_levels=dict(self.LEVELS)
        return dict_levels[self.level]
    
    language        = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    #native_language = models.ForeignKey('Language', on_delete=models.SET_NULL)
    #excersise       = models.ManyToManyField(Excersise, help_text='Select excersises for current Test')  