from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        Blog.objects.create(title=title, content=content, author=author)
        return redirect('display')
    return render(request, 'create.html')

def edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.author = request.POST.get('author')
        blog.save()
        return redirect('display')
    return render(request, 'edit.html', {'blog': blog})

def delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('display')
    return render(request, 'delete.html', {'blog': blog})

def display(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 5)  # Show 5 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'display.html', {'page_obj': page_obj})