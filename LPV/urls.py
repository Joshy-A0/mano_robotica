from django.contrib import admin
from django.urls import path, include  # 👈 nota el 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),  # 👈 esto enlaza las URLs de tu app
    path("miapp/", include("miapp.urls")),

]
