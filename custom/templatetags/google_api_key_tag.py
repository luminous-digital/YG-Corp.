from django import template

from yougov.settings.base import GOOGLE_API_KEY

register = template.Library()


@register.simple_tag
def google_api_key():
    return GOOGLE_API_KEY
