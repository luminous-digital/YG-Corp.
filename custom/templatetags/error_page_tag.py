from django import template

from flex.models import ErrorPage

register = template.Library()


@register.simple_tag
def error_page():
    error_object = ErrorPage.objects.all().first()
    return error_object.content if error_object else ' '
