from django.shortcuts import render
from app_accounts.models import RegisteredCourse
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    ctx = {}
    ctx['registered_course'] = [rc.course for rc in request.user.registeredcourse_set.all()]
    return render(request, 'student-dashboard.html', ctx)
