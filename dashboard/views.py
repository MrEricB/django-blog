from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from blogs.models import Blog

@login_required(login_url='/accounts/signup')
def dashboard_home(request):
    if request.user.is_superuser:
        blogs = Blog.objects
        current_user = 'Administrator'
    else:
        blogs = Blog.objects.filter(author=request.user)
        current_user = request.user

    return render(request, 'dashboard/index.html', {"current_user": current_user, "blogs": blogs})