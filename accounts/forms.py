from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): #UserCreationForm에 기존 Meta를 새로 정의 했기때문에, 상속으로 받아주고, 원하는 값 fields 만 재정의하겠다.
        # fields = ('username', 'email')
        fields = UserCreationForm.Meta.fields + ('email',)
        #UserCreationForm이 User모델에 대한 필드이며 User모델은 email필드를 가져있기때문에 호출가능

        