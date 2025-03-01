# residuos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views 
from . import views

router = DefaultRouter()
router.register(r'residuos', views.ResiduoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar_residuo/', views.registrar_residuo, name='registrar_residuo'),
    path('listar_coletas/', views.listar_coletas, name='listar_coletas'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('catalogo_recompensas/', views.catalogo_recompensas, name='catalogo_recompensas'),  # Adicione esta linha
    path('trocar_recompensa/<int:recompensa_id>/', views.trocar_recompensa, name='trocar_recompensa'),  # Adicione esta linha
    path('api/', include(router.urls)),
]


