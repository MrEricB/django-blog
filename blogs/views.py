from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'blog/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})

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
            return redirect('home')
        else:
            return render(request, 'blog/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'blog/create.html')