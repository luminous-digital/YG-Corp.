from django import template

from custom.models import CookieSnippet

register = template.Library()


@register.simple_tag
def cookie_ga_id():
    return CookieSnippet.objects.all()[0].ga_id if CookieSnippet.objects.all()[0].ga_id else ""
