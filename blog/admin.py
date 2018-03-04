# blog/admin.py
from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'title', 'slug', 'tags', 'description', 'create_date', 'modify_date')
    list_filter = ('modify_date',)  # modify_date를 필터로 하는 사이드바를 보여준다.
    search_fields = ('title', 'content',)  # 검색박스를 띄우고 검색 쿼리는 title, content 에거 검색하게 한다.
    prepopulated_fields = {'slug': ('title',)}  # slug 필드는 title 필드를 이용해 미리 채워진다.(소문자, 숫자, -_ 자동 복사)

    # 포스트 변경에서 action 목록에 함수 이름으로 기능을 추가한다.
    # 함수에 대해 short_description을 지정하면 그 문자열을 함수와 매핑 후 action 목록에 추가한다.
    actions = ['make_published', 'make_draft', 'make_withdrawn']

    # status 필드의 Bulk Update용 : Published로 바꾼다.
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경하였음'.format(updated_count))

    make_published.short_description = '지정 포스팅을 Published 상태로 변경'

    # status 필드의 Bulk Update용 : Draft로 바꾼다.
    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경하였음'.format(updated_count))

    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경'

    # status 필드의 Bulk Update용 : Withdrawn로 바꾼다.
    def make_withdrawn(self, request, queryset):
        updated_count = queryset.update(status='w')
        self.message_user(request, '{}건의 포스팅을 Withdrawn 상태로 변경하였음'.format(updated_count))

    make_withdrawn.short_description = '지정 포스팅을 Withdrawn 상태로 변경'


admin.site.register(Post, PostAdmin)  # Post와 PostAdmin을 admin 페이지에 등로한다.