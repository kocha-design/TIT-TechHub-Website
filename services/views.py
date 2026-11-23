from django.shortcuts import render
from .models import Service, TargetMarket, ApproachStep
from core.models import SiteSettings

def services(request):
    core_services = Service.objects.filter(is_core_service=True)
    partner_services = Service.objects.filter(is_core_service=False)
    target_markets = TargetMarket.objects.all()
    approach_steps = ApproachStep.objects.all()
    site_settings = SiteSettings.objects.first()
    
    context = {
        'core_services': core_services,
        'partner_services': partner_services,
        'target_markets': target_markets,
        'approach_steps': approach_steps,
        'settings': site_settings,
    }
    return render(request, 'services.html', context)