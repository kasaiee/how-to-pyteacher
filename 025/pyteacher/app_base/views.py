from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
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
    if course not in [rc.course for rc in request.user.registeredcourse_set.all()]:
        request.user.registeredcourse_set.create(course=course)
        messages.success(
            request, '%s عزیز، خوشحالم که در این دوره شرکت کردی. حالا میتونی این دوره رو از توی پروفایلت با من شروع کنی :)' % request.user.username)
    else:
        messages.success(
            request, '%s عزیز، شما قبلا در این دوره ثبت نام کرده اید!' % request.user.username)
    return HttpResponseRedirect(reverse('app-accounts:profile'))
