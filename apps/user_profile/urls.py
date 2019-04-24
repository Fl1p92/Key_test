from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('edit/', views.EditProfileView.as_view(), name='edit'),
]
