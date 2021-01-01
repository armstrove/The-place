from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http import Http404
# from django.views.generic.edit import FormView
# from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured


from languageTests.forms import TakeATestDummy

from .validators import validate_excersise_choose_the_word
from .validators import validate_excersise_construct_a_sentence  
from .validators import validate_excersise_type_the_word
from .validators import validate_excersise_type_the_sentence
from .validators import validate_excersise_type_the_sentence_inline
from .validators import validate_excersise_click_the_correct_option

from analytics.signals import object_viewed_signal
from analytics.mixins import ObjectViewedMixin
from .signals         import topic_viewed_signal
from .signals         import test_viewed_signal
from .signals         import test_attempt_signal


from .widgets import DragnDropWidget
from .widgets import RadioSelectClick
from django.forms.widgets import Input
from django.forms.fields import CharField
from languageTests.fields import DragNDropField , CharFieldEmpty, ChoiceFieldEmpty


from progress.models import TopicProgress
from progress.models import TestProgress




from django import forms
import json
import re
import pprint

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
        
        language_tests_to_view = LanguageTest.objects.all()
        if self.request.GET.get('level'):
            level = self.request.GET.get('level')
            if level != "All":
                language_tests_to_view = language_tests_to_view.filter(level=level)
        #all_language_tests = all_language_tests.filter(level='b')
        #for language_test in language_tests_to_view:
        #    test_progress=TestProgress.objects.get_or_create(user=self.request.user, language_test=language_test)
            
            
        context["language_test_list"]=language_tests_to_view
        context["levels"]=LanguageTest.LEVELS
        return context

class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "Topic_list"
    template_name = "Topic_list.html"

    def get_context_data(self, **kwargs):
        context = super(TopicListView, self).get_context_data(**kwargs)
        
        topics_to_view = Topic.objects.all()
        if self.request.GET.get('level'):
            level = self.request.GET.get('level')
            if level != "All":
                topics_to_view = topics_to_view.filter(level=level)
                
        topics_with_progress_info = []        
        for topic in topics_to_view:
            #pprint.pprint(dir(self.request.user))
            topic_progress=None
            if self.request.user.is_authenticated:
                topic_progress=TopicProgress.objects.get_or_create(user=self.request.user, topic=topic)
            topics_with_progress_info.append({'topic':topic,
                                              'progress':topic_progress,
                                              })
                
        context["Topic_list"] = topics_with_progress_info
        context["levels"]     = Topic.LEVELS
        return context

class TopicDetailView(ObjectViewedMixin, generic.DetailView):
    model = Topic

    def get_object(self, *args, **kwargs):
        request=self.request
        pk = self.kwargs.get('pk')
        qs = Topic.objects.get_by_pk(pk)
        instance = qs.first()
        if instance is None:
            raise Http404("Topic doesn't exist")
        #print("instance=<{}>".format(instance))
        if self.request.user.is_authenticated:
            topic_viewed_signal.send(instance.__class__,instance=instance,request=request)
        return instance

    def get_context_data(self, *args, **kwargs):
        context=super(TopicDetailView, self).get_context_data(*args, **kwargs)
        #topic = get_object_or_404(Topic,pk=self.kwargs.get('pk'))
        language_tests_to_view = self.object.languagetest_set.all().order_by('number')
        
        tests_with_progress_info=[]
        for language_test in language_tests_to_view:
            test_progress=None
            if self.request.user.is_authenticated:
                test_progress,status=TestProgress.objects.get_or_create(user=self.request.user, language_test=language_test)
            tests_with_progress_info.append({'test':language_test,
                                             'progress':test_progress,
                                             })
            
        #context["language_test_list"]=tests_with_progress_info
        context = {
                'topic': self.object,
                'language_tests': tests_with_progress_info
        } 
        #pprint.pprint(context)
        return context
    
