from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def current_time(format_str):
    return datetime.now().strftime(format_str)


@register.simple_tag
def simple_message_footer():
    return 'testando tags no footer'