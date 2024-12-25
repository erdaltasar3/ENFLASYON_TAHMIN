# myapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa
    
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),  # Hakkımızda
    path('iletisim/', views.iletisim, name='iletisim'),  # İletişim
    path('giris/', views.giris, name='giris'),  # Giriş Yap
    
    path('register/', views.register_view, name='register'),


    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('profil/', views.profile_view, name='profil'),
    
    
    path('countries/', views.grafikler, name='grafikler'),
    
    
    
    path('countries/<int:country_id>/', views.country_detail, name='country_detail'),
    path('tahmin/<int:country_id>/', views.tahmin_yap, name='tahmin_yap'),
    
   
]
