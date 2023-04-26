from django.db import models
from django.utils import timezone

# Create your models here.


# appointment model
class Appointment(models.Model):
    patients_name = models.CharField(max_length= 100)
    doctors_name = models.CharField(max_length = 100)
    appointment_time = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Appointment with Doctor {self.doctors_name} on {self.appointment_time}"


# symptoms model