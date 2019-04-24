from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), kwargs={'pk': 1}, name='index'),
]
