from django import forms
from django.contrib.auth.models import User
from blog.models import Comment,Post
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')

class WritePost(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','slug','author','body','publish','status','tags')

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
