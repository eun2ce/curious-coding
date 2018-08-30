from django import forms
from django.forms import  TextInput
from .models import Board
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# class CommentForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Comment
#         fields = ('author','password','message',)

        # fields = '__all__'
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
    #nick_name = forms.CharField(max_length=30,help_text='necessary.') # 별명

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','date_joined','last_login']
        # 학번 이름 별명 이메일 비밀번호 비밀번호 확인

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password'] 