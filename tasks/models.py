from django.db import models


class Task(models.Model):
    employee = models.ForeignKey('auth.User', max_length=100, verbose_name='Υπάλληλος ACS', on_delete=models.CASCADE,)  # delete kai
    title = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.title) 
