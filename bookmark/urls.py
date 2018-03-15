# bookmark/urls
from django.conf.urls import url
from django.views.generic import ListView, DetailView
# from .views import BookmarkLV, BookmarkDV
from .models import Bookmark
from .views import *  # 북마크 포스트 생성, 수정, 삭제를 사이트 내에서 하기위한 view 클래스들 import

urlpatterns = [
    # Class-based view
    # url(r'^list/', BookmarkLV.as_view(), name="bookmark_list_view"),
    # url(r'^detail/(?P<pk>\d+)/$', BookmarkDV.as_view(), name="bookmark_detail_view"),
    # views.generic에 기반한 Class-based view
    url(r'^$', ListView.as_view(model=Bookmark), name="index"),  # list_view
    url(r'^detail/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name="detail_view"),

    # 북마크 포스트 추가, 자기가 만든.. 수정 가능한 레코드 리스트 보기, 수정, 삭제
    # /add/
    url(r'^add/$', BookmarkCreateView.as_view(), name="add_bookmark"),
    # /change
    url(r'^change/$', BookmarkChangeListView.as_view(), name="changeable_bookmark"),
    # /99/update
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdateView.as_view(), name="update_bookmark"),
    # /00/add/
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDeleteView.as_view(), name="delete_bookmark"),
]