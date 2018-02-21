# blog/models.py
from django.db import models
import re
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+-]?\d+\.?\d*)$', value): # +- 있어도 되고 없어도 됨, n.n, n.n 형식
        raise ValidationError('LngLat 타입이 바르지 않습니다.')


# Create your models here.
# DB 만들기 장고 ORM 이용... DB Post와 그 내부 column 정의
class Post(models.Model):
    # 필수 필드 : null, empty 불가(둘 다 False). 상태 따로 지정하지 않으면 기본적으로 default인 False 적용
    # 그냥 makemigration을 하면 default 값에 대한 질문을 해오므로, default 인자를 설정해주자.
    author = models.CharField(max_length=20, default='anonymous')
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 최대 100자 이내로 입력해주세요.')            # 길이 제한 있는 문자열
    # title = models.CharField(max_length=100,
    #     choices= (                                            # ('저장될 값', 'UI에 보여질 레이블')
    #         ('제목 1', '제목 1 레이블'),
    #         ('제목 2', '제목 2 레이블'),
    #         ('제목 3', '제목 3 레이블')
    #     ))
    content = models.TextField(verbose_name='내용',
                               help_text='Markdown 문법 사용 바람')   # 길이제안 없는 문자열
    tags = models.CharField(max_length=100, blank=True)             # 비워도 괜찮음.
    lnglat = models.CharField(max_length=40, blank=True,
                              validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력 바람')
                              # Validator 함수 사용
    created_at = models.DateTimeField(auto_now_add=True)    # 최초 저장이 되는 일시 자동저장
    updated_at = models.DateTimeField(auto_now=True)        # 저장될 때마다 일시 자동저장
    testfield = models.IntegerField(default=10)
    testtime = models.DateTimeField(default=timezone.now)