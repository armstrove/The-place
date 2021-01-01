from django import template
from django import forms
from django.utils.safestring import mark_safe
register = template.Library()
import re
import random
import string


def format_error_text(text):
    text=re.sub(r"\$h(.*?)\$h",r'<b>\1</b>',text,re.DOTALL)
    return text

def format_text_for_inline(text):
    return re.sub(r".*?(\$\$\$).*?",r"\1 ",text)
    

def drag_n_drop_html(answer,id_num,rand=False,answered_true=False):
    words_for_drag_n_drop=""
    drop_answer_string=""
    symbols=[',','.',':',"?"]
    
    words_of_answer=answer.split(" ")
    if rand:
        random.shuffle(words_of_answer)
        print("words={}".format(words_of_answer))
    
    if answered_true:  
        print("Don't answered or answered false")
        for index,splited_strings in enumerate(words_of_answer):
            if splited_strings in symbols:
                words_for_drag_n_drop += '<div class="symbol">' + splited_strings + '</div>'
            elif splited_strings:
                words_for_drag_n_drop += '<div class="dragNDropWord" id="" draggable="false" ondragstart="drag(event)" style="display: none;" onclick="add_answer(event)">' + '</div>'
            else:
                print("Error: unknown drapNdrop string" + splited_strings)
            drop_answer_string += '<div class="drag-n-drop-aswer-cell" id="{}{}" draggable="false" ondragstart="drag_answer(event)"  ondrop="drop(event)" ondragover="allowDrop(event)">'.format(id_num,index) + splited_strings + '</div>'
    else:        
        print("Answered true")
        for index,splited_strings in enumerate(words_of_answer):
            if splited_strings in symbols:
                words_for_drag_n_drop += '<div class="symbol">' + splited_strings + '</div>'
            elif splited_strings:
                words_for_drag_n_drop += '<div class="dragNDropWord" id="{}{}" draggable="true" ondragstart="drag(event)" onclick="add_answer(event)">'.format(id_num,index) + splited_strings + '</div>'
            else:
                print("Error: unknown drapNdrop string" + splited_strings)
            drop_answer_string += '<div class="drag-n-drop-aswer-cell" draggable="true" ondragstart="drag_answer(event)"  ondrop="drop(event)" ondragover="allowDrop(event)" onclick="remove_element(event.target)"></div>'


        

    return [words_for_drag_n_drop,drop_answer_string]

def generate_drag_n_drop_answer_choice_html(answer,answered_val,id_num,answered_true=False):
    symbols=[',','.',':',"?"]
    words_for_drag_n_drop = ""
    drop_answer_string    = ""
    #print("value======{}".format(answered_val))
    if re.match(r"^\s*$",str(answered_val)):
        print("None or empty")
        [words_for_drag_n_drop,drop_answer_string]=drag_n_drop_html(answer,id_num,rand=True,answered_true=answered_true)
    else:
        [words_for_drag_n_drop,drop_answer_string]=drag_n_drop_html(answer,id_num,rand=True,answered_true=answered_true)
    
    return [words_for_drag_n_drop,drop_answer_string]

#from ..models import Answer
@register.simple_tag
def excersise_choose_the_word(excersise_text,form,answers):
    #print("range=<{}>",format(len(answers)))
    answers_iterator=iter(answers)
    output_string=excersise_text
    error_html=""
    error_html_text=""
    error_in_answers=False
    counter=1
    for ans in answers_iterator:
        ans=next(answers_iterator)
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field(form,ans).value()))
        value=form.fields[ans].get_bound_field(form,ans).value()
        if form.is_bound:        
            if form.fields[ans].get_bound_field(form,ans).errors:
                text=form.fields[ans].get_bound_field(form,ans).errors.as_text()
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
            if value=="":
                text="This can't be empty"
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
        
        html_field=form.fields[ans].get_bound_field(form,ans).__str__()
        output_string=re.sub(r'\$\$\$',html_field,output_string,count=1)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
        #print("-----{}------".format(output_string))
        #print("{} {}".format(output_string,error_html))
        counter+=1
        
    if form.is_bound:    
        if error_in_answers:
            status_html='<div class="wrapper-status"><div class="status explanation-message">{}</div></div>'.format(error_html_text)   
        else:
            status_html='<div class="wrapper-status"><div class="status success-message">Excelent</div></div>'
    else:
        status_html=""
    output_string=re.sub(r'<select ',r'<select class="selectstrove" ',output_string)    
    return mark_safe("{} {}".format(output_string,status_html))    

