from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from languageTests.forms import TakeATestDummy
from .validators import validate_excersise_answers,validate_excersise_answers_drag_and_drop
from .widgets import DragnDropWidget
from django.forms.widgets import Input
from django.forms.fields import CharField
from languageTests.fields import DragNDropField

from django import forms
import json

from types import MethodType

# Create your views here.

from languageTests.models import Language, Excersise, LanguageTest, Tutorial

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
    
class LanguageTestDetailView(generic.DetailView):
    model = LanguageTest   
    

    
def pass_a_test(request, pk):
    language_test = get_object_or_404(LanguageTest, pk=pk)
    content={}
    if request.method == 'POST':
        if "ans0" in request.POST or "sentence0" in request.POST:
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
    counter=0
    counter_w=0    
    for excersise in language_test.excersise_set.all():
         tests_dict[excersise.id]=[]
         if excersise.exercise_type == 'w': 
            for answer in excersise.answer_set.all():
                ANSWER_CHOICES=[]
                ANSWER_CHOICES.append((" ",""))
                tests_dict[excersise.id].append(answer)
                for possible_answer in answer.possible_answers.split('/'):
                    ANSWER_CHOICES.append((possible_answer,possible_answer))
                ANSWER_CHOICES=tuple(ANSWER_CHOICES)
                new_field_name="ans" + str(counter)
                new_fields[new_field_name]=forms.ChoiceField(choices = ANSWER_CHOICES, widget=forms.Select(),required=False , help_text="Hello", validators=[validate_excersise_answers(answer=answer)])
                tests_dict[excersise.id].append(new_field_name)
                counter=counter+1
         elif excersise.exercise_type == 's':
             new_field_name="sentence" + str(counter_w)
             #print(excersise.text)
             #new_fields[new_field_name]=DragNDropField(widget=Input, required=True, validators=[validate_excersise_answers_drag_and_drop(sentence=excersise.text)])
             #new_fields[new_field_name]=CharField(required=True, validators=[validate_excersise_answers_drag_and_drop(sentence=excersise.text)])
             #new_fields[new_field_name]=CharField(required=True)
             new_fields[new_field_name]=DragNDropField(widget=DragnDropWidget, required=False, validators=[validate_excersise_answers_drag_and_drop(sentence=excersise.text)])
             #new_fields[new_field_name]=DragNDropField()
             tests_dict[excersise.id].append(new_field_name)
             counter_w=counter_w+1
             pass
         else:
             print("Error: Can't find the excercise type: '" + excersise.exercise_type + "'")

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
    
    