# photo/fields : 커스텀 필드 ThumbnailImageField 정의를 위함
from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image  # 이미지 처리 라이브러리 PIL 임포트
import os


# 아래 호출되기 전 미리 정의 : 기존 이미지 파일 기준으로 썸네일 파일 이름을 생성한다.
def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


# 커스텀 필드를 위한 File 처리 클래스
class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):  # 썸네일 파일 경로
        return _add_thumb(self.path)

    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):  # 썸네일 파일 url
        return _add_thumb(self.url)

    thumb_url = property(_get_thumb_url)

    # 원본 이미지 저장 + 원본 파일에서부터 128x128짜리 썸네일을 만들어 저장한다.
    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)

        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)))
        background.save(self.thumb_path, 'PNG')

    # 본래의 삭제 기능(super)에서 원본 뿐 아니라 썸네일도 삭제시키는 기능을 추가한다.
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)


# 실제 쓰이는 장고 모델 필드
class ThumbnailImageField(ImageField):
    # 새로운 커스텀 필드 만들 때 위에 만들었던 File 처리 클래스를 반드시 attr_class로 지정한다.
    attr_class = ThumbnailImageFieldFile

    # 새 생성자 오버라이드
    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        # 부모 크래스 생성자를 호출하여 관련 속성 초기화
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
