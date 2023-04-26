from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.TextField()

    def __str__(self):
        return self.user.username



class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric = models.CharField(max_length=7)
    email = models.CharField(max_length=40, null=True, blank=True)
    phone_no = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    card_no = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    email = models.CharField(max_length=50, null=True, blank=True)
    appointment_time = models.DateTimeField()
    health_notes = models.TextField(max_length=300, null=True, blank=True)
    phone_no = models.CharField(max_length=20, default=None)
    access_id = models.CharField(max_length=190, default=0000)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Appointment with Doctor {self.doctor} on {self.appointment_time}"
