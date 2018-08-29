from django import forms
from .models import Board
from django.contrib.auth.models import User
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

class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']