from django import template

register = template.Library()


@register.filter
def get_type(obj):
    return obj.__class__.__name__
