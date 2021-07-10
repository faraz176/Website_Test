from django.shortcuts import render, get_object_or_404
from .models import blog


def all_blogs(request):
    blog1 = blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blog1':blog1})

def detail(request, blog_id):
    blogs = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/details.html',{'blogs':blogs})
