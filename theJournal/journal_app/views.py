from django.shortcuts import render
from .models import Article


def index(request):
    posts = Article.objects.order_by('-id')[:]
    return render(request, 'journal_app/index.html', {'posts': posts})


def about(request):
    return render(request, 'journal_app/about.html')
