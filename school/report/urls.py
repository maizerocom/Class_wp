from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard),
    path('search/', views.search),
]
