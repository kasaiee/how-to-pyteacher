from django import template
from app_social.models import Like, Bookmark

register = template.Library()


@register.filter
def is_liked(obj, user):
    return obj.likes.filter(user=user)


@register.filter
def is_booked(obj, user):
    return obj.bookmarks.filter(user=user)
