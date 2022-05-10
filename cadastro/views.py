from dataclasses import field
from re import template
from statistics import mode
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, Cidade, Perfil, Categoria, Endereco_Armazenamento, Endereco_Armazenamento_Categoria, Item_Descartavel
from django.urls import reverse_lazy
#Impedir que usuários não autenticados acessem uma determinada página
from django.contrib.auth.mixins import LoginRequiredMixin
#Controle de acesso dos login de adm e cliente


class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'uf']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome', 'data_nascimento', 'telefone1', 'telefone2', 'email', 'observacao', 'data_cadastro']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome', 'observacao', 'data_cadastro']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')

class EnderecoArmazenamentoCreate(CreateView):
    model = Endereco_Armazenamento
    fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'data_cadastro', 'cidade']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')

class EnderecoArmazenamentoCategoriaCreate(CreateView):
    model = Endereco_Armazenamento_Categoria
    fields = ['endereco_armazenamento', 'categoria']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')    

class ItemDescartavelCreate(CreateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'data_cadastro', 'perfil', 'categoria', 'endereco_armazenamento']
    template_name = 'cadastro/form.html'
    sucessl_url = reverse_lazy('index')