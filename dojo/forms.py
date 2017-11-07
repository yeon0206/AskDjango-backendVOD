#dojo/forms.py
#Models Fields와 유사
#Models Fields: Database Field 들을 파이썬 클래스화
#Form Fields: HTML Form Field 들을 파이썬 클래스화

from django import forms
from .models import Post

# Form VS ModelForm

''' ModelForm을 쓰면  Model에다가 정의한다. 그러면 admin에서도 입력시 정의됨
def min_length_3_validator(value): #title이 value로 담긴다.
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요.')
'''
'''
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields='__all__'
        fields=['title','content']
    
    ''' # 모델폼내부에 구현되어있음
    def save(self, commit=True):
        self.instance = Post(**self.cleaned_data)
            if commit:
                self.instance.save()
            return self.instance
    '''