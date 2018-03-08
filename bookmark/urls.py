# bookmark/urls
from django.conf.urls import url
from django.views.generic import ListView, DetailView
# from .views import BookmarkLV, BookmarkDV
from .models import Bookmark

urlpatterns = [
    # Class-based view
    # url(r'^list/', BookmarkLV.as_view(), name="bookmark_list_view"),
    # url(r'^detail/(?P<pk>\d+)/$', BookmarkDV.as_view(), name="bookmark_detail_view"),
    # views.generic에 기반한 Class-based view
    url(r'^$', ListView.as_view(model=Bookmark), name="index"),  # list_view
    url(r'^detail/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name="detail_view"),
]