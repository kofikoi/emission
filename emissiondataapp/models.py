from django.db import models
from django.urls import reverse

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        url =  reverse('country_detail', args=[int(self.id)])
        print(url)
        return url

    
class Emission(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    iso_alpha = models.CharField(max_length=100)
    year = models.IntegerField()
    total_emissions = models.FloatField()
    coal = models.FloatField()
    oil = models.FloatField()
    gas_fuel_emissions = models.FloatField()
    cement = models.FloatField()
    flaring = models.FloatField()
    other = models.FloatField()
    per_capita = models.FloatField()

    def __str__(self):
        return f"{self.country} ({self.year})"