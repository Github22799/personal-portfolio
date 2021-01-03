from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:id>/', views.post, name='post'),
]
