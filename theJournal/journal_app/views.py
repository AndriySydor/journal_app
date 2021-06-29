from django.shortcuts import render
from .models import Article
from .models import ImagePost


def index(request):
    posts = Article.objects.order_by('-id')[:]
    return render(request, 'journal_app/index.html', {'posts': posts})


def about(request):
    return render(request, 'journal_app/about.html')


def photos(request):
    elements = ImagePost.objects.order_by('-id')[:]
    return render(request, 'journal_app/photos.html', {'elements': elements})
