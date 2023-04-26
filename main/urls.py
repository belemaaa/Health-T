from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book appointment/', views.create_appointment, name='create-appointment'),
    # path('success/', views.appointment_success, name="success"),
    path('view apointments/', views.view_appointments, name='view-appointments'),

]
