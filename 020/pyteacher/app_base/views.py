from django.shortcuts import render
from django.http import HttpResponse
from app_base.models import Course
from django.contrib.auth.decorators import login_required


def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)


def course_detail(request, id):
    ctx = {}
    ctx['course'] = Course.objects.get(id=id)
    ctx['courses'] = Course.objects.all().exclude(id=id)
    return render(request, 'course-detail.html', ctx)


@login_required
def register_course(request, course_id):
    course = Course.objects.get(id=course_id)
    request.user.registeredcourse_set.create(course=course)
    return HttpResponse('OK!')
