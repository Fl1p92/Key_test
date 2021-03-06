from django.urls import path

from . import views


urlpatterns = [
    path('logs/', views.LogView.as_view(), name='logs'),
    path('requests/', views.RequestView.as_view(), name='requests'),
]
