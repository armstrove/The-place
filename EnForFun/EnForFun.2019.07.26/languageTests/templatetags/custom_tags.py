from django import template
from django import forms
from django.utils.safestring import mark_safe
register = template.Library()
import re


#from ..models import Answer

@register.simple_tag
def add_choices_to_excersise(excersise_text,form,answers):
    #print("range=<{}>",format(len(answers)))
    it=iter(answers)
    output_string=excersise_text
    for ans in it:
        ans=next(it)
        #print(ans)
        #print("<?{}?> ({})".format(answer,form_answer))
        #print("<?{}?> ()".format(ans))
        #print("aa{}aa".format(dir(form.fields[ans])))
        #print("aa{}aa".format(dir(form)))
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field))
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field.__str__))
        print("aaa{}aaa".format(form.fields[ans].get_bound_field(form,ans).errors))
        html_field=form.fields[ans].get_bound_field(form,ans).__str__()
        output_string=re.sub(r'\$\$\$',html_field,output_string,count=1)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
    return mark_safe(output_string)    
        
        


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)