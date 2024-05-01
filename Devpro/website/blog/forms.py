from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.forms.fields import Field
from django.forms import Field,ModelForm
from django.db import models
from blog.models import *
from .models import *

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields={
            'first_name',
            'last_name',
            'username',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=[ 'content','name','email',]
    
class Crew_Form(ModelForm):
    class Meta:
        model = crew
        fields='__all__'

class Blog_Form(ModelForm):
    class Meta:
        model = Blogpost
        fields='__all__'

