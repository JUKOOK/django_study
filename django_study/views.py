# django_study/views
# 단순 템플릿만 보여주는 로직의 경우 generic view에서 generic.base의 TemplateView를 상속한다.
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'  # 연결 html 이름 정의 (필수)
