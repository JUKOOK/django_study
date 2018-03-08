# blog/forms : search를 위함.
from django import forms  # 폼을 클래스로서 정의할 수 있는 기능 제공


class PostSearchForm(forms.Form):
    # 모델 클래스 정의하듯이 하면 된다. 변수 search_word는 필드로써, id의 역할을 한다.
    search_word = forms.CharField(label='search_word')
