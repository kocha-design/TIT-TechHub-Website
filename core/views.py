from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteSettings, HomePage, ContactMessage

def home(request):
    site_settings = SiteSettings.objects.first()
    home_content = HomePage.objects.first()
    context = {
        'settings': site_settings,
        'home': home_content,
    }
    return render(request, 'home.html', context)

def contact(request):
    site_settings = SiteSettings.objects.first()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect('contact')
    
    return render(request, 'contact.html', {'settings': site_settings})