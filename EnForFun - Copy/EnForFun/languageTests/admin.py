from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.contenttypes.models import ContentType

# Register your models here.
from languageTests.models import Excersise, Language, LanguageTest, Topic, Answer, Explanation, Tutorial, TutorialComponent


class LanguageTestInline(admin.TabularInline):
#class ExcersiseInline(admin.StackedInline):
     model  = LanguageTest
     #fields = ['level','exercise_type','text', 'id', 'get_edit_link']
     fields = [ 'number', 'language', 'get_edit_link' ]
     readonly_fields = ["get_edit_link"]
     extra  = 0
     
     def get_edit_link(self, obj):      
       if obj.pk:
           return mark_safe("""<a href="{src}"><p>Edit Language Test</p></a>""".format(
               src=reverse('admin:%s_%s_change' % ( self.model._meta.app_label, self.model._meta.model_name), args=[str(obj.id)]) 
           ))
       return _("Save and continue please")
     
     get_edit_link.short_description = _("Edit link")
     get_edit_link.allow_tags = True

class ExcersiseInline(admin.TabularInline):
#class ExcersiseInline(admin.StackedInline):
     formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
      }   
     
     model  = Excersise
     fields = ['exercise_type','text','id', 'get_edit_link']
     readonly_fields = ["get_edit_link"]
     extra  = 0
     
     def get_edit_link(self, obj):      
       if obj.pk:
           return mark_safe("""<a href="{src}"><p>Edit excersise</p></a>""".format(
               src=reverse('admin:%s_%s_change' % ( self.model._meta.app_label, self.model._meta.model_name), args=[str(obj.id)]) 
           ))
       return _("Save and continue please")
     
     get_edit_link.short_description = _("Edit link")
     get_edit_link.allow_tags = True
     
     
class AnswerInline(admin.TabularInline):
    model = Answer
    extra  = 0
    fields = ['answer_string', 'possible_answers' ,'explanation_string' ,'get_edit_link']
    readonly_fields = ["get_edit_link"]    

    def get_edit_link(self, obj):      
      if obj.pk:
          return mark_safe("""<a href="{src}"><p>Edit Answer</p></a>""".format(
              src=reverse('admin:%s_%s_change' % ( self.model._meta.app_label, self.model._meta.model_name), args=[str(obj.id)]) 
          ))
      return _("Save and continue please")
    
    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True

class ExplanationInline(admin.TabularInline):
    model = Explanation
    extra = 0

    def get_edit_link(self, obj):      
      if obj.pk:
          return mark_safe("""<a href="{src}"><p>Edit Explanations</p></a>""".format(
              src=reverse('admin:%s_%s_change' % ( self.model._meta.app_label, self.model._meta.model_name), args=[str(obj.id)]) 
          ))
      return _("Save and continue please")
    
    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True

class TutorialComponentInline(admin.TabularInline):
    model = TutorialComponent
    extra = 0
    
    def get_edit_link(self, obj):      
      if obj.pk:
          return mark_safe("""<a href="{src}"><p>Edit Component</p></a>""".format(
              src=reverse('admin:%s_%s_change' % ( self.model._meta.app_label, self.model._meta.model_name), args=[str(obj.id)]) 
          ))
      return _("Save and continue please")
    
    get_edit_link.short_description = _("Edit link")
    get_edit_link.allow_tags = True

@admin.register(TutorialComponent)
class TutorialComponentAdmin(admin.ModelAdmin):
     list_display = [ 'component_type', 'tutorial' ]

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
     list_display = [ 'tutorial_title' ]
     inlines = [ TutorialComponentInline ]

@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
     list_display = [ 'answer' , 'explain_text' , 'language' ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
     list_display = [ 'excersise' , 'answer_string', 'explanation_string', 'possible_answers' ]
     inlines = [ ExplanationInline ]

@admin.register(Excersise)
class ExcersiseAdmin(admin.ModelAdmin):
     formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
     }   
     list_display = [ 'display_text' , 'exercise_type']
     inlines = [ AnswerInline ]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
     list_display = [ 'name' ]    
     
@admin.register(LanguageTest) 
class LanguageTestAdmin(admin.ModelAdmin):
     #list_display = [ 'title' , 'language', 'level']   
     list_display = [ 'number', 'language' ,'topic','task']
     inlines = [ ExcersiseInline ]
     

@admin.register(Topic) 
class TopicAdmin(admin.ModelAdmin):     
     list_display = [ 'title' , 'level'] 
     inlines = [ LanguageTestInline ]
     
     