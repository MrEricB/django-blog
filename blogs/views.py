from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'blog/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.user != blog.author:
        blog.view_count += 1
        blog.save()
    return render(request, 'blog/detail.html', {'blog':blog})

@login_required(login_url='/accounts/signup')
def publish(request, blog_id):
    # TODO: make sure blog belongs to user or user ins admin
    if blog_id:
        blog = Blog.objects.get(id=blog_id)
        blog.published_date = timezone.now()
        blog.save()
        return redirect('dashboard:dashboard_home', user_id=request.user.id)

@login_required(login_url='/accounts/signup')
def editBlog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        # update the blog
        if request.POST['title']:
            blog.title = request.POST['title']
        if request.POST['text']:
            blog.text = request.POST['text']
        # if request.FILES['image']:
        #     blog.image = request.FILES['image']

        blog.save()
        return redirect('dashboard:dashboard_home', user_id=request.user.id)
    else:
        return render(request, 'dashboard/edit_blog.html', {'blog': blog})

# TODO: move createblog to dashboard?? also pass user id to it?
@login_required(login_url='/accounts/signup')
def createblog(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['text'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            blog = Blog()
            blog.title = request.POST['title']
            blog.text = request.POST['text']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                blog.url = request.POST['url']
            else:
                blog.url = 'http://' + request.POST['url']
            blog.icon = request.FILES['icon']
            blog.image = request.FILES['image']
            # blog.pub_date = timezone.datetime.now()
            blog.author = request.user
            blog.save()
            # return redirect('/' + str(blog.id))
            return redirect('blog:home')
        else:
            return render(request, 'blog/createblog.html',{'error':'All fields are required.'})
    else:
        return render(request, 'blog/createblog.html')


@login_required(login_url='/accounts/signup')
def deleteBlog(request, blog_id):
    # TODO: make sure blog belongs to user or user is an admin
    if request.method == 'POST':
        if blog_id:
            blog = Blog.objects.get(id=blog_id)
            # delete the blog
            blog.delete()
            # redirect back to dashboard
            return redirect('dashboard:dashboard_home', user_id=request.user.id)
    else:
        blog = Blog.objects.get(id=blog_id) 
        return render(request, 'dashboard/delete_blog.html', {"blog": blog})