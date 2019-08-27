from django import template

register = template.Library()


@register.filter
def two_column_decor(first_decor, second_decor):
    return True if first_decor == second_decor else False



