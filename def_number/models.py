from django.db import models

class PhoneProvider(models.Model):
    ndc = models.IntegerField()
    snA = models.DecimalField(max_digits=20, decimal_places=0)
    snB = models.DecimalField(max_digits=20, decimal_places=0)
    capacity = models.IntegerField(null=True, blank=True)
    provider = models.TextField(null=True, blank=True)
    region = models.TextField(null=True, blank=True)
    territory_gar = models.TextField(null=True, blank=True)
    inn = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True)

    class Meta:
        app_label = 'def_number'  # Замените 'your_app_label' на фактическое название вашего приложения
        db_table = 'phone_providers'
        indexes = [
            models.Index(fields=['ndc', 'snA', 'snB'], name='idx_provider'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['ndc', 'snA', 'snB'], name='unique_ndc_snA_snB')
        ]

    def __str__(self):
        return f"{self.provider} ({self.ndc}-{self.snA}-{self.snB})"
