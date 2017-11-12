from django import forms
from askdjango.widgets.naver_map_point_widget import NaverMapPointWidget
from .models import Post,Comment

class PostForm(forms.ModelForm):
    # dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width': "100%",'height': 200}))

    class Meta:
        model = Post
        fields='__all__'
        widgets={
            'lnglat': NaverMapPointWidget(attrs={'width': 600,'height': 300}),
        }
        #위젯을 클래스로 지정해도되고 인스턴스로 지정해도됨.


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']