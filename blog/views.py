from django.shortcuts import render


def show_blog(request):
    return render(request, 'blog/blog.html')
