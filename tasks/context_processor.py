
from .models import *

import datetime


def task_count(request):
    today = datetime.date.today()
    if request.user.is_authenticated:
        context = { 'total_tasks' : Task.objects.filter(complete=False,created__year=today.year, employee=request.user).order_by('-created').count() 
        }
        return context
    else:
        return {}
