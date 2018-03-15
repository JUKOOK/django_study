# photo/models
from django.db import models
from django.core.urlresolvers import reverse
from .fields import ThumbnailImageField  # 우리가 fields.py 에서 직접 만들 커스텀 필드
# Create your models here.


# 앨범에 대한 모델
class Album(models.Model):
    name = models.CharField('이름', max_length=20)
    description = models.CharField('한 줄 요약', max_length=80, blank=True)

    # model 연결될 테이블의 기본 특성
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))


# 앨범 내부의 사진에 대한 모델
class Photo(models.Model):
    album = models.ForeignKey(Album)  # 여기서 정의된 것이 Album의 pk에 외래키로 연결한다.
    title = models.CharField('제목', max_length=30)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    # 우리가 정의한 커스텀 필드 ThumbnailImageField 형태로 정의
    # photo/%/%m : MEDIA_ROOT로 정의된 디렉토리 하위에 ~/photo/2018/03 처럼 연월을 포함한
    # 디렉토리를 만들고 그 곳에 업로드하는 실제 사진의 원본 및 썸네일 사진을 저장한다는 것이다.

    description = models.TextField('사진 요약', blank=True)
    upload_date = models.DateTimeField('upload_date', auto_now_add=True)

    # model 연결될 테이블의 기본 특성
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))