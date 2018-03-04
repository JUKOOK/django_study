# blog/urls
from django.conf.urls import url
from .views import *

urlpatterns = [
    # 이곳의 name은 2계층 url 구조에 대해 namespace A:B 의 B가 된다.
    # class-based view의 경우 <클래스명>.as_view() 로 정의한다.

    # 기본 list 보기 -> / 또는 /post/
    url(r'^$', PostLV.as_view(), name="index"),
    url(r'^post/$', PostLV.as_view(), name="post_list"),

    # /post/django-slug_ex/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name="post_detail"),

    # /archive/ 기본, 전체 기록 보관소
    url(r'^archive/$', PostAV.as_view(), name="post_archive"),

    # /archive/2012/ 년도별 보관소
    url(r'^archive/(?P<year>\d{4})/$', PostYAV.as_view(), name="post_year_archive"),

    # /archive/2012/nov 연월별 보관소
    url(r'^archive/(?P<year>\d{4})/3월/$', PostMAV.as_view(), name="post_month_archive"),

    # /archive/2012/nov/10/ 일자별 보관소
    url(r'^archive/(?P<year>\d{4})/3월/(?P<day>\d{1,2})/$', PostDAV.as_view(), name="post_day_archive"),

    # /today/ 금일 보관소
    url(r'^today/$', PostTAV.as_view(), name="post_today_archive"),
]