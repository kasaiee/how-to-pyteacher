from django.shortcuts import render
from app_accounts.models import RegisteredCourse
from app_social.models import Bookmark
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    ctx = {}
    ctx['registered_course'] = [rc.course for rc in request.user.registeredcourse_set.all()]
    return render(request, 'student-dashboard.html', ctx)


@login_required
def booked_items(request):
    ctx = {}
    booked_items = Bookmark.objects.filter(user=request.user)
    ctx['items'] = [book_item.content_object for book_item in booked_items]
    return render(request, 'booked-items.html', ctx)
