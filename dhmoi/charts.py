from django.shortcuts import render
from .models import Adeia, Polisi, Ergasies
from django.db.models import Sum
from django.views.generic import TemplateView
import datetime

class AdeiaChartView(TemplateView):
    template_name = 'charts/adeia_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context["qs"] = Adeia.objects.values('employee__first_name','employee__last_name').filter(createddate__year=today.year).exclude(adeiatype='2').annotate(days=Sum('days'))
        return context


class PolisiChartView(TemplateView):
    template_name = 'charts/polisi_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context["qs"] = Polisi.objects.values('dhmos__name').filter(katagrafi__year=today.year).annotate(sinoltimi=Sum('sinoltimi'))
        return context


class ErgasiaChartView(TemplateView):
    template_name = 'charts/ergasia_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context["qs"] = Ergasies.objects.values('dhmos__name').order_by('dhmos__name').filter(importdate__year=today.year).annotate(total_time=Sum('time'))
        return context