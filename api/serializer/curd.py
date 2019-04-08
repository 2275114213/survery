
from rest_framework import serializers
from ..service.field import CustomCharField

from web import models


class SurveySerializer(serializers.ModelSerializer):

    number = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    handle = serializers.SerializerMethodField()
    by_class = CustomCharField()


    #by_class = CustomCharField(prefix=)
    class Meta:
        model = models.Survey
        fields = ("name","by_class",'number','link','date',"handle")

    def get_number(self,instance):
        return instance.surveyrecord_set.count()

    def get_link(self,instance):
        request = self.context.get("request")
    def get_handle(self,instance):
        return "查看报告"