from django import forms
from .models import Comment, Board

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','message')

        # fields = '__all__'
class BoardForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

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