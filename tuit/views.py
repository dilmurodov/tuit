from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import PochtaForma
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


def pochtaga_junatish(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        forma = PochtaForma(request.POST)
        if forma.is_valid():
            form_data = forma.cleaned_data
            post_url = request.build_absolute_uri(post.statya_urli())
            title = f"{ form_data['name']} ({form_data['email']}) recommends you reading " \
                    f"{post.title}"
            body = f"Read '{post.title}' at\n\n\n {post_url} \n\n {form_data['name']}\'s comments: " \
                   f"{form_data['comments']}"
            send_mail(title, body,  form_data['email'], [form_data['to']])
            sent = True
            return render(request, 'tuit/post/share.html', {'post': post, 'form': forma, 'sent':sent})
    else:
        forma = PochtaForma()
        return render(request, 'tuit/post/share.html', {'post': post, 'form': forma, 'sent':sent})
