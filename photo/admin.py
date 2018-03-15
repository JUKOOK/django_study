# photo/admin
from django.contrib import admin
from .models import Album, Photo


# Register your models here.
# 외래키로 연결된 Album과 Photo가 1:N 관계 형성하므로, 각 앨범 별로 사진들도 함께 보여줄 수 있다.
# 보여주는 형식은 StackedInline(스택모양 열)과 TabularInline(테이블모양 행)
class PhotoInline(admin.StackedInline):
    model = Photo  # 추가로 보여주는 테이블(외래키를 가진 N측)
    extra = 5  # 추가할 때 몇 개 객체 저장공간을 열어줄 것인가


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]  # 앨범 객체 표시할 때 인라인으로 표시하는 사항
    list_display = ('name', 'description')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'album')


admin.site.register(Album, AlbumAdmin)  # Album와 AlbumAdmin을 admin 페이지에 등록한다.
admin.site.register(Photo, PhotoAdmin)  # Photo와 PhotoAdmin을 admin 페이지에 등록한다.