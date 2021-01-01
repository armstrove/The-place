from django.contrib import admin

# Register your models here.
from languageTests.models import Excersise, Language, LanguageTest


class ExcersiseInline(admin.TabularInline):
     model  = Excersise
     fields = ['display_language_test']
     extra  = 0

@admin.register(Excersise)
class ExcersiseAdmin(admin.ModelAdmin):
     list_display = [ 'display_text' , 'level' , 'language_test']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
     list_display = [ 'name' ]    
     
@admin.register(LanguageTest) 
class LanguageTestAdmin(admin.ModelAdmin):
     list_display = [ 'title' , 'language', 'level']   
     inlines = [ ExcersiseInline ]