from django import template

register = template.Library()


@register.filter
def get_type(obj):
    return obj.__class__.__name__


@register.filter
def calc_price(item, user):
    return item.price() - sum(
        [ri.session.price for ri in user.registereditem_set.filter(session__course=item)])
