# blog/models.py
from django.db import models
import re     # Regular Expression
from django.forms import ValidationError
from django.core.urlresolvers import reverse
from tagging.fields import TagField


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*), ([+-]?\d+\.?\d*)$', value):  # +- 있어도 되고 없어도 됨, n.n, n.n 형식
        raise ValidationError('LngLat 타입이 바르지 않습니다.')


# Create your models here.
# DB 만들기 장고 ORM 이용... DB Post와 그 내부 column 정의
class Post(models.Model):
    # STATUS_CHOICES에 대해 미리 정의한다. char 1짜리로 연결된다.
    # admin.py에서 actions 구현을 통해 status field를 Bulk Update 가능케할 수 있다.
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
        ('a', 'Another_ex'),
    )

    # 필수 필드 : null, empty 불가(둘 다 False). 상태 따로 지정하지 않으면 기본적으로 default인 False 적용
    # 그냥 makemigration을 하면 default 값에 대한 질문을 해오므로, default 인자를 설정해주자.
    author = models.CharField('작성자', max_length=20)
    title = models.CharField('제목', max_length=50, help_text='포스팅 제목을 최대 50자 이내로 입력해주세요.')      # 길이 제한 있는 문자열
    # title = models.CharField(max_length=100,
    #     choices= (                                            # ('저장될 값', 'UI에 보여질 레이블')
    #         ('제목 1', '제목 1 레이블'),
    #         ('제목 2', '제목 2 레이블'),
    #         ('제목 3', '제목 3 레이블')
    #     ))
    slug = models.SlugField('Slug', max_length=50, help_text='포스트 제목의 별칭입니다. 한 단어만!', unique=True)
    content = models.TextField('내용', help_text='포스트 내용')   # 길이제안 없는 문자열
    description = models.CharField('한 줄 요약', max_length=100, help_text='포스트 내용 한 줄 설명', blank=True)
    create_date = models.DateTimeField('Create Date', auto_now_add=True)    # 최초 저장이 되는 일시 자동저장
    modify_date = models.DateTimeField('Modify Date', auto_now=True, editable=True)        # 저장될 때마다 일시 자동저장

    # 추가 field :
    tag = TagField()  # tagging을 import함으로써...
    status = models.CharField('상태', max_length=1, choices=STATUS_CHOICES)
    lnglat = models.CharField(max_length=40, blank=True, validators=[lnglat_validator], help_text='경도, 위도 포맷으로 입력 바람')
    # Validator 함수 사용

    class Meta:
        verbose_name = 'post'  # 테이블 단수 별칭
        verbose_name_plural = 'posts'  # 테이블 복수 별칭
        db_table = 'my_post'  # DB에 저장되는 테이블 이름 default는 blog_post <앱 이름>_<model 이름>
        ordering = ('-modify_date',)  # 모델 객체 리스트 출력시 modify_date 기준 내림차순

    def __str__(self):  # 객체의 문자열 표시
        return self.title

    def get_absolute_url(self):  # url 추출 : /blog/(?P<slug>[-\w]+)/ 에서 slug에 현재 객체의 slug 필드 값을 대입
        return reverse('blog:post_detail', args=(self.slug,))

    # get_previous_by_modify_date 라는 장고 내장함수 이용, modify_date 기준으로 이전 post 객체 반환한다.
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # get_next_by_modify_date 라는 장고 내장함수 이용, modify_date 기준으로 다음 post 객체 반환한다.
    def get_next_post(self):
        return self.get_next_by_modify_date()
