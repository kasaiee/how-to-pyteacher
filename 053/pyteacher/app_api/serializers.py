from rest_framework import serializers
from app_social.models import Comment
from sorl.thumbnail import get_thumbnail


class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    user_full_name = serializers.SerializerMethodField()

    def get_replies(self, obj):
        return CommentListSerializer(obj.comment_set.filter(approved=True), many=True).data

    def get_avatar(self, obj):
        return get_thumbnail(obj.user.profile.avatar, '55x55', crop='center', quality=99).url

    def get_user_full_name(self, obj):
        return obj.user.get_full_name() if obj.user.get_full_name() else obj.user.username

    class Meta:
        model = Comment
        exclude = ('content_type', 'object_id', 'approved', 'user')
