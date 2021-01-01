# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:05:30 2019

@author: A
"""


from django.urls import path, re_path
from . import views

urlpatterns = [
     path('', views.index, name='index_lt'),
     path('topics/', views.TopicListView.as_view(), name='topics'),
     path('topics/<int:pk>', views.topic_view, name='topic'),
     #path('topics/', views.index, name='topics'),
     path('tutorials/', views.TutorialsListView.as_view(), name='tutorials'),
     path('languagetest/<int:pk>', views.LanguageTestDetailView.as_view(), name='languagetest_detail'),
]

urlpatterns += [
        path('languagetest/<int:pk>/take_a_test', views.pass_a_test, name='take_a_test'),
        path('tutorials/<int:pk>', views.tutorial_view, name='tutorial'),
]