from django.contrib import admin
from django.urls import path,include,re_path
from .views import  basic
urlpatterns = [
    path('', basic.SurveyIndexView.as_view()),
    re_path('(?P<pk>\d+)/',basic.SurveyDetailView.as_view, name='survey_detail')

]

