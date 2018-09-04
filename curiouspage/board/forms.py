from django import forms
from django.forms import  TextInput
from .models import Board,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.csrf import csrf_exempt

class CommentForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Comment
        fields = ('message',)

#        fields = '__all__'

class BoardForm(forms.ModelForm):
    sj_type =  SUBJECT_TYPE_CHOICE = (('Language', 'Language'),
                                    ('Database', 'Database'),
                                    ('Etc', 'Etc'),)
    subject_type = forms.ChoiceField(choices = sj_type, label="", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = Board
        fields = (
            #'author','password',
                'subject_type',
                'title',
                'content',
                'file',)

class ConfirmPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Board
        fields = ('password',)
 
class SignUpForm (UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'type':'number'})) # 학번
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        # 학번 이름 별명 이메일 비밀번호 비밀번호 확인
        help_texts = {'username': None,'email' : None,'password':None,}
    
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = False
        user.save()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        help_texts = {'username': None,}
        fields = ['username', 'password'] 
