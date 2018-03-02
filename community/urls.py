# community/urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^write/', views.write, name="community_write"),
    url(r'^list/', views.list, name="community_list"),
    url(r'^go/(?P<num>[0-9]+)/$', views.goToview, name="community_goToview"),
    # 정규표현식 : 한 자리 이상 숫자가 들어올 수 있다, 그 숫자는 num 변수에 전달된다.
]