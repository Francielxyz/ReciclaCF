from django.contrib import admin

from .models import Estado, Cidade, Perfil, Categoria, Endereco_Armazenamento, Item_Descartavel

# Register your models here.
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Perfil)
admin.site.register(Categoria)
admin.site.register(Endereco_Armazenamento)
admin.site.register(Item_Descartavel)
