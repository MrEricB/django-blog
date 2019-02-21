from django.contrib import admin
from django.urls import path, include
from blogs import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_id>', views.detail, name='detail'),
    path('create', views.createblog, name='create'),
]