#    topic = get_object_or_404(Topic, pk=pk)
#    language_tests = topic.languagetest_set.all()
#    context  = {
#         'topic': topic,
#         'language_tests': language_tests
#    }
#    return render(request, 'languageTests/topic.html', context)

    
class LanguageTestDetailView(ObjectViewedMixin, generic.FormView):
    model = LanguageTest 
    form_class = TakeATestDummy
    template_name = 'languageTests/take_a_test.html'
    success_url = reverse_lazy('topics')

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        print("^^^^^^^^^^")
        language_test=self.get_object()
        topic_pk=language_test.topic_id
        # pprint.pprint(dir(obj))
        # pprint.pprint(obj)
        print("##########")
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url + str(topic_pk))  # success_url may be lazy

    def get_object(self, *args, **kwargs):
        request=self.request
        pk = self.kwargs.get('pk')
        qs = LanguageTest.objects.get_by_pk(pk)
        instance = qs.first()
        if instance is None:
            raise Http404("Topic doesn't exist")
        # print("instance=<{}>".format(instance))
        topic_viewed_signal.send(instance.__class__,instance=instance,request=request)
        return instance

    def get_form(self, form_class=None):
          request=self.request
          language_test=self.get_object()

          content={}

          if check_field_name_is_in_post(request):
            for key in request.POST.keys():
                if key != 'csrfmiddlewaretoken':
                    #print("Key============{}".format(key))
                    content[key] = request.POST[key]

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
                       # new_fields[new_field_name]=forms.CharField(help_text="Hello", required=False, validators=[validate_excersise_type_the_word(answer=answer)])
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
          #if form.is_valid():
          #    form.full_clean
          #    print("form<{}>".format(dir(form.data)))
          #    print("form<{}>".format(form.data.items()))
          #    print("form is valid !!!")

          #    context = {
          #        'form': form,
          #        'language_test': language_test,
          #    }
          #    test_attempt_signal.send(language_test.__class__,instance=language_test,request=request,passed=True)
          #    return render(request, 'languageTests/success.html', context)
          #else:
          #    test_attempt_signal.send(language_test.__class__,instance=language_test,request=request,passed=False)
          #if form.is_valid():
          #  form.full_clean
          #if 'form' not in kwargs:
          #      kwargs['form'] = form
          #      kwargs['language_test'] = language_test
          #return super().get_context_data(**kwargs)
          return form
      
    def get_context_data(self, **kwargs):
        print("GET_CONTENT")
        language_test=self.get_object()
        #if 'form' not in kwargs:
        kwargs['form'] = self.get_form()
        kwargs['language_test'] = language_test
        kwargs['object'] = language_test
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        print("GET")
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())  

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        language_test = self.get_object()
        form = self.get_form()
        if form.is_valid():
            if self.request.user.is_authenticated:
                test_attempt_signal.send(language_test.__class__,instance=language_test,request=self.request,passed=True)
            return self.form_valid(form)
        else:
            if self.request.user.is_authenticated:
                test_attempt_signal.send(language_test.__class__,instance=language_test,request=self.request,passed=False)
            return self.form_invalid(form)
    
    # def get_initial(self):
    #       initial = super(LanguageTestDetailView, self).get_initial()
    #       #initial.update({'form':form, 'language_test':language_test })
    #       return initial
    # def get_context_data(self, *args, **kwargs):
    #     context=super(LanguageTestDetailView, self).get_context_data(*args, **kwargs)
    #     #context['languagetest']=self.get_object()
    #     context['languagetest']=self.object
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     request  = self.request
    #     pk       = self.kwargs.get('pk')
    #     #pprint.pprint(dir(LanguageTest.objects))
    #     instance = LanguageTest.objects.get_by_pk(pk)
    #     if instance is None:
    #         raise Http404("LanguageTest doesn't exist")
    #     return instance
  

def check_field_name_is_in_post(request):
    field_names=["ans_choose_the_word","ans_t","ans_ts","sentence","ans_type_the_word_faded","ans_type_the_sentence_inline","ans_click_the_correct_option"]
    for field_name in field_names:
        if str(field_name)+"0" in request.POST:
            return True
    return False    
    
def pass_a_test(request, pk):
    language_test = get_object_or_404(LanguageTest, pk=pk)
    content={}
    test_viewed_signal.send(language_test.__class__,instance=language_test,request=request)
    
    if request.method == 'POST':
        #if "ans0" in request.POST or "sentence0" in request.POST:
        if check_field_name_is_in_post(request):
            for key in request.POST.keys():
                if key != 'csrfmiddlewaretoken':
                    #print("Key============{}".format(key))
                    content[key] = request.POST[key]
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
            test_attempt_signal.send(language_test.__class__,instance=language_test,request=request,passed=True)
            return render(request, 'languageTests/success.html', context)
        else:
            test_attempt_signal.send(language_test.__class__,instance=language_test,request=request,passed=False)
    context = {
        'form': form,
        'language_test': language_test,
    }

    return render(request, 'languageTests/take_a_test.html', context)


def tutorial_view(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    context = {
         'tutorial': tutorial
    }
    return render(request, 'languageTests/tutorial.html', context)


def topic_view(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    language_tests = topic.languagetest_set.all()
    context = {
         'topic': topic,
         'language_tests': language_tests
    }
    return render(request, 'languageTests/topic.html', context)
