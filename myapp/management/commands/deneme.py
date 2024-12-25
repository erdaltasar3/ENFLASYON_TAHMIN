import pandas as pd
from myapp.models import EconomicData


def train_and_predict(country_id):
    # Veritabanından verileri çek
    data_queryset = EconomicData.objects.filter(country_id=country_id).values(
        'cpi', 'unemployment_rate', 'interest_rate_lag1', 'gdp_growth', 'gdp_growth_lag1', 'unemployment_lag1'
    )
    data = pd.DataFrame.from_records(data_queryset)
    print("Veritabanından alınan veri:")
    print(data.head())  # İlk birkaç satırı kontrol edin





from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Veritabanından alınan veriyi işleyen örnek komut"

    def handle(self, *args, **kwargs):
        from myapp.models import EconomicData
        import pandas as pd

        data_queryset = EconomicData.objects.all().values()
        data = pd.DataFrame.from_records(data_queryset)
        print("Veritabanından alınan veri:")
        print(data.head())
