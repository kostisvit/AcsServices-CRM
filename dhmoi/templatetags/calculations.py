from django import template


register = template.Library()

@register.filter(name='subtract')
def subtract(adeiatotal, day_left):
    return adeiatotal - day_left