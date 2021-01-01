# -*- coding: utf-8 -*-
from django.forms.fields import Field, CharField
from django.core import validators
from languageTests.widgets import DragnDropWidget
from django.core.exceptions import ValidationError

import re

class DragNDropField(Field):
    widget = DragnDropWidget
    default_error_messages = {
         'empty': "Please try :).",            
    }
    def __init__(self, *args, max_length=None, min_length=None, strip=True, empty_value='', **kwargs):
        self.max_length = max_length
        self.min_length = min_length
        self.strip = strip
        self.empty_value = empty_value
        super().__init__(*args,**kwargs)
        if min_length is not None:
            self.validators.append(validators.MinLengthValidator(int(min_length)))
        if max_length is not None:
            self.validators.append(validators.MaxLengthValidator(int(max_length)))
        self.validators.append(validators.ProhibitNullCharactersValidator())
    
    def validate(self, value):
        super().validate(value)
        if re.match(r"^\s*$",value):
            #print("Value is empty:validator")
            raise ValidationError(self.error_messages['empty'], code='empty')
    
    def clean(self,value):    
        value = super().clean(value)    
        #print("Cleaned value={}".format(value))
        #if re.match(r"^\s*$",value):
        #    print("Value is empty")

    def to_python(self, value):
        """Return a string."""
        #value = super().to_python(value)
        #print("to_python empty values=%s" % self.empty_values)
        #print("to_python value=%s" % value)
        
        if value not in self.empty_values:
            value = str(value)
            if self.strip:
                value = value.strip()
        if value in self.empty_values:
            return self.empty_value
        return value

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        if self.max_length is not None and not widget.is_hidden:
            # The HTML attribute is maxlength, not max_length.
            attrs['maxlength'] = str(self.max_length)
        if self.min_length is not None and not widget.is_hidden:
            # The HTML attribute is minlength, not min_length.
            attrs['minlength'] = str(self.min_length)
        return attrs
    
    
class CharFieldEmpty(CharField): 
    default_error_messages = {
         'empty': "Please try :).",            
    }
    def validate(self, value):
        super().validate(value)
        if re.match(r"^\s*$",value):
            #print("Value is empty:validator")
            raise ValidationError(self.error_messages['empty'], code='empty') 
            #raise ValidationError("", code='empty') 