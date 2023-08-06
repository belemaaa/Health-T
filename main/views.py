from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Doctor, Patient, Appointment
import random
from django.contrib.auth.decorators import login_required

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
            return render(request, 'main/register.html', context)    
        else:
            new_patient = Patient(matric=matric_no, email=email, phone=phone, password=password, card_no=card_no)
            new_patient.save()
            messages.success(request, 'Account successfully created')
            return render(request, "main/login.html")

    return render(request, 'main/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        # password = request.POST.get('password', '')
        password = request.POST['password']
        
        patient = Patient.objects.filter(email=email, password=password)
        #request.session['patient'] = patient.email
    
        if patient:
            return render(request, "main/index.html")
        else:
            context = {
                'error': 'Invalid username or password'
            }
            return render(request, "main/login.html", context)
    return render(request, "main/login.html")  

# home page view
def index(request):
    return render(request, "main/index.html")

# generate unique id
def generate_id():
    return ''.join(random.choices('123456789', k=10))

def book_appointment(request):
    doctors = Doctor.objects.all()

    if request.method == 'POST':
       # inputed_email = request.POST['name']
        doctor_id = request.POST['doctor']
        inputed_email = request.POST['email']
        date = request.POST['date']
        notes = request.POST['notes']
        phone = request.POST['phone']
        access_id = generate_id()

        patient = Patient.objects.get(email=inputed_email) 
        doctor = Doctor.objects.get(id=doctor_id)
        print(doctors)

        new_appointment = Appointment(
            patient=patient,
            doctor=doctor, 
            email=inputed_email, 
            appointment_time=date, 
            health_notes=notes, 
            phone_no=phone, 
            access_id=access_id
            )
        new_appointment.save()
        context = {
            'token' : access_id,
            'email' : inputed_email,
            'appointment_time': date,     
        }
        return render(request, 'main/id_page.html', context)
    context = {
        'doctors' : doctors
    }
    return render(request, 'main/book_appointment.html', context)

def view_appointments(request):
    # patient_id = request.session['patient']
    # patient_view = Patient.objects.get(email=patient_id)
    appointments = Appointment.objects.filter()
    return render(request, "main/view_appointments.html", {'appointments': appointments})

def input_health_data(request):
    return render(request, 'main/health_data.html')

def request_ambulance(request):
    return render(request, 'main/request_ambulance.html')





