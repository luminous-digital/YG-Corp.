from django import template

register = template.Library()


@register.filter
def css_style_counter(number):
    if number % 4 == 0 or (number - 1) % 4 == 0:
        return '--alt'
    return
