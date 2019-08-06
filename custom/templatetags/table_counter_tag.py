from django import template

register = template.Library()


@register.filter
def table_counter_tag(d, key):
    return d[key]
