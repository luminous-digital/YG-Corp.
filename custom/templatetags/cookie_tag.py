from django import template
from custom.models import CookieSnippet

register = template.Library()


# Cookie snippets
@register.inclusion_tag('custom/cookie.html', takes_context=True)
def cookie_elements(context):
    return {
        'cookie_elements': CookieSnippet.objects.all(),
        'request': context['request'],
    }
