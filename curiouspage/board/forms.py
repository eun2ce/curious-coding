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
    password = forms.CharField(widget=forms.PasswordInput)
    sj_type =  SUBJECT_TYPE_CHOICE = (('Language', 'Language'),
                                    ('Database', 'Database'),
                                    ('Etc', 'Etc'),)
    subject_type = forms.ChoiceField(choices = sj_type, label="", initial='', widget=forms.Select(), required=True)
    class Meta:
        model = Board
        fields = ('author',
                'password',
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
    username = forms.CharField(max_length=30,help_text='necessary.')
    nick_name = forms.CharField(max_length=30,help_text='necessary.')
    student_number = forms.CharField(widget=TextInput(attrs={'type':'number'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ['student_number','username','nick_name','email','password1','password2']