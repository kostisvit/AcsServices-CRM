from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('acsservices/@dM1N/$login/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'template_name': 'registration/logout.html'}, name='logout'),
    path('', include('dhmoi.urls'), name='home'),
    path('', include, ('tasks.urls'), name='home')
    #path('', include, ('timologisi.urls'), name='home')

]
