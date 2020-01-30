from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('student/all/', views.all_student),
    path('student/add/', views.add_student),
    path('student/edit/<int:std_id>/', views.edit_student),
    path('course/all', views.all_course),
    path('course/add', views.add_course),
    path('course/edit/<int:course_id>/', views.edit_course),
]
