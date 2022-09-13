from django.urls import path 
from .views import EstadoCreate, CidadeCreate, CategoriaCreate, EnderecoArmazenamentoCreate, ItemDescartavelCreate
from .views import EstadoUpdate, CidadeUpdate, PerfilUpdate, CategoriaUpdate, EnderecoArmazenamentoUpdate, ItemDescartavelUpdate
from .views import EstadoDelete, CidadeDelete, PerfilDelete, CategoriaDelete, EnderecoArmazenamentoDelete, ItemDescartavelDelete
from .views import EstadoList, CidadeList, ItemDescartavelList, CategoriaList, EnderecoArmazenamentoList
from .views import Index
from .views import CidadeAutocomplete

urlpatterns = [
    path('cadastro/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('cadastro/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastro/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastro/endereco/', EnderecoArmazenamentoCreate.as_view(), name='cadastrar-endereco'),
    path('cadastro/item-descartavel/', ItemDescartavelCreate.as_view(), name='cadastrar-item-descartavel'),

    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='editar-perfil'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/endereco/<int:pk>/', EnderecoArmazenamentoUpdate.as_view(), name='editar-endereco'),
    path('editar/item-descartavel/<int:pk>/', ItemDescartavelUpdate.as_view(), name='editar-item-descartavel'),

    path('excluir/estado/<int:pk>/', EstadoDelete.as_view(), name='excluir-estado'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name='excluir-perfil'),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/endereco/<int:pk>/', EnderecoArmazenamentoDelete.as_view(), name='excluir-endereco'),
    path('excluir/item-descartavel/<int:pk>/', ItemDescartavelDelete.as_view(), name='excluir-item-descartavel'),

    path('listar/estados/', EstadoList.as_view(), name='listar-estado'),
    path('listar/cidades/', CidadeList.as_view(), name='listar-cidade'),
    path('listar/categorias/', CategoriaList.as_view(), name='listar-categoria'),
    path('listar/item/', ItemDescartavelList.as_view(), name='listar-item-descartavel'),
    path('listar/enderecos/', EnderecoArmazenamentoList.as_view(), name='listar-endereco'),

    path('sobre/', Index.as_view(), name='sobre'),

    path('buscar/cidade/', CidadeAutocomplete.as_view(), name='buscar-cidade'),

]

