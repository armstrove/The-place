from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from languageTests.forms import TakeATestDummy
from .validators import validate_excersise_answers


from django import forms
from .forms import TakeATestDummy
import json

from types import MethodType

# Create your views here.

from languageTests.models import Language, Excersise, LanguageTest

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

class LanguageTestListView(generic.ListView):
    model = LanguageTest
    context_object_name = "language_test_list"
    template_name = "languageTests_list.html"
    
    
class LanguageTestDetailView(generic.DetailView):
    model = LanguageTest   
    
    
def pass_a_test(request, pk):
    language_test = get_object_or_404(LanguageTest, pk=pk)
    content={}
    if request.method == 'POST':
        if "ans0" in request.POST:
            for key in request.POST.keys():
                if key != 'csrfmiddlewaretoken':
                    content[key] = request.POST[key]
            #language_test.answers = json.dumps(content)
            #language_test.save()
        # Create a form instance and populate it with data from the request (binding):
        #form = TakeATest(request.POST)
            
        # Check if the form is valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #book_instance.due_back = form.cleaned_data['renewal_date']
            #book_instance.s ave()
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
    for excersise in language_test.excersise_set.all():
        tests_dict[excersise.id]=[]
        for answer in excersise.answer_set.all():
            ANSWER_CHOICES=[]
            ANSWER_CHOICES.append(("",""))
            tests_dict[excersise.id].append(answer)

            for possible_answer in answer.possible_answers.split('/'):   
                ANSWER_CHOICES.append((possible_answer,possible_answer))
            ANSWER_CHOICES=tuple(ANSWER_CHOICES)

            new_field_name="ans" + str(counter)
            #new_fields[new_field_name]=forms.ChoiceField(choices = ANSWER_CHOICES, required=True, help_text="Hello")
            new_fields[new_field_name]=forms.ChoiceField(choices = ANSWER_CHOICES, required=False, help_text="Hello", validators=[validate_excersise_answers(answer=answer)])
            
            tests_dict[excersise.id].append(new_field_name)
            counter=counter+1


    #def clean(self):
    #        cleaned_data = super(TakeATest, self).clean()
    #        print("cleaned data =<{}>".format(cleaned_data))
    #        for answer_field in cleaned_data:
    #            print(answer_field)
    #            value=cleaned_data.get(answer_field)
    #            print("value={}".format(value))

    TakeATest=type('TakeATest',(TakeATestDummy,),new_fields)
    
    #content={'id_1':'yes','id_2':'no'}
    #print("content<")
    #print(content)
    #print(">content")
    form=TakeATest(content)
    #form.clean=MethodType(clean,form)
    form.set_tests_dict(tests_dict)
    
    if request.method == 'POST':
        if form.is_valid():
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
    
    
    
    
    