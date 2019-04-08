from django.urls import path
from .views import  curd

urlpatterns = [
    path("surveys/",curd.SurveysApiView.as_view())

]