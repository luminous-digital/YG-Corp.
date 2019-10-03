from django import template

from yougov.settings.base import YEARS_BEFORE_ARCHIVE

register = template.Library()


@register.filter
def year_list(years):
    dates = []
    for year in years:
        dates.append(year["date"].year)
    dates = list(dict.fromkeys(dates))
    if len(dates) <= 1:
        return
    if len(dates) > YEARS_BEFORE_ARCHIVE:
        dates = dates[:YEARS_BEFORE_ARCHIVE]
        dates.append('Archive')
    dates.insert(0, 'All')
    return dates
