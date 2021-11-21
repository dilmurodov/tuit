from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request, 'tuit/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__day=day, publish__month=month, status='published')
#   agar yuqoridagi shartga tug'ri keladigan statya topilsa post
#   bulmasa HTTP 404 (obyekt ne naydyon)
    return render(request, 'tuit/post/detail.html', {'post': post})
