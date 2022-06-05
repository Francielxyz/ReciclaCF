from django.urls import path
from .views import Index

urlpatterns = [
    path('inicio/', Index.as_view(), name='inicio'),
]
