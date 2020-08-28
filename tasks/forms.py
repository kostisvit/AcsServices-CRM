from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import ModelChoiceField
from django.contrib.auth.models import User



class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return '{last_name} {first_name}'.format(last_name=obj.last_name, first_name=obj.first_name)


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task....'}))
    employee = UserModelChoiceField(queryset=User.objects.order_by('last_name').filter(is_active=True), label='Υπάλληλος ACS')

    class Meta:
        model = Task
        fields = '__all__'
        