# blog/admin.py
from django.contrib import admin
from .models import Post


# Register your models here.
# admin.site.register(Post) 요거를 커스텀 할 경우 : 장식자 형태로 해보면

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'title', 'tags', 'created_at', 'updated_at']
    # 포스트 변경에서 action 목록에 함수 이름으로 기능을 추가한다.
    # 함수에 대해 short_description을 지정하면 그 문자열을 함수와 매핑 후 action 목록에 추가한다.
    actions = ['make_published', 'make_draft']

    # status field의 Bulk Update용 : Published로 바꾼다.
    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경하였음'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published 상태로 변경'

    # status field의 Bulk Update용 : Draft로 바꾼다.
    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft 상태로 변경하였음'.format(updated_count))

    make_draft.short_description = '지정 포스팅을 Draft 상태로 변경'