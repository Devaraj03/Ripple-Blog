from django.urls import path
from blog.views import *
from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',Home,name='home'),
    path('signup',signup,name="signup"),
    path('login',auth_views.LoginView.as_view(),name="login"),
    path('logout',auth_views.LogoutView.as_view(),name="logout"),
    path('profile',profile,name="profile"),
    path('check',check,name="check"),
    path('checkall',checkall,name="checkall"),
    path('contact',contact,name="contact"),
    path('helloworld',helloworld,name="helloworld"),
    path("<slug:slug>",Postdetails,name="postdetails"),
    ]
urlpatterns == static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 