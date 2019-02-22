from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.utils import timezone

from blogs.models import Blog

# TODO: pass user id as function?
@login_required(login_url='/accounts/signup')
def dashboard_home(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # check logged in user is same user as from user_id in the url
    if user == request.user:
        # send user to the dashboard
        if request.user.is_superuser:
            blogs = Blog.objects
            current_user = 'Administrator'
        else:
            blogs = Blog.objects.filter(author=request.user)
            current_user = request.user

        can_pub = True
        return render(request, 'dashboard/index.html', {"current_user": current_user, 
                                                        "blogs": blogs,
                                                        "can_pub": can_pub })
    else:
        return redirect('home')