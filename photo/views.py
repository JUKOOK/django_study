# photo/views
# from django.shortcuts import render -> 함수형 뷰
# class-based view를 위한 제네릭 뷰 import
from django.views.generic import ListView, DetailView
from .models import Album, Photo  # 보여주는 모델 연결


# default template, model에 대한 context는 자동!!
class AlbumListView(ListView):
    model = Album
    # template_name = 'photo/album_list.html'


class AlbumDetailView(DetailView):
    model = Album
    # template_name = 'photo/album_detail.html'


class PhotoDetailView(DetailView):
    model = Photo
    # template_name = 'photo/photo_detail.html'
