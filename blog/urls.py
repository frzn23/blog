from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment', views.postComment, name='Post Comment'),
    path('', views.home, name='BlogHome'),
    path('<str:slug>', views.blogpost, name='BlogPost'),
]
