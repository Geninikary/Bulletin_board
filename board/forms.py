from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User, Group
from .models import Post, Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading',
            'category',
            'text',
            'author',
        ]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['msg_content']


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.object.get(name='user_author')
        basic_group.user_set.add(user)
        return user
