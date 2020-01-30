from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('teacher/', views.teacher),
    path('course/<int:course_id>', views.course),
    path('qrcode/', views.qrcode),
]
