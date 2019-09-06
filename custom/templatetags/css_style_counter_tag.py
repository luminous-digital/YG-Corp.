from django import template

register = template.Library()


@register.filter
def css_style_counter(number):
    return number % 4 == 0 or (number - 1) % 4 == 0
