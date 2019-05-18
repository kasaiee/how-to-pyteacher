from rest_framework import serializers
from app_social.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    user_full_name = serializers.SerializerMethodField()

    def get_replies(self, obj):
        return CommentListSerializer(obj.comment_set.filter(approved=True), many=True).data

    def get_avatar(self, obj):
        return obj.user.profile.avatar.url

    def get_user_full_name(self, obj):
        return obj.user.get_full_name() if obj.user.get_full_name() else obj.user.username

    class Meta:
        model = Comment
        exclude = ('content_type', 'object_id', 'approved', 'user')
