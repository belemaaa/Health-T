from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    specialization = models.CharField(max_length=100, default=None)
    phone_number = models.CharField(max_length=20, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class Patient(models.Model):
    matric = models.CharField(max_length=7, default=None)
    email = models.EmailField(max_length=40, null=True, blank=True)
    phone_no = models.CharField(max_length=15, default=None)
    password = models.CharField(max_length=50, default=None)
    card_no = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.email
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    email = models.CharField(max_length=50, null=True, blank=True)
    appointment_time = models.DateTimeField(null=True, blank=True)
    health_notes = models.TextField(max_length=300, null=True, blank=True)
    phone_no = models.CharField(max_length=20, default=None)
    access_id = models.CharField(max_length=190, default=0000)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
         return f"Appointment with Doctor {self.doctor} on {self.appointment_time}. access id: {self.access_id}"

    
