from django.shortcuts import render
from app_base.models import Course


def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)


def course_detail(request, id):
    ctx = {}
    ctx['course'] = Course.objects.get(id=id)
    ctx['courses'] = Course.objects.all().exclude(id=id)
    return render(request, 'course-detail.html', ctx)