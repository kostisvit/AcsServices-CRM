from django.conf.urls import url
from . import views
from django.conf import settings

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
    url(r'acs-services/main/training', views.training, name='training'),
    url(r'acs-services/update-records/training/(?P<pk>\d+)/',views.training_update, name='training_update'),
    url(r'acs-services/add-records/pelatis-new',views.dhmospost_new, name='pelatis_new'),
    url(r'acs-services/add-records/epafi-new',views.epafi_new, name='epafi_new'),
    url(r'acs-services/add-records/ergasia-new',views.ergasia_new, name='ergasia_new'),
    url(r'acs-services/add-records/adeia-new',views.adeia_new, name='adeia_new'),
    url(r'acs-services/add-records/aithma-new',views.aithma_new, name='aithma_new'),
    url(r'acs-services/add-records/polisi-new',views.polisi_new, name='polisi_new'),
    url(r'acs-services/add-records/service-new',views.service_new, name='service_new'),
    url(r'acs-services/add-records/training-new',views.training_new, name='training_new'),
    url(r'delete_pelatis/(?P<pk>\d+)/',views.delete_pelatis, name='delete_pelatis'),
    url(r'delete_epafi/(?P<pk>\d+)/', views.delete_epafi, name='delete_epafi'),
    url(r'delete_ergasia/(?P<pk>\d+)/',views.delete_ergasia, name='delete_ergasia'),
    url(r'delete_adeia/(?P<pk>\d+)/', views.delete_adeia, name='delete_adeia'),
    url(r'delete_aithma/(?P<pk>\d+)/', views.delete_aithma, name='delete_aithma'),
    url(r'delete_polisi/(?P<pk>\d+)/', views.delete_polisi, name='delete_polisi'),
    url(r'delete_service/(?P<pk>\d+)/',views.delete_service, name='delete_service'),
    url(r'delete_training/(?P<pk>\d+)/',views.delete_training, name='delete_training'),
    url(r'^export-pelates/xls/$', views.export_pelates, name='export_pelates'),
    url(r'^export-epafes/xls/$', views.export_contacts, name='export_contacts'),
    url(r'^export-ergasies/xls/$', views.export_ergasies, name='export_ergasies'),
    url(r'^export-aithmata/xls/$', views.export_aithmata, name='export_aithmata'),
    url(r'^export-adeia/xls/$', views.export_adeia, name='export_adeia'),






]
