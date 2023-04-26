from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('', views.index, name="index"),
    path('book appointment/', views.book_appointment, name='book_appointment'),
    path('view apointments/', views.view_appointments, name='view-appointments'),
    path('health data', views.input_health_data, name="health_data"),
    path('ambulance', views.request_ambulance, name="ambulance"),

]
