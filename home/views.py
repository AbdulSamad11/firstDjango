from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'home': "main banda"
    }
    return render(request,'index.html', context)

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'user sent a message')
    return render(request,'contact.html')
