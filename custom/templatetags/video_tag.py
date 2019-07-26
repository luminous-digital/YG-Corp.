from django import template
import math

register = template.Library()


@register.filter(name='video_tag')
def format_seconds(s):
    s = 0 if not s else s
    mins = math.floor(s / 60)
    secs = math.floor(s - (mins * 60))
    return "%d:%02d" % (mins, secs)
