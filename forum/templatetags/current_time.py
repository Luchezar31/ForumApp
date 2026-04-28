from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag(name='current_time')
def get_current_time(format_time='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(format_time)

