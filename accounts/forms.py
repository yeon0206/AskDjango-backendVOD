from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile
class SignupForm(UserCreationForm): #SignupForm은 User모델에 대한 모델폼, 모델폼은 하나의 모델만 지원, SignupForm->User모델
    phone_number = forms.CharField()
    address = forms.CharField()

    #폰넘버,어드레스는 Profile모델의 필드. 따라서, User모델 인스턴스 생성 시 Profile모델 인스턴스도 같이 생성해줌.
    #SignupForm은 User모델에 대한 폼이기 때문에, 단순히 phone_number 필드만 정의해주면 지원해주지 않고 저장되지 않는다.
    #따라서 따로 저장해줘야함
    class Meta(UserCreationForm.Meta): #UserCreationForm에 기존 Meta를 새로 정의 했기때문에, 상속으로 받아주고, 원하는 값 fields 만 재정의하겠다.
        # fields = ('username', 'email')
        fields = UserCreationForm.Meta.fields + ('email',)
        #UserCreationForm이 User모델에 대한 필드이며 User모델은 email필드를 가져있기때문에 호출가능
    def save(self):
        user = super().save() #SignupForm에 save를 호출했으니 관련모델인 user인스턴스를 리턴

        profile = Profile.objects.create(
            user = user,
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address'],
        )
        return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self): #clean_필드명 통해서 유효성 검사
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('mismatched!')
        return answer