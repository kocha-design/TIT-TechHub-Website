from django.db import models

class SiteSettings(models.Model):
    """Hii itadhibiti mambo ya jumla kama Logo, Jina la Kampuni, Contact Info"""
    site_name = models.CharField(max_length=100, default="TIT TechHub")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True)
    contact_email = models.EmailField(default="tittechhub.official@gmail.com")
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    office_address = models.TextField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    footer_text = models.CharField(max_length=200, default="Innovate • Develop • Grow")

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class HomePage(models.Model):
    """Hii inadhibiti Hero Section ya Home Page"""
    hero_title = models.CharField(max_length=200, default="Innovate. Develop. Grow.")
    hero_subtitle = models.TextField(default="We build world-class software...")
    hero_background_image = models.ImageField(upload_to='home/', blank=True, null=True)
    hero_button_text = models.CharField(max_length=50, default="Explore Our Services")
    hero_button_link = models.CharField(max_length=100, default="/services/")
    
    # Sehemu ya chini ya Hero (Optional kama unataka features)
    featured_title = models.CharField(max_length=100, blank=True, null=True)
    featured_text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"

    def __str__(self):
        return "Home Page Settings"


class ContactMessage(models.Model):
    """Hii inahifadhi ujumbe kutoka kwa fomu ya Contact"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"