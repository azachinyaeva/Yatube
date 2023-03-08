from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group
from django.core.paginator import Paginator


# Главная страница
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('group').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related('group').filter(group=group).order_by('-pub_date')[:10]
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)

