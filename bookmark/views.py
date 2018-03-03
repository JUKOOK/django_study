# bookmark/views
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark


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


