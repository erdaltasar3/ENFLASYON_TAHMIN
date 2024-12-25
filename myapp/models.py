from django.db import models

# Create your models here.

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    
class EconomicData(models.Model):
    country = models.ForeignKey(Country, related_name='economic_data', on_delete=models.CASCADE)
    year = models.IntegerField()
    unemployment_rate = models.FloatField(null=True, blank=True)
    cpi = models.FloatField(null=True, blank=True)
    gdp_growth = models.FloatField(null=True, blank=True)
    unemployment_lag1 = models.FloatField(null=True, blank=True)  # İşsizlik Lag
    interest_rate_lag1 = models.FloatField(null=True, blank=True)  # Faiz Lag
    gdp_growth_lag1 = models.FloatField(null=True, blank=True)  # GSYH Lag

    def __str__(self):
        return f"{self.country.name} - {self.year}"