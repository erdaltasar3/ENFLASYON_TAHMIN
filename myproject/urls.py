# myproject/urls.py
# URL configuration for myproject project.

from django.contrib import admin
from django.urls import include, path  # include fonksiyonunu burada import ediyoruz

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site için URL
    path('', include('myapp.urls')),  # myapp uygulamasının URL'lerini dahil ediyoruz
]
