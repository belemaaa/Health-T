from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Doctor, Patient, Appointment
import random


# Create your views here.

# registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        matric_no = request.POST['matric']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        card_no = request.POST['card_no']
         
        
        existing_patient = Patient.filter(email=email)
        if existing_patient:
            context = {
                'error': 'Email already exists'
            }
            return render(request, 'register.html', context)
        
        
        else:
            new_patient = Patient(matric=matric_no, email=email, phone=phone, password=password, card_no=card_no)
            new_patient.save()
            messages.success(request, 'Account successfully created')
            return redirect('login')

    return render(request, 'main/register.html')




def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Invalid Username or Password') 
            return render(request, 'main/login.html')

    return render(request, 'main/login.html')  




# home page view
def index(request):
    return render(request, 'main/index.html')



# generate unique id
def generate_id():
    return ''.join(random.choices('123456789', k=10))



def book_appointment(request):
    if request.method == 'POST':
        username = request.POST['name']
        doctor = request.POST['doctor']
        email = request.POST['email']
        date = request.POST['appointment_time']
        notes = request.POST['health_notes']
        phone = request.POST['phone_no']
        access_id = generate_id()

        new_appointment = Appointment(doctor=doctor, email=email, appointment_time=date, health_notes=notes, phone_no=phone, access_id=access_id)
        new_appointment.save()

        context = {
            'token' : access_id,
            'email' : email,
            'appointment_time': date
        }
        return render(request, 'main/id_page.html', context)

    return render(request, 'main/book_appointment.html')



def view_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user.patient)
    return render(request, 'main/view_appointments.html', {'appointments': appointments})



def input_health_data(request):
    return render(request, 'main/health_data.html')


def request_ambulance(request):
    return render(request, 'main/request_ambulance.html')





