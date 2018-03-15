# bookmark/views
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

# 사이트 내부에서 레코드 생성, 수정, 삭제를 위한 제네릭 views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django_study.views import LoginRequiredMixin


# views.generic 기반한 class-based view 정의
# 클래스형 제네릭 뷰 : 장고가 잡아주는 2가지 속성 // 1. 컨텍스트 변수로 object_list를 정의했음
#                                              // 2. 연결되는 템플릿 파일은 <모델명소문자>_list.html로 정해짐
# ListView : bookmark_list.html에 자동 연결
class BookmarkLV(ListView):
    model = Bookmark


# 클래스형 제네릭 뷰 : 장고가 잡아주는 2가지 속성 // 1. 컨텍스트 변수로 object를 정의했음
#                                              // 2. 연결되는 템플릿 파일은 <모델명소문자>_detail.html로 정해짐
# DetailView : bookmark_detail.html에 자동 연결
class BookmarkDV(DetailView):
    model = Bookmark


# 사이트 내에 북마크 레코드에 대해 create, update, delete 기능을 집어넣기 위한 class-based view
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    # template_name = : default 로 <모델명소문자>_form.html

    def form_valid(self, form):
        form.instance.owner = self.request.user  # 폼의 owner 필드에 현재 로그인된 사용자의 User객체를 할당한다.
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkChangeListView(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    # template_name = : default 없음 따로 지정해야 함.

    def get_queryset(self):  # 북마크 레코드 중 지금 로그인한 사용자가 만든 객체들만 리스트해서 보여준다.
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')
    # template_name = : default 로 <모델명소문자>_form.html


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
    # template_name = : default 로 <모델명소문자>_confirm_delete.html
