from django.shortcuts import render


def profile(request):
    return render(request, 'student-dashboard.html')
