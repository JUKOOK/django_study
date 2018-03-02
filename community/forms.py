# community/forms
# html에서 form, input... 등등의 절차를 생략한다.
# forms를 통해 models의 녀석들을 html에서 간편하게 form input을 받을 수 있게 한다.

from django.forms import ModelForm
from .models import Article

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email']

        # 여기까지 하면 models의 DB를 user가 input으로 작성할 form이 완성된 상태(틀같은 느낌)
