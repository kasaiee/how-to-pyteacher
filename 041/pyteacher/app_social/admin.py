from django.contrib import admin
from app_social.models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content_object',
    )


admin.site.register(Like, LikeAdmin)
