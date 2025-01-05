from django.db import models


class MentalHealth(models.Model):
    class Meta:
        verbose_name_plural = "Mental Health"

    country = models.CharField(max_length=254, blank=False, null=True)
    country_code = models.CharField(max_length=3, blank=False, null=True)
    year = models.IntegerField(blank=False, null=True)
    schitzophrenia = models.DecimalField(decimal_places=6, max_digits=7, blank=True, null=True)
    bipolar_disorder = models.DecimalField(decimal_places=6, max_digits=7, blank=True, null=True)
    eating_disorders = models.DecimalField(decimal_places=6, max_digits=7, blank=True, null=True)
    anxiety_disorders = models.DecimalField(decimal_places=6, max_digits=7, blank=True, null=True)
    depression = models.DecimalField(decimal_places=6, max_digits=7, blank=True, null=True)

    def __str__(self):
        return f'{self.country} - {self.id}'
