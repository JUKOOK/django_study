# blog/admin.py
from django.contrib import admin
from .models import Post


# Register your models here.
# admin.site.register(Post) 요거를 커스텀 할 경우

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tags', 'created_at', 'updated_at']