from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from app_base.models import Course, CourseSession, CourseSessionExercise


@login_required
@api_view(['POST'])
def like(request):
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_id and obj_type:
        if obj_type in ['Course', 'CourseSession', 'CourseSessionExercise']:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            import ipdb; ipdb.set_trace()
            my_obj.likes.create(user=request.user)
    return Response({"message": "Hello, world!"})
