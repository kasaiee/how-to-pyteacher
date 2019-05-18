from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
import os
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from app_chat.models import Chat
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from app_base.models import Course, CourseSession
from django.contrib.auth.decorators import login_required


def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)


def course_detail(request, slug):
    ctx = {}
    ctx['course'] = course = Course.objects.get(slug=slug)
    ctx['courses'] = Course.objects.all().exclude(slug=slug)
    return render(request, 'course-detail.html', ctx)


def course_session_detail(request, course_slug, session_slug):
    ctx = {}
    course = Course.objects.get(slug=course_slug)
    ctx['session'] = course.coursesession_set.get(slug=session_slug)
    return render(request, 'course-session-detail.html', ctx)


def course_session_exercise_detail(request, course_slug, session_slug, exercise_slug):
    ctx = {}
    course = Course.objects.get(slug=course_slug)
    session = course.coursesession_set.get(slug=session_slug)
    ctx['exercise'] = session.coursesessionexercise_set.get(slug=exercise_slug)
    return render(request, 'exercise-detail.html', ctx)


@login_required
def register_course(request, item_id, item_type):
    if item_type not in ['Course', 'CourseSession']:
        messages.error(request, 'اون! یه مشکلی پیش اومده...')
        return HttpResponseRedirect('/')
    model = eval(item_type)
    item = model.objects.get(id=item_id)
    if item_type == 'Course' and item not in [rc.course for rc in request.user.registereditem_set.all()]:
        request.user.registereditem_set.create(course=item)
        messages.success(
            request, '%s عزیز، خوشحالم که در این دوره شرکت کردی. حالا میتونی این دوره رو از توی پروفایلت با من شروع کنی :)' % request.user.username)
    elif item_type == 'CourseSession' and item not in [rs.session for rs in request.user.registereditem_set.all()]:
        request.user.registereditem_set.create(session=item)
        messages.success(
            request, '%s عزیز، خوشحالم که در این قسمت رو گرفتی. حالا میتونی این قسمت رو از توی پروفایلت با من ادامه بدی کنی :)' % request.user.username)
    else:
        messages.success(
            request, '%s عزیز، شما قبلا در این دوره ثبت نام کرده اید!' % request.user.username)
    return HttpResponseRedirect(reverse('app-accounts:registered-items'))


@login_required
def change_seen_status(request):
    msg_id = request.GET.get('msg_id')
    if msg_id:
        try:
            msg_id = int(msg_id)
            msg = Chat.objects.filter(id=msg_id)
            if msg:
                msg_owner_groups = [gp.name for gp in msg[0].user.groups.all()]
                requested_user_groups = [gp.name for gp in request.user.groups.all()]
                if ('students' in msg_owner_groups and 'operators' in requested_user_groups) or \
                        ('operators' in msg_owner_groups and 'students' in requested_user_groups):
                    msg = msg[0]
                    msg.seen = True
                    msg.save()
        except ValueError:
            return HttpResponseBadRequest()
    response_data = {}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


MERCHANT = os.environ['zarincode']
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional


def payment(request, course_id):
    """ price per toman """
    CallbackURL = 'http://127.0.0.1:8000' + reverse('app-base:verify', args=(course_id, ))  # Important: need to edit for realy server.
    course = Course.objects.get(id=course_id)
    result = client.service.PaymentRequest(MERCHANT, course.price, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], course.price)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')
