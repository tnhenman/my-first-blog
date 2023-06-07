from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
        labels ={'title':'名前','text':'内容'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('author','text',)