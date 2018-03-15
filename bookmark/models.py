# bookmark/models
from django.db import models
from django.contrib.auth.models import User  # User의 포스트의 소유자를 고려, 확인하기 위함 / ForeignKey로써!


# Create your models here.
class Bookmark(models.Model):
    # title : 공백 값을 가질 수 있고, null 값을 가질 수도 있다.
    title = models.CharField(max_length=30, blank=True, null=True)
    # url : verboser_name(별칭) 은 'url' 이고, 유일한 값을 가진다.
    url = models.URLField('url', unique=True)
    owner = models.ForeignKey(User, null=True)  # 1:N 관계이므로 User 외래키로...

    # 클래스 객체를 문자열로 표현, 테이블의 객체 각각을 표현할 수 있다.
    def __str__(self):
        return self.title
