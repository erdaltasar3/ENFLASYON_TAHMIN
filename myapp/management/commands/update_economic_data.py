import numpy as np
import pandas as pd
from django.core.management.base import BaseCommand
from fredapi import Fred
from scipy import stats
from myapp.models import Country, EconomicData

class Command(BaseCommand):
    help = "FRED API'den ekonomik verileri çekerek veritabanına kaydeder."

    def handle(self, *args, **kwargs):
        # FRED API Anahtarı
        fred = Fred(api_key='09e2fa0c64e66c8f426774db8eafa118')

        # Ülke (ABD)
        country, created = Country.objects.get_or_create(name="United States", slug="united-states")

        # FRED API'den veri çekme
        cpi = fred.get_series('CPIAUCSL')  # TÜFE
        unemployment = fred.get_series('UNRATE')  # İşsizlik oranı
        interest_rate = fred.get_series('FEDFUNDS')  # Faiz oranı
        gdp_growth = fred.get_series('A191RL1Q225SBEA')  # GSYH büyüme oranı

        # Yıllık yüzdelik değişim (Enflasyon oranı) hesaplama
        cpi_yoy = cpi.pct_change(periods=12) * 100  # Yıllık değişim

        # Verileri birleştirme
        data = pd.concat([cpi_yoy, unemployment, interest_rate, gdp_growth], axis=1)
        data.columns = ['CPI_YoY', 'Unemployment', 'Interest Rate', 'GDP Growth']
        data.dropna(inplace=True)  # Eksik verileri kaldırma

        # Aykırı değerleri Z-skoru ile temizleme
        data = data[(np.abs(stats.zscore(data)) < 3).all(axis=1)]

        # Lag özelliklerini ekleme
        data['Unemployment_Lag1'] = data['Unemployment'].shift(1)
        data['Interest Rate_Lag1'] = data['Interest Rate'].shift(1)
        data['GDP Growth_Lag1'] = data['GDP Growth'].shift(1)
        data.dropna(inplace=True)

        # Veritabanına kaydetme
        for date, row in data.iterrows():
            year = date.year
            economic_data, created = EconomicData.objects.get_or_create(country=country, year=year)
            economic_data.unemployment_rate = row['Unemployment']
            economic_data.cpi = row['CPI_YoY']
            economic_data.gdp_growth = row['GDP Growth']
            # Ekstra Lag özelliklerini kaydetmek
            economic_data.save()

        self.stdout.write(self.style.SUCCESS(f"ABD için ekonomik veriler başarıyla güncellendi."))
