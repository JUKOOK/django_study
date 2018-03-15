# django_study/views
# 단순 템플릿만 보여주는 로직의 경우 generic view에서 generic.base의 TemplateView를 상속한다.
from django.views.generic.base import TemplateView

# 계정 관련 import
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

# login_required 함수 : 사용자가 로그인했는지를 확인해 로그인된 경우 원래 함수 실행, 아닌 경우 로그인 페이지로 redirect
from django.contrib.auth.decorators import login_required


class HomeView(TemplateView):
    template_name = 'home.html'  # 연결 html 이름 정의 (필수)


# 계정 관련 class-based view : 엥간한 것은 이미 되어 있다. 여기서는 기본이 없는 계정 등록에 관한 것만 view 만든다.
class UserCreateView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')  # 계정 생성이 완료되면 url register_done 의 view 실행


class UserCreateDoneView(TemplateView):
    template_name = 'registration/registration_done.html'



# LoginRequiredMixin 클래스 : login_required() 데코레이터 기능을 제공하기 위한 클래스.
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):  # as_view 메소드를 클래스 메소드로 정의한다.
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)