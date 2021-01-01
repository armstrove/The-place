# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:05:30 2019

@author: A
"""


from django.urls import path, re_path
from . import views

urlpatterns = [
     path('', views.index, name='index_lt'),
     path('languagetests/', views.LanguageTestListView.as_view(), name='languagetests'),
     path('languagetest/<int:pk>', views.LanguageTestDetailView.as_view(), name='languagetest_detail'),
]

urlpatterns += [
        path('languagetest/<int:pk>/take_a_test', views.pass_a_test, name='take_a_test'),
]