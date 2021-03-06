# Generated by Django 3.2.4 on 2021-06-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=200, upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
