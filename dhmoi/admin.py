# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Dhmos, Employee, Service, Ergasies, Aithmata, Adeia, Hardware, Polisi, Profile, Training
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from import_export import fields,resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget,CharWidget



class DhmosinfoResource(resources.ModelResource):
	
	class Meta:
		model = Dhmos

def make_visible(modeladmin,request,queryset):
	queryset.update(is_visible=True)
make_visible.short_description = "Ενεργοποίηση πελάτη"

def make_unvisible(modeladmin,request,queryset):
	queryset.update(is_visible=False)
make_unvisible.short_description = "Απενεργοποίηση πελάτη"

class DhmosAdmin(ImportExportModelAdmin):
	resource_class = DhmosinfoResource
	list_display = ('name', 'phone','address','city', 'teamviewer', 'fax', 'email','is_visible')
	list_filter = ['name',]
	search_fields = ['name',]
	actions = [make_visible,make_unvisible]
	

class EmployeeResource(resources.ModelResource):

	class Meta:
		model = Employee

def make_visible(modeladmin,request,queryset):
	queryset.update(is_visible=True)
make_visible.short_description = "Ενεργοποίηση υπαλλήλου"

def make_unvisible(modeladmin,request,queryset):
	queryset.update(is_visible=False)
make_unvisible.short_description = "Απενεργοποίηση υπαλλήλου"


class EmployeeAdmin(ImportExportModelAdmin):
	list_display = ('dhmos','lastname', 'firstname', 'phone', 'email','is_visible')
	search_fields = ['lastname']
	actions = [make_visible,make_unvisible]
	

class ErgasiesResource(resources.ModelResource):
	dhmos = fields.Field(column_name='Δήμος',attribute='dhmos',widget=ForeignKeyWidget(Dhmos, 'name'))
	employee = fields.Field(column_name='Υπάλληλος', attribute='employee', widget=ForeignKeyWidget(User, 'last_name')) 
	jobtype = fields.Field(column_name='Τύπος', attribute='jobtype')
	importdate = fields.Field(column_name='Ημ. Καταχ.', attribute='importdate')
	app = fields.Field(column_name='Εφαμογή', attribute='app')
	info = fields.Field(column_name='Εργασία', attribute='info')
	name = fields.Field(column_name='Υπάλληλος Δήμου', attribute='name')
	time = fields.Field(column_name='Χρόνος', attribute='time')
	class Meta:
		model = Ergasies
		exclude =('id','text','ticketid')
		export_order = ('dhmos','importdate','app','employee','jobtype','info','name','time')
 		


class ErgasiesAdmin(ImportExportModelAdmin):
	list_display = ('dhmos','app','importdate','name','jobtype','info','employee','time','ticketid')
	search_fields = ['dhmos',]
	list_filter = ['employee','dhmos','jobtype','app']
	ordering = ['importdate']
	resource_class = ErgasiesResource

class AdeiesResource(resources.ModelResource):
	date_hierarchy = 'createddate'
	class Meta:
		model = Adeia


class AdeiesAdmin(ImportExportModelAdmin):
	
	list_display = ('employee', 'adeiatype','startdate','enddate','days','createddate')
	search_fields = ['employee']
	list_filter = ['employee','createddate']

	
class PolisiAdmin(ImportExportModelAdmin):
	list_display = ('dhmos','eidos','posothta','sinoltimi','katagrafi','etos')


class TrainingAdmin(ImportExportModelAdmin):
	list_display = ('foreas', 'importdate', 'training_type', 'app', 'time', 'employee', 'created_at', 'updated_at')
	


admin.site.register(Dhmos, DhmosAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Ergasies, ErgasiesAdmin)
admin.site.register(Service)
admin.site.register(Aithmata)
admin.site.register(Adeia, AdeiesAdmin)
admin.site.register(Hardware)
admin.site.register(Polisi, PolisiAdmin)
admin.site.register(Profile)
admin.site.register(Training, TrainingAdmin)







admin.site.unregister(Group)
admin.site.site_header = "Μαζιώτης Σταύρος & ΣΙΑ ΕΕ"
admin.site.site_title = "Μαζιώτης Σταύρος & ΣΙΑ ΕΕ"
admin.site.index_title = "ACS Services"




