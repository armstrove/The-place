from django.contrib import admin
from progress.models import TopicProgress, TestProgress


@admin.register(TopicProgress)
class TopicProgressAdmin(admin.ModelAdmin):
     #list_display = [ 'user','started','finished']    
     list_display  = [ 'user','topic','started','finished','visited_times']    
     search_fields = ('user__email','topic__title')
     ordering = ('user',) 
     list_filter  = ('user','topic') 

@admin.register(TestProgress)
class TestProgressAdmin(admin.ModelAdmin):
     list_display  = [ 'user','language_test','started','finished','visited_times','passed_times','failed_times']  
     list_filter  = ('user','language_test') 
     ordering = ('user',)

#@admin.register(ProgressProfile)
#class ProgressProfileAdmin(admin.ModelAdmin):
#     list_display = [ 'user','topic_progress']       