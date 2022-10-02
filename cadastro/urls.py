from django.urls import path 
from .views import CategoriaCreate, EnderecoArmazenamentoCreate, ItemDescartavelCreate
from .views import PerfilUpdate, CategoriaUpdate, EnderecoArmazenamentoUpdate, ItemDescartavelUpdate
from .views import PerfilDelete, CategoriaDelete, EnderecoArmazenamentoDelete, ItemDescartavelDelete
from .views import ItemDescartavelList, CategoriaList, EnderecoArmazenamentoList
from .views import Index
from .views import CidadeAutocomplete, CategoriaAutocomplete, EnderecoArmazenamentoAutocomplete

urlpatterns = [
    path('cadastro/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastro/endereco/', EnderecoArmazenamentoCreate.as_view(), name='cadastrar-endereco'),
    path('cadastro/item-descartavel/', ItemDescartavelCreate.as_view(), name='cadastrar-item-descartavel'),

    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='editar-perfil'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/endereco/<int:pk>/', EnderecoArmazenamentoUpdate.as_view(), name='editar-endereco'),
    path('editar/item-descartavel/<int:pk>/', ItemDescartavelUpdate.as_view(), name='editar-item-descartavel'),

    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name='excluir-perfil'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/endereco/<int:pk>/', EnderecoArmazenamentoDelete.as_view(), name='excluir-endereco'),
    path('excluir/item-descartavel/<int:pk>/', ItemDescartavelDelete.as_view(), name='excluir-item-descartavel'),

    path('listar/categorias/', CategoriaList.as_view(), name='listar-categoria'),
    path('listar/item/', ItemDescartavelList.as_view(), name='listar-item-descartavel'),
    path('listar/enderecos/', EnderecoArmazenamentoList.as_view(), name='listar-endereco'),

    path('sobre/', Index.as_view(), name='sobre'),

    path('buscar/cidade/', CidadeAutocomplete.as_view(), name='buscar-cidade'),
    path('buscar/categoria/', CategoriaAutocomplete.as_view(), name='buscar-categoria'),
    path('buscar/enderco/', EnderecoArmazenamentoAutocomplete.as_view(), name='buscar-endereco'),

]