@register.simple_tag
def excersise_click_the_correct_option(excersise_text,form,answers):
    answers_iterator=iter(answers)
    output_string=excersise_text
    error_html=""
    error_html_text=""
    error_in_answers=False
    counter=1
    for ans in answers_iterator:
        #ans=next(answers_iterator)
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field(form,ans).value()))
        value=form.fields[ans].get_bound_field(form,ans).value()
        if form.is_bound:        
            if form.fields[ans].get_bound_field(form,ans).errors:
                text=form.fields[ans].get_bound_field(form,ans).errors.as_text()
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
            if value=="":
                text="This can't be empty"
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
        
        html_field=form.fields[ans].get_bound_field(form,ans).__str__()
        output_string=re.sub(r'\$\$\$',html_field,output_string,count=1)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
        #print("-----{}------".format(output_string))
        #print("{} {}".format(output_string,error_html))
        counter+=1    
        
    if form.is_bound:    
        if error_in_answers:
            status_html='<div class="wrapper-status"><div class="status explanation-message">{}</div></div>'.format(error_html_text)   
        else:
            status_html='<div class="wrapper-status"><div class="status success-message">Excelent</div></div>'
    else:
        status_html=""
    output_string=re.sub(r'<select ',r'<select class="selectstrove" ',output_string)    
    return mark_safe("{} {}".format(output_string,status_html))    



#from ..models import Answer
@register.simple_tag
def excersise_type_the_word(excersise_text,form,answers):
    #print("range=<{}>",format(len(answers)))
    answers_iterator=iter(answers)
    output_string=excersise_text
    error_html=""
    error_html_text=""
    error_in_answers=False
    counter=1
    for ans in answers_iterator:
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field(form,ans).value()))
        value=form.fields[ans].get_bound_field(form,ans).value()
        if form.is_bound:        
            if form.fields[ans].get_bound_field(form,ans).errors:
                text=form.fields[ans].get_bound_field(form,ans).errors.as_text()
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
            if value=="":
                error_html_text = error_html_text          
                error_in_answers=True
        
        
        html_field=form.fields[ans].get_bound_field(form,ans).__str__()
        #print("html_field={}".format(html_field))
        output_string=re.sub(r'\$\$\$',html_field,output_string,count=1)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
        #print("-----{}------".format(output_string))
        #print("{} {}".format(output_string,error_html))
        counter+=1
        
    if form.is_bound:    
        if error_in_answers:
            status_html='<div class="wrapper-status"><div class="status explanation-message">{}</div></div>'.format(format_error_text(error_html_text))   
        else:
            status_html='<div class="wrapper-status"><div class="status success-message">Excelent</div></div>'
    else:
        status_html=""
    output_string=re.sub(r'<select ',r'<select class="selectstrove" ',output_string)    
    return mark_safe("{} {}".format(output_string,status_html))    

@register.simple_tag
def excersise_type_the_sentence(excersise_text,form,answers):
    answers_iterator=iter(answers)
    output_string=excersise_text
    error_html=""
    error_html_text=""
    error_in_answers=False
    counter=1
    for ans in answers_iterator:
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field(form,ans).value()))
        value=form.fields[ans].get_bound_field(form,ans).value()
        if form.is_bound:        
            if form.fields[ans].get_bound_field(form,ans).errors:
                text=form.fields[ans].get_bound_field(form,ans).errors.as_text()
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
            if value=="":
                error_html_text = error_html_text          
                error_in_answers=True
        
        
        html_field=form.fields[ans].get_bound_field(form,ans).__str__()
        #print("html_field={}".format(html_field))
        output_string=re.sub(r'\$\$\$',"<br/>{}".format(html_field),output_string,count=1)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
        #print("-----{}------".format(output_string))
        #print("{} {}".format(output_string,error_html))
        #output_string="{}<br/>{}".format(output_string,html_field)
        counter+=1
        
    if form.is_bound:    
        if error_in_answers:
            status_html='<div class="wrapper-status"><div class="status explanation-message">{}</div></div>'.format(format_error_text(error_html_text))   
        else:
            status_html='<div class="wrapper-status"><div class="status success-message">Excelent</div></div>'
    else:
        status_html=""
    output_string=re.sub(r'<select ',r'<select class="selectstrove" ',output_string)    
    return mark_safe("{} {}".format(output_string,status_html))    

