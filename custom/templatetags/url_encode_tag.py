from django import template
import urllib.parse

register = template.Library()


@register.filter
def url_encode(text):
    return urllib.parse.quote_plus(text)
