from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Country, EconomicData

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Name alanından slug oluşturur
    list_display = ("name", "description")

@admin.register(EconomicData)
class EconomicDataAdmin(admin.ModelAdmin):
    list_display = ("country", "year", "unemployment_rate", "cpi", "gdp_growth")
    list_filter = ("country", "year")
    search_fields = ("country__name", "year")
