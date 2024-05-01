from django.contrib.auth.forms  import UserChangeForm
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from blog.models import Blogpost,Comment,Img,crew
from blog.forms import *
from django.contrib.auth import logout
from blog.urls import *
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings

def Home(request): 
    blogposts=Blogpost.objects.all()
    context={

        "blogposts":blogposts
    }
    return render(request,'home.html',context)


def Postdetails(request,slug):
    postdetail=get_object_or_404(Blogpost,slug=slug)
    comment =postdetail.comments.all()
    if request.method=="POST":
        print(request.POST)
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            com = Comment.objects.create(post=postdetail,name=request.POST['name'],content=request.POST['content'],email=request.POST['email'])
            com.save()
    else:
        commentform=CommentForm()
    context={
        "postdetail":postdetail,
        "comment":comment,
        "commentform":commentform
    }
    return render(request,'postdetails.html',context)

def signup(request):
    if request.method =="POST":
       form=UserCreationForm(request.POST)
       if form.is_valid:
           form.save()
    else:
        form = UserCreationForm()
    context={
          "form":form
    }
    return render(request,'signup.html',context)

def profile(request):
    context={
        'blogpost':Blog_Form()
    }
    if request.method == "POST":
        blogpost = Blog_Form(request.POST)
        if blogpost.is_valid():
            blogpost.save()
    return render(request,'profile.html',context)

def logout_view(request):
    logout(request)

def contact(request):
    return render(request,'contact.html')


def helloworld(request):
    return render(request,'helloworld.html')

def check(request):
    context={
        'form':Crew_Form()
    }
    if request.method == "POST":
        form = Crew_Form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'check.html',context)

def checkall(request):
    context={
    "all_check" : crew.objects.all()
    }
    return render(request,'checkall.html',context)


