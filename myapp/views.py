from django.shortcuts import render, redirect
import pandas as pd


def index(request):
    return render(request, 'myapp/index.html')


def grafikler(request):
    return render(request, 'grafikler.html')  # Grafikler

def hakkimizda(request):
    return render(request, 'hakkimizda.html')  # Hakkımızda

def iletisim(request):
    return render(request, 'iletisim.html')  # İletişim

def giris(request):
    return render(request, 'giris.html')  # Giriş Yap


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Başarılı girişten sonra yönlendirme
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı!')
    return render(request, 'giris.html')  # Giriş formu sayfasını renderla


from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Başarıyla kayıt oldunuz! Şimdi giriş yapabilirsiniz.')
                return redirect('login')  # Kayıt sonrası giriş sayfasına yönlendirme
            else:
                messages.error(request, 'Bu kullanıcı adı zaten alınmış.')
        else:
            messages.error(request, 'Şifreler eşleşmiyor!')
    return render(request, 'kayit.html')  # Kayıt formu sayfasını renderla


from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profil.html')



from django.shortcuts import render, get_object_or_404
from .models import Country


from django.shortcuts import render
from .models import Country

def grafikler(request):
    countries = Country.objects.exclude(id__isnull=True)  # ID'si olmayanları hariç tut
    return render(request, 'grafikler.html', {'countries': countries})





from django.shortcuts import render, get_object_or_404
from .models import Country, EconomicData


from django.shortcuts import render, get_object_or_404
from .models import Country, EconomicData

def country_detail(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    economic_data = EconomicData.objects.filter(country=country).order_by('year')

    # Veriler grafik için hazırlanıyor
    labels = [data.year for data in economic_data]
    cpi_data = [data.cpi for data in economic_data]
    unemployment_data = [data.unemployment_rate for data in economic_data]
    gdp_growth_data = [data.gdp_growth for data in economic_data]  # GDP verileri eklendi

    context = {
        'country': country,
        'labels': labels,
        'cpi_data': cpi_data,
        'unemployment_data': unemployment_data,
        'gdp_growth_data': gdp_growth_data,  # GDP verileri context'e eklendi
    }
    return render(request, 'myapp/country_detail.html', context)



def tahmin_yap(request, country_id):
    country = get_object_or_404(Country, id=country_id)
    context = {
        'country': country,
    }
    return render(request, 'myapp/tahmin_yap.html', context)

