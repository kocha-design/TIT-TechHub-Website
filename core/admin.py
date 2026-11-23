from django.contrib import admin
from .models import SiteSettings, HomePage, ContactMessage, Stat

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return True

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if HomePage.objects.exists():
            return False
        return True

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'order')   # Tumehamisha title mbele
    list_editable = ('value', 'order')           # value sasa sio ya kwanza
    list_display_links = ('title',)              # title iwe ndio link ya kufungua