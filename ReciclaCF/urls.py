from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('', include('cadastro.urls')),
    path('', include('usuarios.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
