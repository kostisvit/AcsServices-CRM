from .models import Ergasies, Employee, Dhmos, Aithmata, Adeia, Training, Hardware
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
import xlwt
import csv
import datetime


# Εξαγωγή πελατών
def export_pelates(request):
    dhmos_queryset = Dhmos.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=pelates.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pelates')
    columns = [
        'Πελάτης',
        'Διεύθυνση',
        'Πόλη',
        'Τηλέφωνο',
        'FAX',
        'E-mail',
        'Website',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for dhmos in dhmos_queryset:
        row_num += 1
        row = [
            dhmos.name,
            dhmos.address,
            dhmos.city,
            dhmos.phone,
            dhmos.fax,
            dhmos.email,
            dhmos.website,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response


#export υπαλλήλων
def export_epafes(request):
    employee_queryset = Employee.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=epafes.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pelates')
    columns = [
        'Πελάτης',
        'Όνομα',
        'Επώνυμο',
        'Τμήμα',
        'Τηλέφωνο',
        'Κινητό',
        'Email',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for employee in employee_queryset:
        row_num += 1
        row = [
            employee.dhmos.name,
            employee.firstname,
            employee.lastname,
            employee.tmhma,
            employee.phone,
            employee.cellphone,
            employee.email,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response



# Export εργασιών έτους
def export_ergasies(request):
    today = datetime.date.today()
    ergasies_queryset = Ergasies.objects.filter(importdate__year=today.year)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ergasies.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Ergasies')
    columns = [
        'Δήμος',
        'Ημ.Καταχ.',
        'Τύπος',
        'Υπαλ.Επικοιν.',
        'Εργασία',
        'Υπάλληλος ACS',
        'Χρόνος',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for ergasies in ergasies_queryset:
        row_num += 1
        row = [
            ergasies.dhmos.name,
            ergasies.importdate.strftime('%d/%m/%Y'),
            ergasies.jobtype,
            ergasies.name,
            ergasies.info,
            ergasies.employee.last_name + " " + ergasies.employee.first_name,
            ergasies.time,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response


# export αιτήματα
def export_aithmata(request):
    today = datetime.date.today()
    aithmata_queryset = Aithmata.objects.filter(importdate__year=today.year)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=aithmata.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Aithmata')
    columns = [
        'Πελάτης',
        'Ημ.Καταχ.',
        'Υπαλ.Επικοιν.',
        'Χρέωση ACS',
        'Ημ.Κλεισ.',
        'Πληροφορίες',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for aithmata in aithmata_queryset:
        row_num += 1
        row = [
            aithmata.dhmos.name,
            aithmata.importdate.strftime('%d/%m/%Y'),
            aithmata.employee,
            aithmata.assign.last_name + " " + aithmata.assign.first_name,
            aithmata.closedate,
            aithmata.info,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            wb.save(response)
    return response


# export άδειες χρήστη
def export_adeia(request):
    today = datetime.date.today()
    adeia_queryset = Adeia.objects.filter(createddate__year=today.year, employee=request.user)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=adeies.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Adeia')
    columns = [
        'Υπάλληλος',
        'Τύπος άδειας',
        'Αρχή',
        'Τέλος',
        'Σύνολο Ημερ.',
        'Καταγραφή',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for adeia in adeia_queryset:
        row_num += 1
        row = [
            adeia.employee.last_name + " " + adeia.employee.first_name,
            adeia.adeiatype,
            adeia.startdate.strftime('%d/%m/%Y'),
            adeia.enddate.strftime('%d/%m/%Y'),
            adeia.days,
            adeia.createddate.strftime('%d/%m/%Y'),
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            wb.save(response)
    return response


# export εκπαιδεύσεις
def export_training(request):
    training_queryset = Training.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=training.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Training')
    columns = [
        'Φορέας',
        'Χώρος',
        'Ημ. Καταχ.',
        'Εργασία',
        'Εφαρμογή',
        'Διάρκεια',
        'Υπάλληλος',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for training in training_queryset:
        row_num += 1
        row = [
            training.foreas,
            training.place,
            training.importdate.strftime('%d/%m/%Y'),
            training.training_type,
            training.app,
            training.time,
            training.employee.last_name + " " + training.employee.first_name,
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response


# export hardware
def export_hardware(request):
    hardware_queryset = Hardware.objects.all()

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=hardware.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Hardware')
    columns = [
        'Υπάλληλος',
        'Η/Υ',
        'Επεξεργαστής',
        'Μνήμη',
        'Οθόνη',
        'Λειτουργικό',
        'Office',
        'Printer',
    ]
    row_num = 1
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    for hardware in hardware_queryset:
        row_num += 1
        row = [
            hardware.employee.last_name + " " + hardware.employee.first_name,
            hardware.pcbrand,
            hardware.cpu,
            hardware.ram,
            hardware.hdd,
            hardware.monitor,
            hardware.windows,
            hardware.office,
            hardware.printer
        ]
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)

    return response
