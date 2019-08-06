from django import template

register = template.Library()


@register.filter
def value_from_index_tag(d, key):
    return d[key]
