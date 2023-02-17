from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, group_name):
    template = 'posts/group_list.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template, context)