@register.simple_tag
def excersise_type_the_sentence_inline(excersise_text,form,answers):
    answers_iterator=iter(answers)
    #output_string=excersise_text
    output_string="<del>" + excersise_text + "</del>"
    ##format_text_for_inline(excersise_text)
    error_html=""
    error_html_text=""
    error_in_answers=False
    counter=1
    for ans in answers_iterator:
        #print("aaa{}aaa".format(form.fields[ans].get_bound_field(form,ans).value()))
        value=form.fields[ans].get_bound_field(form,ans).value()
        if form.is_bound:        
            if form.fields[ans].get_bound_field(form,ans).errors:
                text=form.fields[ans].get_bound_field(form,ans).errors.as_text()
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
            if value=="":
                error_html_text = error_html_text          
                error_in_answers=True
        
        
        html_field=form.fields[ans].get_bound_field(form,ans).__str__()
        #print("html_field={}".format(html_field))
        output_string="{}<br/>{}".format(output_string,html_field)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
        #print("-----{}------".format(output_string))
        #print("{} {}".format(output_string,error_html))
        #output_string="{}<br/>{}".format(output_string,html_field)
        counter+=1
        
    if form.is_bound:    
        if error_in_answers:
            status_html='<div class="wrapper-status"><div class="status explanation-message">{}</div></div>'.format(format_error_text(error_html_text))   
        else:
            status_html='<div class="wrapper-status"><div class="status success-message">Excelent</div></div>'
    else:
        status_html=""
    output_string=re.sub(r'<select ',r'<select class="selectstrove" ',output_string)    
    return mark_safe("{} {}".format(output_string,status_html))    

        
@register.simple_tag
def excersise_construct_a_sentence(excersise_text,form,sentences,id_num):

    sentences_iterator=iter(sentences)
    
    output_string=""
    drop_answer_string='<div class="drag-n-drop-answers-wrapper">'
    words_for_drag_n_drop='<div class="drag-n-drop-wrapper">'
    error_html=""
    error_html_text=""
    error_in_answers=False
    counter=1
    
    for sentence in sentences_iterator:

        value=form.fields[sentence].get_bound_field(form,sentence).value()
        #[words_for_drag_n_drop_gen,drop_answer_string_gen] = generate_drag_n_drop_answer_choice_html(answer=excersise_text,answered_val=value,id_num=id_num)
        #print("my value {}".format(value))

        
        if form.is_bound:
            
            if form.fields[sentence].get_bound_field(form,sentence).errors:
                text=form.fields[sentence].get_bound_field(form,sentence).errors.as_text()
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
                [words_for_drag_n_drop_gen,drop_answer_string_gen] = generate_drag_n_drop_answer_choice_html(answer=excersise_text,answered_val=value,id_num=id_num)
            else:
                [words_for_drag_n_drop_gen,drop_answer_string_gen] = generate_drag_n_drop_answer_choice_html(answer=excersise_text,answered_val=value,id_num=id_num,answered_true=True)
                pass
                
            if value=="":
                text="This can't be empty"
                error_html_text = error_html_text + str(counter) + " " + text + "<br>"            
                error_in_answers=True
        else:
            [words_for_drag_n_drop_gen,drop_answer_string_gen] = generate_drag_n_drop_answer_choice_html(answer=excersise_text,answered_val=value,id_num=id_num)
        

        words_for_drag_n_drop += words_for_drag_n_drop_gen
        drop_answer_string    += drop_answer_string_gen
        
        html_field=form.fields[sentence].get_bound_field(form,sentence).__str__()
        #print("dir=",dir(form.fields[sentence].get_bound_field(form,sentence)))
        #print("obj=",form.fields[sentence].get_bound_field(form,sentence))
        #print("value=",value)
        output_string += html_field 
        #output_string=re.sub(r'\$\$\$',html_field,output_string,count=1)
        #output_string=re.sub(r'\$\$\$',"<br/>",output_string,count=1)
        #print("{} {}".format(output_string,error_html))
        counter+=1
        
        #ans=next(it)
    output_string += drop_answer_string + "</div>"    
    output_string += words_for_drag_n_drop + "</div>"
    
    if form.is_bound:    
        if error_in_answers:
            status_html='<div class="wrapper-status"><div class="status explanation-message">{}</div></div>'.format(format_error_text(error_html_text))   
        else:
            status_html='<div class="wrapper-status"><div class="status success-message">Excelent !</div></div>'
    else:
        status_html=""
    
    #output_string=re.sub(r'<select ',r'<select class="selectstrove" ',output_string)    
    return mark_safe("{} {}".format(output_string,status_html))    
        


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)