import datetime 

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class TakeATestDummy(forms.Form):
        
    testDict={}
    def set_tests_dict(self,dict_to_set):
        self.testDict=dict_to_set
    
    def append_new_test(self,name,count):
        self.testDict[name]=count
        pass
    def get_tests_dict(self):
        return self.testDict
 
class TakeATestFormer(forms.Form):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
    def get_language_tests(self):
        pass

    
    
    #renewal_date = forms.DateField(help_text=language_test)
    #for excersice in language_test.excersise_set:
    #       pass      
    
    #def clean_renewal_date(self):
    #    data = self.cleaned_data['renewal_date']
        
        # Check if a date is not  in the past. 
        #if data < datetime.date.today():
        #    raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        #if data > datetime.date.today() + datetime.timedelta(weeks=4):
        #    raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
    #    return data  