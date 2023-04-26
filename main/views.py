from django.shortcuts import render, redirect

from .forms import AppointmentForm
from .models import Appointment


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('appointment-success')

    
    else:
        form = AppointmentForm()

    return render(request, 'main/create-appointment.html', {'form': form})



def appointment_success(request):
    return render(request, 'main/appointment_success.html')



def view_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'main/view_appointments.html', {'appointments': appointments})





