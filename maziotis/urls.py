from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('dhmoi.urls'), name='home'),
    path('', include, ('tasks.urls'), name='home'),

]
