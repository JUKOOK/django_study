# blog/views
from django.views.generic import ListView, DetailView, TemplateView
# \ 이용하면 두 줄로 쓸 수 있다.
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, \
    DayArchiveView, TodayArchiveView
from tagging.models import Tag, TaggedItem  # Tag 클라우드와 태그된 포스트 객체들
from tagging.views import TaggedObjectList  # Tag

# search 기능을 넣기 위한 import
from django.views.generic import FormView
from .forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render  # <-- 함수형 view일 경우 사용

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
    context_object_name = 'posts'  # 컨텍스트 변수를 object_list 외에도 posts 사용 (object_list 사용 가능)
    paginate_by = 6


# DetailView
class PostDV(DetailView):
    model = Post
    # default : template_name = 'blog/post_detail.html'
    # tagging -> 컨텍스트 변수 tags_for_object 사용 가능(object 객체에 달려있느 태그들의 리스트)


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


class TagTC(TemplateView):  # 태그 클라우드는 태그 아이템들에 대해 화면에 보여주기만 하므로
    template_name = 'tagging/tagging_cloud.html'


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


# search를 위한 FormView 제네릭 뷰 상속한 class-based view
# FormView : GET 요청인 경우 폼을 화면에 띄우고 사용자의 입력을 기다리며, 제출된 데이터는 POST 요청으로
# 접수되어 유효성 검사를 한다.(form_valid) 유효한 post가 있으면 render한다.
class SearchFormView(FormView):
    form_class = PostSearchForm  # 연동 폼 지정
    template_name = 'blog/post_search.html'  # 띄울 템플릿 이름

    # 사용자 입력 데이터의 유효성 검사 들어온 포스트의 search_word(id)를 searchWord에
    # 저장하고, Q로 검색하여 해당되는 포스트 레코드를 post_list에 담아낸다.
    def form_valid(self, form):
        searchWord = '%s' % self.request.POST['search_word']
        # <field>__icontains : 해당 field에 대소문자 구별 없이 단어 포함 여부
        # distinct() : 중복 제외
        post_list = Post.objects.filter(Q(title__icontains=searchWord) |
                                        Q(description__icontains=searchWord) |
                                        Q(content__icontains=searchWord) |
                                        Q(tag__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form  # PostSearchForm 자체를 지정
        context['search_form'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)  # No redirection
