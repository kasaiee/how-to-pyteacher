from django.shortcuts import render
from app_base.models import Course


def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)


def course_detail(request, title):
    ctx = {}
    ctx['course'] = Course.objects.get(title=title)
    ctx['courses'] = Course.objects.all().exclude(title=title)
    return render(request, 'course-detail.html', ctx)