from django.urls import reverse
from django.template import loader
from rest_framework import serializers
from ..service.field import CustomCharField
from rest_framework.fields import DateTimeField
from rest_framework.fields import DateField

from web import models


class SurveySerializer(serializers.ModelSerializer):
    # 自定义方法. 数据库里面没有的字段
    number = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    handle = serializers.SerializerMethodField()
    by_class = CustomCharField()
    date = DateTimeField(format ='%Y-%m-%d %X')
    #by_class = CustomCharField(prefix=)
    class Meta:
        model = models.Survey
        fields = ("name","by_class",'number','link','date',"handle",)

    def get_number(self,instance):
        return instance.surveyrecord_set.count()

    def get_link(self,instance):
        request = self.context.get("request")
        # request.get_fullpath, 获得域名request.get_host
        return "{}{}".format(request.get_host(),reverse('survey_detail', args=(instance.pk, )))
    def get_handle(self,instance):
        return loader.render_to_string('commponts/button.html',{'href':instance.pk})