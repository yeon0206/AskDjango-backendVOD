from django import forms
from django.views.generic import ListView, CreateView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=100)

#blog/forms.py 에 만들어줘야함
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/'

post_new = PostCreateView.as_view()

'''
get_absolute_url 은 URL Reverse 를 수행하는 함수에 의해서 호출됩니다.

1. django.shortcuts.resolve_url 함수를 쓸 때
2. django.views.generic.CreateView, django.views.generic.UpdateView 등의 CBV를 쓸 때, success_url 로서 사용됩니다.
'''