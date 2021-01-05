from django.shortcuts import render
from .models import Adeia, Polisi, Ergasies
from django.db.models import Sum, ExpressionWrapper, F, DecimalField, FloatField, Q
from django.db.models.functions import Cast
from django.views.generic import TemplateView
import datetime



class AdeiaChartView(TemplateView):
    template_name = 'charts/adeia_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context["qs"] = Adeia.objects.values('employee__first_name','employee__last_name').filter(Q(createddate__year=query)).exclude(adeiatype='2').annotate(days=Sum('days'))
        return context


class PolisiChartView(TemplateView):
    template_name = 'charts/polisi_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context["qs"] = Polisi.objects.values('dhmos__name').annotate(total=Cast('sinoltimi',output_field=FloatField()))
        return context


class ErgasiaChartView(TemplateView):
    template_name = 'charts/ergasia_chart.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context["qs"] = Ergasies.objects.values('dhmos__name').order_by('dhmos__name').filter(importdate__year=today.year).annotate(total_time=Sum('time'))
        return context