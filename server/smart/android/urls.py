from django.urls import path

from . import views

urlpatterns = [
    path('switcher_status', views.switcher_status, name='switcher_status'),
    path('switcher_off', views.switcher_on, name='switcher_off'),
    path('switcher_on/<int:time>', views.switcher_on, name='switcher_on'),
    path('check_up', views.check_up, name='check_up'),
]
