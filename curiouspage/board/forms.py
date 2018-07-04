from django import forms
from .models import Comment, Board

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','message')

        # fields = '__all__'
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'