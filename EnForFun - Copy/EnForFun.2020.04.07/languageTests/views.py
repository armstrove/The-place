from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from languageTests.forms import TakeATestDummy

from .validators import validate_excersise_choose_the_word
from .validators import validate_excersise_construct_a_sentence  
from .validators import validate_excersise_type_the_word
from .validators import validate_excersise_type_the_sentence
from .validators import validate_excersise_type_the_sentence_inline
from .validators import validate_excersise_click_the_correct_option

from analytics.signals import object_viewed_signal
from analytics.mixins import ObjectViewedMixin


from .widgets import DragnDropWidget
from .widgets import RadioSelectClick
from django.forms.widgets import Input
from django.forms.fields import CharField
from languageTests.fields import DragNDropField , CharFieldEmpty, ChoiceFieldEmpty

from django import forms
import json
import re

from types import MethodType

# Create your views here.

from languageTests.models import Language, Excersise, LanguageTest, Tutorial, Topic

def index(request):
    """View function for home page of site."""

    # Number of visits to this view, as counted in the session variable.
    num_visits_l = request.session.get('num_visits_l', 0)
    request.session['num_visits_l'] = num_visits_l + 1
    
    # Generate counts of some of the main objects
    num_lang_tests = LanguageTest.objects.all().count()
     
    context = {
        'num_lang_tests': num_lang_tests,
        'num_visits': num_visits_l,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index2.html', context=context)

class TutorialsListView(generic.ListView):
    model = Tutorial
    context_object_name = "tutorial_list"
    template_name = "tutorials_list.html"

    def get_context_data(self, **kwargs):
        context = super(TutorialsListView, self).get_context_data(**kwargs)
        all_tutorials = Tutorial.objects.all()
        filtered_tutorials = all_tutorials
        if self.request.GET.get('level'):
            level = self.request.GET.get('level')
            if level != "All":
                filtered_tutorials = all_tutorials.filter(level=level)
        context["tutorials_list"]=filtered_tutorials
        context["levels"]=Tutorial.LEVELS
        return context
    
class LanguageTestListView(generic.ListView):
    model = LanguageTest
    context_object_name = "language_test_list"
    template_name = "languageTests_list.html"

    def get_context_data(self, **kwargs):
        context = super(LanguageTestListView, self).get_context_data(**kwargs)
        
        all_language_tests = LanguageTest.objects.all()    
        if self.request.GET.get('level'):
            level = self.request.GET.get('level')
            if level != "All":
                all_language_tests = all_language_tests.filter(level=level)
        #all_language_tests = all_language_tests.filter(level='b')    
        context["language_test_list"]=all_language_tests
        context["levels"]=LanguageTest.LEVELS
        return context

class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "Topic_list"
    template_name = "Topic_list.html"

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        
        all_topics = Topic.objects.all()    
        if self.request.GET.get('level'):
            level = self.request.GET.get('level')
            if level != "All":
                all_topics = all_topics.filter(level=level)
        #all_language_tests = all_language_tests.filter(level='b')    
        context["Topic_list"]=all_topics
        context["levels"]=Topic.LEVELS
        return context
    
class LanguageTestDetailView(generic.DetailView):
    model = LanguageTest   
    

def check_field_name_is_in_post(request):
    field_names=["ans_choose_the_word","ans_t","ans_ts","sentence","ans_type_the_word_faded","ans_type_the_sentence_inline","ans_click_the_correct_option"]
    for field_name in field_names:
        if str(field_name)+"0" in request.POST:
            return True
    return False    
    
def pass_a_test(request, pk):
    language_test = get_object_or_404(LanguageTest, pk=pk)
    content={}
    object_viewed_signal.send(language_test.__class__,instance=language_test,request=request)
    
    if request.method == 'POST':
        #if "ans0" in request.POST or "sentence0" in request.POST:
        if check_field_name_is_in_post(request):
            for key in request.POST.keys():
                if key != 'csrfmiddlewaretoken':
                    #print("Key============{}".format(key))
                    content[key] = request.POST[key]
            #language_test.answers = json.dumps(content)
            #language_test.save()
        #Create a form instance and populate it with data from the request (binding):
        #form = TakeATest(request.POST)
            
        # Check if the form is valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_instance.due_back = form.cleaned_data['renewal_date']
            #book_instance.save()
            #pass
            # redirect to a new URL:
            #return HttpResponseRedirect(('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        pass
        #proposed_renewal_date = "a"
        #form = TakeATest(initial={'language_test': "a"})
    
    new_fields={}
    tests_dict={}
    counter_w=0
    counter_s=0
    counter_t=0
    counter_ts=0 
    counter_tsi=0
    counter_cco=0
    for excersise in language_test.excersise_set.all():
         tests_dict[excersise.id]=[]
         if excersise.exercise_type == 'w': 
            for answer in excersise.answer_set.all():
                ANSWER_CHOICES=[]
                ANSWER_CHOICES.append((" ",""))#added for default null 
                tests_dict[excersise.id].append(answer)
                for possible_answer in answer.possible_answers.split('/'):
                    ANSWER_CHOICES.append((possible_answer,possible_answer))
                ANSWER_CHOICES=tuple(ANSWER_CHOICES)
                new_field_name="ans_choose_the_word" + str(counter_w)
                new_fields[new_field_name]=ChoiceFieldEmpty(choices = ANSWER_CHOICES, widget=forms.Select(),required=False , help_text="Choose the word", validators=[validate_excersise_choose_the_word(answer=answer)])
                #new_fields[new_field_name]=forms.ChoiceField(choices = ANSWER_CHOICES, widget=forms.Select(),required=False , help_text="Hello", validators=[validate_excersise_choose_the_word(answer=answer)])
                tests_dict[excersise.id].append(new_field_name)
                counter_w=counter_w+1
         elif excersise.exercise_type == 's':
             new_field_name="sentence" + str(counter_s)
             new_fields[new_field_name]=DragNDropField(widget=DragnDropWidget, required=False, validators=[validate_excersise_construct_a_sentence(sentence=excersise.text)])
             tests_dict[excersise.id].append(new_field_name)
             counter_s=counter_s+1
             pass
         elif excersise.exercise_type == 't':
             for answer in excersise.answer_set.all():
                 new_field_name="ans_t" + str(counter_t)
                 new_fields[new_field_name]=CharFieldEmpty(help_text="Type the word", required=False, validators=[validate_excersise_type_the_word(answer=answer)],widget=forms.TextInput(attrs={'autocomplete':'off'}))
                 #new_fields[new_field_name]=forms.CharField(help_text="Hello", required=False, validators=[validate_excersise_type_the_word(answer=answer)])
                 tests_dict[excersise.id].append(new_field_name)
                 counter_t=counter_t+1
         elif excersise.exercise_type == 'ts':
             for answer in excersise.answer_set.all():
                 new_field_name="ans_ts" + str(counter_ts)
                 new_fields[new_field_name]=CharFieldEmpty(help_text="Type the sentense", required=False, validators=[validate_excersise_type_the_sentence(answer=answer)])
                 #new_fields[new_field_name]=forms.CharField(help_text="Hello", required=False, validators=[validate_excersise_type_the_word(answer=answer)])
                 tests_dict[excersise.id].append(new_field_name)
                 counter_ts=counter_ts+1
         elif excersise.exercise_type == 'tsi':
             for answer in excersise.answer_set.all():
                 new_field_name="ans_type_the_sentence_inline" + str(counter_ts)
                 #initial_text=re.sub(r"\$\$\$",r"",excersise.text)
                 new_fields[new_field_name]=CharFieldEmpty(help_text="Type the sentense inline", required=False, initial=excersise.text, validators=[validate_excersise_type_the_sentence_inline(answer=answer)])
                 #new_fields[new_field_name]=CharFieldEmpty(help_text="Type the sentense inline", required=False, validators=[validate_excersise_type_the_sentence_inline(answer=answer)])
                 #new_fields[new_field_name]=forms.CharField(help_text="Hello", required=False, validators=[validate_excersise_type_the_word(answer=answer)])
                 tests_dict[excersise.id].append(new_field_name)
                 counter_ts=counter_tsi+1  
         elif excersise.exercise_type == 'cco':
             for answer in excersise.answer_set.all():
                 ANSWER_CHOICES=[]
                 #ANSWER_CHOICES.append((" ",""))#added for default null 
                 for possible_answer in answer.possible_answers.split('/'):
                    ANSWER_CHOICES.append((possible_answer,possible_answer))
                 ANSWER_CHOICES=tuple(ANSWER_CHOICES)
                 new_field_name="ans_click_the_correct_option" + str(counter_ts)
                 #initial_text=re.sub(r"\$\$\$",r"",excersise.text)
                 #new_fields[new_field_name]=ChoiceFieldEmpty(choices = ANSWER_CHOICES, widget=forms.RadioSelect(attrs={'class': "checkbox-answer"}), required=False, help_text="Click the correct option", validators=[validate_excersise_click_the_correct_option(answer=answer)])                 
                 new_fields[new_field_name]=ChoiceFieldEmpty(choices = ANSWER_CHOICES, widget=RadioSelectClick(attrs={'class': "checkbox-answer"}), required=False, help_text="Click the correct option", validators=[validate_excersise_click_the_correct_option(answer=answer)])                 
                 #new_fields[new_field_name]=CharFieldEmpty(help_text="Type the sentense inline", required=False, validators=[validate_excersise_type_the_sentence_inline(answer=answer)])
                 #new_fields[new_field_name]=forms.CharField(help_text="Hello", required=False, validators=[validate_excersise_type_the_word(answer=answer)])
                 tests_dict[excersise.id].append(new_field_name)
                 counter_ts=counter_cco+1         
         elif excersise.exercise_type == 'tf':
             for answer in excersise.answer_set.all():
                 new_field_name="ans_type_the_word_faded" + str(counter_ts)
                 new_fields[new_field_name]=CharFieldEmpty(help_text="Type the word faded", required=False,  validators=[validate_excersise_type_the_word(answer=answer)], widget= forms.TextInput(attrs={'placeholder':answer.possible_answers}))
                 #new_fields[new_field_name]=forms.CharField(help_text="Hello", required=False, validators=[validate_excersise_type_the_word(answer=answer)])
                 tests_dict[excersise.id].append(new_field_name)
                 counter_ts=counter_ts+1 
         else:
             print("Error:views.py: Can't find the excercise type: '" + excersise.exercise_type + "'")

    TakeATest=type('TakeATest',(TakeATestDummy,),new_fields)
    
    if request.method == 'POST':
        form=TakeATest(content)
    else:
        form=TakeATest()
    form.set_tests_dict(tests_dict)
    if request.method == 'POST':
        if form.is_valid():
            form.full_clean
            print("form<{}>".format(dir(form.data)))
            print("form<{}>".format(form.data.items())) 
            print("form is valid !!!")
            pass
            context = {
                'form': form,
                'language_test': language_test,
            }
            return render(request, 'languageTests/success.html', context)
    context = {
        'form': form,
        'language_test': language_test,
    }
    
    

    return render(request, 'languageTests/take_a_test.html', context)
    
def tutorial_view(request, pk):    
    tutorial = get_object_or_404(Tutorial, pk=pk)
    context  = {
         'tutorial': tutorial
    }
    return render(request, 'languageTests/tutorial.html', context)
    
def topic_view(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    language_tests = topic.languagetest_set.all()
    context  = {
         'topic': topic,
         'language_tests': language_tests
    }
    return render(request, 'languageTests/topic.html', context)