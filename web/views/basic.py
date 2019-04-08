from django.views.generic import TemplateView

class SurveyIndexView(TemplateView):

    template_name = "web/index.html"

    extra_context = {
        "title": "欢迎使用问卷调查系统苑昊"
    }


class SurveyDetailView(TemplateView):
    template_name = "web/index.html"

    extra_context = {
        "title": "欢迎使用问卷调查系统苑昊"
    }
