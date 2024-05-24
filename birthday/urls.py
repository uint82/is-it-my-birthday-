from django.urls import path
from . import views

urlpatterns = [
    path('', views.is_birthday, name='is_birthday'),
]
