import datetime
import urllib.parse
from django.http import HttpResponse
from icalendar import Calendar, Event


def ical_view(request, name, date):
    """
    Route that returns an ical file for a specific event.
    :return: ical file as part of HttpResponse with only the details of a specific event
    """
    event_date = datetime.datetime.strptime(date, '%Y%m%d')
    name = urllib.parse.unquote_plus(name)

    cal = Calendar()
    cal.add('prodid', '-//Calendar Event event//mxm.dk//')
    cal.add('version', '2.0')
    event = Event()
    event.add('summary', name)
    event.add('dtstart', event_date)
    cal.add_component(event)
    return HttpResponse(cal.to_ical(), content_type="text/calendar")
