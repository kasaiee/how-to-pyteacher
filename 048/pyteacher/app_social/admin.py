from django.contrib import admin
from app_social.models import Like, Bookmark, Comment, CommentLike


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_object',
    )


class BookmarkAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_object',
    )


admin.site.register(Like, LikeAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Comment)
admin.site.register(CommentLike)
