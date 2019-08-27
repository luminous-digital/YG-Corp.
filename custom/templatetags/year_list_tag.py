from django import template

from yougov.settings.base import YEARS_BEFORE_ARCHIVE

register = template.Library()


@register.filter
def year_list(years):
    dates = []
    for year in years:
        dates.append(year["date"].year)
    return list(dict.fromkeys(dates))[:YEARS_BEFORE_ARCHIVE]
