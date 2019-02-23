from django.contrib import admin
from django.urls import path, include
from blogs import views

app_name='blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:blog_id>', views.detail, name='detail'),
    # path('create', views.createblog, name='create'),
    path('<int:blog_id>/publish', views.publish, name='publish'), #change path to public/<int:blog_id>
    path('delete/<int:blog_id>', views.deleteBlog, name='delete'),
    path('edit/<int:blog_id>', views.editBlog, name='edit'),
    path('createblog', views.createblog, name='createblog')
]