from django.db import models

class AboutPage(models.Model):
    """Inadhibiti Ukurasa wa About"""
    title = models.CharField(max_length=200, default="About Us")
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    company_overview = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    class Meta:
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page Settings"


class CoreValue(models.Model):
    """Core Values za Kampuni (Innovation, Quality, etc.)"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="Mfano: fas fa-lightbulb")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    """Wanachama wa Timu (Founder, Technical Director, etc.)"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.role}"