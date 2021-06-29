from django.db import models


class Article(models.Model):
    title = models.CharField('Title', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField('Description')

    def __str__(self):
        return self.title
