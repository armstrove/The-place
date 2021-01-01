from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.contenttypes.models import ContentType

# Register your models here.
from languageTests.models import Excersise, Language, LanguageTest, Answer, Explanation


class ExcersiseInline(admin.TabularInline):
#class ExcersiseInline(admin.StackedInline):
     model  = Excersise
     fields = ['level', 'text', 'id', 'get_edit_link']
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
    fields = ['answer_string', 'possible_answers' ,'get_edit_link']
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

@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
     list_display = [ 'answer' , 'explain_text' , 'language' ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
     list_display = [ 'excersise' , 'answer_string', 'possible_answers' ]
     inlines = [ ExplanationInline ]

@admin.register(Excersise)
class ExcersiseAdmin(admin.ModelAdmin):
     list_display = [ 'display_text' , 'level' , 'language_test']
     inlines = [ AnswerInline ]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
     list_display = [ 'name' ]    
     
@admin.register(LanguageTest) 
class LanguageTestAdmin(admin.ModelAdmin):
     list_display = [ 'title' , 'language', 'level']   
     inlines = [ ExcersiseInline ]