from django.shortcuts import render
from .models import AboutPage, CoreValue, TeamMember
from core.models import SiteSettings

def about(request):
    about_content = AboutPage.objects.first()
    core_values = CoreValue.objects.all()
    team_members = TeamMember.objects.all()
    site_settings = SiteSettings.objects.first()
    
    context = {
        'about': about_content,
        'core_values': core_values,
        'team_members': team_members,
        'settings': site_settings,
    }
    return render(request, 'about.html', context)