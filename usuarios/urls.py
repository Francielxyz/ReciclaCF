from django.urls import path
from django.contrib.auth import views

from cadastro.views import RegistrarPerfil

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('registrar/', RegistrarPerfil.as_view(), name='registrar'),
]
