from django.urls import path
from . import views

# for images
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='main_page'),
    path('about', views.about, name='about'),
    path('photos', views.photos, name='photos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
