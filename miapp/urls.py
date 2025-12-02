from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('ManoRobotica/', views.mano_robotica_view, name='ManoRobotica'),
# path(' ', views.login_view, name='login')
    path('guardar-movimiento/', views.guardar_movimiento, name='save_movement'),
    path('cargar-movimiento/', views.cargar_movimiento, name='load_movement'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)