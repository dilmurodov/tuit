from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts_published = Post.published.all()
    pages_list = Paginator(object_list=posts_published, per_page=3)
    page = request.GET.get('page')
    try:
        posts = pages_list.page(page)
    except PageNotAnInteger:
        posts = pages_list.page(1)
    except EmptyPage:
        posts = pages_list.page(pages_list.num_pages)

    return render(request, 'tuit/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, publish__year=year,
                             publish__day=day, publish__month=month, status='published')
#   agar yuqoridagi shartga tug'ri keladigan statya topilsa post
#   bulmasa HTTP 404 (obyekt ne naydyon)
    return render(request, 'tuit/post/detail.html', {'post': post})
