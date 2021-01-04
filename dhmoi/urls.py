from django.conf.urls import url
from . import views
from django.conf import settings
import tasks
from tasks.views import index
import timologisi
from timologisi.views import *
from timologisi.update_records import *
from timologisi.delete_records import *
from .charts import *

urlpatterns = [
    url(r'^$', views.home),
    url(r'acs-services/register/', views.user_register, name='register'),
    url(r'acs-services/main/pelates', views.pelatis, name='pelatis'),
    url(r'acs-services/update-records/pelates/(?P<pk>\d+)/',views.pelatis_update, name='pelatis_update'),
    url(r'acs-services/main/epafes', views.epafi, name='epafi'),
    url(r'acs-services/update-records/epafes/(?P<pk>\d+)/',views.epafi_update, name='epafi_update'),
    url(r'acs-services/main/ergasies', views.ergasia, name='ergasia'),
    url(r'acs-services/update-records/ergasies/(?P<pk>\d+)/',views.ergasia_update, name='ergasia_update'),
    url(r'acs-services/main/adeies', views.adeia, name='adeia'),
    url(r'acs-services/update-records/adeies/(?P<pk>\d+)/',views.adeia_update, name='adeia_update'),
    url(r'acs-services/main/aithmata', views.aithma, name='aithma'),
    url(r'acs-services/update-records/aithma/(?P<pk>\d+)/',views.aithma_update, name='aithma_update'),
    url(r'acs-services/main/polisi', views.polisi, name='polisi'),
    url(r'acs-services/update-records/polisi/(?P<pk>\d+)/',views.polisi_update, name='polisi_update'),
    url(r'acs-services/main/service', views.service, name='service'),
    url(r'acs-services/update-records/service/(?P<pk>\d+)/',views.service_update, name='service_update'),
    url(r'acs-services/main/hardware', views.hardware, name='hardware'),
    url(r'acs-services/update-records/hardware/(?P<pk>\d+)/',views.hardware_update, name='hardware_update'),
    url(r'acs-services/main/training', views.training, name='training'),
    #search
    url(r'acs-services/search/eragsies-search',views.search, name='ergasia_search'),
    url(r'acs-services/search/polisi-search',views.search_sales, name='polisi_search'),
    url(r'acs-services/update-records/training/(?P<pk>\d+)/',views.training_update, name='training_update'),
    #add new records
    url(r'acs-services/add-records/pelatis-new',views.dhmospost_new, name='pelatis_new'),
    url(r'acs-services/add-records/epafi-new',views.epafi_new, name='epafi_new'),
    url(r'acs-services/add-records/ergasia-new',views.ergasia_new, name='ergasia_new'),
    url(r'acs-services/add-records/adeia-new',views.adeia_new, name='adeia_new'),
    url(r'acs-services/add-records/aithma-new',views.aithma_new, name='aithma_new'),
    url(r'acs-services/add-records/polisi-new',views.polisi_new, name='polisi_new'),
    url(r'acs-services/add-records/service-new',views.service_new, name='service_new'),
    url(r'acs-services/add-records/training-new',views.training_new, name='training_new'),
    url(r'acs-services/add-records/hardware-new',views.hardware_new, name='hardware_new'),
    # delete records
    url(r'delete_pelatis/(?P<pk>\d+)/',views.delete_pelatis, name='delete_pelatis'),
    url(r'delete_epafi/(?P<pk>\d+)/', views.delete_epafi, name='delete_epafi'),
    url(r'delete_ergasia/(?P<pk>\d+)/',views.delete_ergasia, name='delete_ergasia'),
    url(r'delete_adeia/(?P<pk>\d+)/', views.delete_adeia, name='delete_adeia'),
    url(r'delete_aithma/(?P<pk>\d+)/', views.delete_aithma, name='delete_aithma'),
    url(r'delete_polisi/(?P<pk>\d+)/', views.delete_polisi, name='delete_polisi'),
    url(r'delete_service/(?P<pk>\d+)/',views.delete_service, name='delete_service'),
    url(r'delete_training/(?P<pk>\d+)/',views.delete_training, name='delete_training'),
    url(r'delete_hardware/(?P<pk>\d+)/',views.delete_hardware, name='delete_hardware'),
    #export data
    url(r'^export-pelates/xls/$', views.export_pelates, name='export_pelates'),
    url(r'^export-epafes/xls/$', views.export_epafes, name='export_epafes'),
    url(r'^export-ergasies/xls/$', views.export_ergasies, name='export_ergasies'),
    url(r'^export-aithmata/xls/$', views.export_aithmata, name='export_aithmata'),
    url(r'^export-adeia/xls/$', views.export_adeia, name='export_adeia'),
    url(r'^export-training/xls/$', views.export_training, name='export_training'),
    url(r'^export-hardware/xls/$', views.export_hardware, name='export_hardware'),
    # url to tasks
    url(r'acs-services/tasks/', tasks.views.index, name='index'),
    url(r'acs-services/update_task/(?P<pk>\d+)/', tasks.views.updateTask, name='update_task'),
    url(r'acs-services/delete_task/(?P<pk>\d+)/', tasks.views.deleteTask, name='delete_task'),
    #url timologisi
    url(r'acs-services/timologisi-main/prosfora/', timologisi.views.prosfora, name='prosfora'),
    url(r'acs-services/timologisi-main/symbasi/(?P<pk>\d+)/', timologisi.views.symbasi, name='symbasi'),
    url(r'acs-services/timologisi-main/symbasi/', timologisi.views.symbasi, name='symbasi'),
    url(r'acs-services/timologisi-main/timologisi/(?P<pk>\d+)/', timologisi.views.timologio, name='timologio'),
    url(r'acs-services/timologisi-main/timologisi/', timologisi.views.timologio, name='timologio'),
    url(r'acs-services/timologisi/update/(?P<pk>\d+)/', timologisi.update_records.prosfora_update, name='prosfora_update'),
    url(r'acs-services/symbasi/update/(?P<pk>\d+)/', timologisi.update_records.symbasi_update, name='symbasi_update'),
    url(r'delete_prosfora/(?P<pk>\d+)/',timologisi.delete_records.delete_prosfora, name='delete_prosfora'),
    url(r'delete_contract/(?P<pk>\d+)/',timologisi.delete_records.delete_contract, name='delete_contract'),
    # chained selection ergasia_new
    url(r'api/ergasies/dhmoi-epafes/(?P<pk>\d+)/', views.api_dhmos, name='api_dhmos'),
    url(r'api/ergasies-update/dhmoi-epafes/(?P<pk>\d+)/', views.api_dhmos_update, name='api_dhmos_update'),
    url(r'api/aithmata/dhmoi-epafes/(?P<pk>\d+)/', views.api_aithma, name='api_aithma'),
    url(r'api/prosfora/dhmoi-epafes/(?P<pk>\d+)/', timologisi.views.api_dhmos_prosfora, name='api_dhmos_prosfora'),
    # charts
    url(r'acs-services/adeia-charts', AdeiaChartView.as_view(), name='adeia_chart'),
    url(r'acs-services/polisi-chart', PolisiChartView.as_view(), name='polisi_chart'),
    url(r'acs-services/ergasia-chart', ErgasiaChartView.as_view(), name='ergasia_chart')
    #timologis-test
    



]
