from django import template

register = template.Library()


@register.filter
def table_column_counter(table_data):
    return str(len(table_data))
