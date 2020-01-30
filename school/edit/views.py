from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Manage index')

def all_student(request):
    return HttpResponse("หน้าจอรายการนักเรียนทั้งหมด")

def add_student(request):
    return HttpResponse("หน้าจอเพิ่มนักเรียน")

def edit_student(request, std_id):
    return HttpResponse("หน้าจอแก้ไขข้อมูลนักเรียน - %d"%(std_id))

def all_course(request):
    return HttpResponse("หน้าจอรายการวิชาเรียนทั้งหมด")

def add_course(request):
    return HttpResponse("หน้าจอเพิ่มวิชาเรียน")

def edit_course(request, course_id):
    return HttpResponse("หน้าจอแก้ไขข้อมูลวิชาเรียน - %d"%(course_id))