from django import template

register = template.Library()

@register.filter
def my_filter_person(data):
    return data + ' -- Filter perosnalizado'