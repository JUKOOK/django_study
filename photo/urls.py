# photo/urls
from django.conf.urls import url
from .views import *

urlpatterns = [
    # 이곳의 name은 2계층 url 구조에 대해 namespace A:B 의 B가 된다.
    # class-based view의 경우 <클래스명>.as_view() 로 정의한다.

    # 기본 앨범 list
    url(r'^$', AlbumListView.as_view(), name="index"),
    url(r'^album/$', AlbumListView.as_view(), name="album_list"),

    # 앨범 detail /album/pk
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailView.as_view(), name="album_detail"),

    # 사진 detail /photo_detail/pk
    url(r'^photo_detail/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name="photo_detail"),
]

# 간단한 class-based view라서 views.py를 안 만드는 경우
# from django.views.generic import ListView, DetailView
# from .models import Album, Photo
# 클래스 이름 대신 ListView, DetailView 사용 -> () 안에 model=Album 혹은 model=Photo 넣으면 끝
