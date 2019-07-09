from django import template
from custom.models import MenuSnippet

register = template.Library()


# Menu snippets
@register.inclusion_tag('custom/menu.html', takes_context=True)
def menu_elements(context):
    return {
        'menu_elements': MenuSnippet.objects.all(),
        'request': context['request'],
    }
