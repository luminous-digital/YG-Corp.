from django import template

register = template.Library()


@register.filter
def value_from_index(d, key):
    return d[key]
