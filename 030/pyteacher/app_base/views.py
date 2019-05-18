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


def course_detail(request, slug):
    title = slug.replace('-', ' ')
    ctx = {}
    ctx['course'] = course = Course.objects.get(title=title)
    ctx['courses'] = Course.objects.all().exclude(title=title)
    return render(request, 'course-detail.html', ctx)


def course_session_detail(request, course_title, session_title):
    ctx = {}
    course = Course.objects.get(title=course_title)
    ctx['session'] = course.coursesession_set.get(title=session_title)
    return render(request, 'course-session-detail.html', ctx)


def course_session_exercise_detail(request, course_title, session_title, exercise_title):
    ctx = {}
    course = Course.objects.get(title=course_title)
    session = course.coursesession_set.get(title=session_title)
    ctx['exercise'] = session.coursesessionexercise_set.get(title=exercise_title)
    return render(request, 'exercise-detail.html', ctx)


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
