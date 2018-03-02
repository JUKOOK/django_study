# community/views
from django.shortcuts import render
from .forms import Form
from .models import Article


# Create your views here.
def write(request):
    # forms.py에서 만든 models 정보를 받는 form을 여기 html에 사용할 수 있게 된다.
    # button submit 후 이것이 POST method이고, 올바르다면 models의 정보구조에 맞게 data로써 저장한다.
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    # 연결 html 내에 form 이라는 template tag를 정의하고 연결한다.
    return render(request, 'community/write.html', {'form': form})


def list(request):
    # form으로 받은 user data를 리스트로 표시해준다.
    articleList = Article.objects.all()

    # 연결 html 내에 articleList 이라는 template tag를 정의하고 연결한다.
    return render(request, 'community/list.html', {'articleList':articleList})


def goToview(request, num="1"):
    # list.html 에서 각 POST를 상세보기 들어가서 볼 수 있게 한다.
    # Article object 내의 POST들에 대해 id로 하나만 Get한다.
    article = Article.objects.get(id=num)

    # 연결 html 내에 article 이라는 template tag를 정의하고 연결한다.
    return render(request, 'community/view.html', {'article':article})