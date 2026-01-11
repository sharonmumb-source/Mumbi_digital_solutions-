from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')
def portfolio(request):
    projects = [
        {
            'title': 'E-Commerce Website',
            'description': 'A fully responsive e-commerce website built with Django and Bootstrap. Features include product catalog, shopping cart, and payment integration.',
            'image': 'images/project1.jpg',  # put your image in static/images/
        },
        {
            'title': 'custom website',
            'description': 'A Django-based hotel booking system that enables customers to reserve rooms online and allows <br>hotel administrator to manage bookings, rooms and availability efficiently',
            'image': 'images/project2.jpg',
        },
        {
            'title': 'web-based information system',
            'description': 'allows users to access, manage, and update information online through a browser, enabling centralized data storage, real-time updates, and role-based access from anywhere.',
            'image': 'images/project3.jpg',
        },
    ]
    return render(request, 'portfolio.html', {'projects': projects})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

