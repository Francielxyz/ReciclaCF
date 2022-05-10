from django.urls import path 
from .views import EstadoCreate, CidadeCreate, PerfilCreate, CategoriaCreate, EnderecoArmazenamentoCreate, EnderecoArmazenamentoCategoriaCreate, ItemDescartavelCreate

urlpatterns = [
    path('cadastro/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('cadastro/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('cadastro/estado/', PerfilCreate.as_view(), name='cadastrar-perfil'),
    path('cadastro/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastro/endereco/', EnderecoArmazenamentoCreate.as_view(), name='cadastrar-endereco'),
    path('cadastro/endereco-categoria/', EnderecoArmazenamentoCategoriaCreate.as_view(), name='cadastrar-endereco-categoria'),
    path('cadastro/item-descartavel/', ItemDescartavelCreate.as_view(), name='cadastrar-item-descartavel'),

    #Adicionar os edith de todas as entidades
    #   path('atualizar/pedido/<int:pk>/', PedidoUpdate.as_view(), name='atualizar-pedido'),
]
