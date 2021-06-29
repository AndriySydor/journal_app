from django.contrib import admin
from .models import Article
from .models import ImagePost

admin.site.register(Article)
admin.site.register(ImagePost)
