from datetime import timedelta

from django import template

register = template.Library()


@register.filter
def days_to_add(date):
    return date + timedelta(days=1)
