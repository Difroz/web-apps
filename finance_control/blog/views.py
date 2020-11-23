from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    list_objects = Post.objects.filter(status='published')
    return render(request, 'blog/post/list.html', {'posts': list_objects})

def post_detail(request, year, month, day, post):
    object = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, 'blog/post/detail.html', {'post': object})


