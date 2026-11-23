from django.db import models

class Service(models.Model):
    """Hii inadhibiti Huduma Zote (Website Dev, Mobile App Dev, n.k.)"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, blank=True, null=True, help_text="Mfano: fas fa-code")
    is_core_service = models.BooleanField(default=True, help_text="True = Core Service, False = Partner Service")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class TargetMarket(models.Model):
    """Wateja/Walengwa (SMEs, Startups, etc.)"""
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Target Market"
        verbose_name_plural = "Target Markets"

    def __str__(self):
        return self.name


class ApproachStep(models.Model):
    """Hatua za Approach (Understand, Analyze, Propose...)"""
    step_number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['step_number']
        verbose_name = "Approach Step"
        verbose_name_plural = "Approach Steps"

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"