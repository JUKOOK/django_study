# blog/views
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# \ 이용하면 두 줄로 쓸 수 있다.
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView


# views.generic 기반한 class-based view 정의
# 클래스형 제네릭 뷰 : 장고가 잡아주는 2가지 속성

# ListView, ArchiveView들 전부
#               // 1. 컨텍스트 변수로 object_list를 정의했음
#               // 2. 연결되는 템플릿 이름의 default는 <모델명소문자>_list.html로 정해짐
#               // 3. ArchiveView들의 연결 템플릿 이름도 마찬가지 방식으로...

# DetailView  // 1. 컨텍스트 변수로 object를 정의했음
#             // 2. 연결되는 템플릿 이름의 default는  <모델명소문자>_detail.html로 정해짐

from .models import Post  # 사용 model import


# ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 연결 template 이름 설정
    context_object_name = 'posts'  # 컨텍스트 변수를 object_list 대신 posts 사용 (object_list 사용 가능)
    paginate_by = 3


# DetailView
class PostDV(DetailView):
    model = Post
    # default : template_name = 'blog/post_detail.html'


# ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'  # 날짜 필드(modify_date) 기준으로 최신 객체를 먼저 출력함
    # default : template_name = 'blog/post_archive.html'


class PostYAV(YearArchiveView):
    model = Post
    # 날짜 필드(modify_date)의 연도를 기준으로 객체의 리스트를 가져와, 속한 월을 리스트로 출력한다.
    date_field = 'modify_date'
    make_object_list = True
    # default : template_name = 'blog/post_archive_year.html'


class PostMAV(MonthArchiveView):
    MonthArchiveView.month = 'mar'
    model = Post
    # 날짜 필드(modify_date)의 연월을 기준으로 객체의 리스트를 가져와 리스트로 출력한다.
    date_field = 'modify_date'
    # default : template_name = 'blog/post_archive_month.html'


class PostDAV(DayArchiveView):
    DayArchiveView.month = 'mar'
    model = Post
    # 날짜 필드(modify_date)의 연월일을 기준으로 객체의 리스트를 가져와 리스트로 출력한다.
    date_field = 'modify_date'
    # default : template_name = 'blog/post_archive_day.html'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'  # 날짜 필드(modify_date) 기준 오늘인 객체의 리스트를 출력한다.
    # default : template_name = 'blog/post_archive_day.html'
