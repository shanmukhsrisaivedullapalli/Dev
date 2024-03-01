# views.py
from django.shortcuts import render, redirect
from .models import Contactform
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def contact_post(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contactform.objects.create(email=email, message=message)
        messages.success(request, 'Message Sent Successfully!')
        return redirect('home')
    messages.error(request, 'Error Sending Message!')
    return redirect('home')

def error_view(request):
    status_code = 404
    exception = "Page not found"
    return render(request, 'error.html', {'status_code': status_code, 'exception': exception})

def error_404_view(request, exception):
    status_code = 404
    exception = "Page not found"
    return render(request, 'error.html', {'status_code': status_code, 'exception': exception})

def error_500_view(request):
    status_code = 500
    exception = "Server error"
    return render(request, 'error.html', {'status_code': status_code, 'exception': exception})