from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)
        labels ={'title':'名前','text':'内容'}