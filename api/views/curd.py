# from django.views.generic import TemplateView

from rest_framework.generics import  ListAPIView
from ..serializer import  curd


from web import models

class SurveysApiView(ListAPIView):
    #  对问卷调查表序列化
    queryset = models.Survey.objects.all()

    # 序列化器
    serializer_class = curd.SurveySerializer



    def list(self,request,*args,**kwargs):
        
        return super(SurveysApiView,self).list(request,*args,**kwargs)