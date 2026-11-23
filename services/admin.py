from django.contrib import admin
from .models import Service, TargetMarket, ApproachStep

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_core_service', 'order')
    list_editable = ('is_core_service', 'order')
    list_filter = ('is_core_service',)

@admin.register(TargetMarket)
class TargetMarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

@admin.register(ApproachStep)
class ApproachStepAdmin(admin.ModelAdmin):
    list_display = ('title', 'step_number', 'description')   # Badilisha mpangilio
    list_editable = ('step_number',)                          # Sasa si field ya kwanza
    list_display_links = ('title',)                           # Weka link kwenye title