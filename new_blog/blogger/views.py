from django.shortcuts import render
from .models import Blog
def index(request):
    blogs = Blog.objects.all()
    print(blogs)

    return render(request,'index.html',{'blogs':blogs})

def post(request, pk):
    post = Blog.objects.get(id=pk)
    return render(request, 'posts.html',{'posts':post})

def about(request):
    return render(request,'about.html')
