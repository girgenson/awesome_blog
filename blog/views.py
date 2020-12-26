from django.shortcuts import render, get_object_or_404
from . models import Post


def show_blog(request):
    all_posts = Post.objects
    return render(request, 'blog/blog.html', {'all_them_posts': all_posts})

def specific_post(request, post_id):
    specific_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/specific_post.html',
                  {'post': specific_post})

