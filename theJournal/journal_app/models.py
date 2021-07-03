from django.db import models


class Article(models.Model):
    title = models.CharField('Title', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField('Description')

    def __str__(self):
        return self.title


class ImagePost(models.Model):
    image = models.ImageField(default='img/default.png', upload_to='img', blank=True, null=True)
    title = models.CharField('Title', max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
