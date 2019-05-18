from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.conf import settings
from app_base.models import Course, CourseSession, CourseSessionExercise
from rest_framework import status
from app_social.models import Comment, CommentLike
from app_api.serializers import CommentListSerializer
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q


@api_view(['POST'])
@login_required
def like(request):
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_id and obj_type:
        if obj_type in settings.ALLOWED_SOCIAL_OBJECTS:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            if my_obj.likes.filter(user=request.user):
                my_obj.likes.filter(user=request.user).delete()
                return Response({"message": "%s دیس لایک شد!" % my_obj.title}, status=status.HTTP_200_OK)
            else:
                my_obj.likes.create(user=request.user)
                return Response({"message": "%s لایک شد!" % my_obj.title}, status=status.HTTP_200_OK)
    return Response({"message": "اوه! یه مشکلی پیش اومده..."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@login_required
def bookmark(request):
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_id and obj_type:
        if obj_type in settings.ALLOWED_SOCIAL_OBJECTS:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            if my_obj.bookmarks.filter(user=request.user):
                my_obj.bookmarks.filter(user=request.user).delete()
                return Response({"message": "%s از نشانه گذاری درآمد!" % my_obj.title}, status=status.HTTP_200_OK)
            else:
                my_obj.bookmarks.create(user=request.user)
                return Response({"message": "%s نشانه گذاری شد!" % my_obj.title}, status=status.HTTP_200_OK)
    return Response({"message": "اوه! یه مشکلی پیش اومده..."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def comment(request):
    if not request.user.is_authenticated:
        return Response(
            {"warning": "برای نظر دادن یا باید وارد سایت بشی یا اینکه ثبت نام کنی!"},
            status=status.HTTP_200_OK)
    comment = request.POST.get('value')
    if not comment:
        return Response(
            {"warning": "فکر کنم یادت رفته نظرتو بگی! لطفا فیلد نظر رو با دقت پر کن..."},
            status=status.HTTP_200_OK)
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_id and obj_type:
        if obj_type in settings.ALLOWED_SOCIAL_OBJECTS:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            my_obj.comments.create(user=request.user, value=comment)
            return Response(
                {"message": "ممنون که وقت گذاشتی نظر دادی. نظر شما بعد از تائید نمایش داده میشه!"},
                status=status.HTTP_200_OK)
    return Response({"message": "اوه! یه مشکلی پیش اومده..."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
    obj_id = request.GET.get('id')
    obj_type = request.GET.get('type')
    if obj_id and obj_id.isdigit() and obj_type and obj_type in settings.ALLOWED_SOCIAL_OBJECTS:
        my_model = eval(obj_type)
        try:
            obj = my_model.objects.get(id=obj_id)
        except my_model.DoesNotExist:
            return Response({"message": "این موردی وجود نداره!"}, status=status.HTTP_400_BAD_REQUEST)
        com = Comment.objects.first()
        ct = ContentType.objects.get_for_model(com)
        comments = obj.comments.filter(Q(approved=True) & ~Q(content_type=ct))
        serializer = CommentListSerializer(instance=comments, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "اوه! یه مشکلی پیش اومده..."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def comment_like(request):
    if not request.user.is_authenticated:
        return Response(
            {"warning": "برای نظر دادن یا باید وارد سایت بشی یا اینکه ثبت نام کنی!"},
            status=status.HTTP_200_OK)
    comment_id = request.POST.get('comment_id')
    value = request.POST.get('value')
    if abs(int(value)) != 1:
        return Response(
            {"warning": "اوه! یه مشکلی پیش اومده..."},
            status=status.HTTP_200_OK)
    try:
        com = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response(
            {"warning": "همچین نظری وجود نداره!"},
            status=status.HTTP_200_OK)
    if CommentLike.objects.filter(user=request.user, comment=com):
        return Response(
            {"warning": "تو به این نظر، قبلا امتیاز دادی!"},
            status=status.HTTP_200_OK)
    CommentLike.objects.create(comment=com, user=request.user, value=value)
    return Response(
        {"message": "امتیازت ثبت شد! دستت درد نکنه..."},
        status=status.HTTP_200_OK)
