from django import forms
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)



post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')


# post_delete = DeleteView.as_view(model=Post, success_url='/blog/')
post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))




'''
커스텀으로 CreateView 방식으로 구현

#blog/forms.py 에 만들어줘야함
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/' 지정하지않으면 model_instance.get_absolute_url()획득시도
    success_url=reverse_lazy('blog:post_list')
    
post_new = PostCreateView.as_view()

get_absolute_url 은 URL Reverse 를 수행하는 함수에 의해서 호출됩니다.

1. django.shortcuts.resolve_url 함수를 쓸 때
2. django.views.generic.CreateView, django.views.generic.UpdateView 등의 CBV를 쓸 때, success_url 로서 사용됩니다.
'''