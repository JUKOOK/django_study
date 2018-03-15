"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView, UserCreateView, UserCreateDoneView

# photo 앱 제작부터 추가
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),  # 첫 페이지 view

    # 계정 인증 관련 url-view 사상
    url(r'^accounts/', include('django.contrib.auth.urls')),  # 이미 대부분의 계정 관련 urls가 포함되었음.
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneView.as_view(), name='register_done'),

    # 이곳의 namespace는 2계층 url 구조에 대해 namespace A:B 의 A가 된다.
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^apisample/', include('restAPI.urls', namespace='restAPI')),
    url(r'^community/', include('community.urls', namespace='community')),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^photo/', include('photo.urls', namespace='photo')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 기존 url 패턴에 static() 함수가 반환하는 URL 패턴을 추가한다.
# 즉, MEDIA_URL -> /media/ URL 요청이 오면 django.views.static.serve() 함수가 처리하되, 이 함수에
# document_root=settings.MEDIA_ROOT 키워드 인자가 전달된다.

# auth 제공 계정 인증 url name - view : urlpattern은 /accounts/~~ 형식이다.
# login, logout, logout_then_login
# password_change, password_change_done
# password_reset, password_reset_done, password_reset_confirm, password_reset_complete
