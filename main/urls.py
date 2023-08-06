from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('view_apointments/', views.view_appointments, name='view_appointments'),
    path('health_data', views.input_health_data, name="health_data"),
    path('ambulance', views.request_ambulance, name="ambulance"),

]
