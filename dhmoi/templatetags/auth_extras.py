from django import template
from django.contrib.auth.models import Group 

register = template.Library()

@register.filter(name='has_group')
def has_group(user, manager): 
    return user.groups.filter(name=manager).exists() 