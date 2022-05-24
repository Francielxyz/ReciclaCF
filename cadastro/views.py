from dataclasses import field
from re import template
from statistics import mode
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, Cidade, Perfil, Categoria, Endereco_Armazenamento, Item_Descartavel
from django.urls import reverse_lazy
#Impedir que usuários não autenticados acessem uma determinada página
from django.contrib.auth.mixins import LoginRequiredMixin
#Controle de acesso dos login de adm e cliente

############# Create #############
class EstadoCreate(CreateView):
    model = Estado
    fields = ['nome', 'uf']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome', 'data_nascimento', 'telefone1', 'telefone2', 'email', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class EnderecoArmazenamentoCreate(CreateView):
    model = Endereco_Armazenamento
    fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'cidade']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class ItemDescartavelCreate(CreateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'data_cadastro', 'perfil', 'categoria', 'endereco_armazenamento']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

############# Update #############
class EstadoUpdate(UpdateView):
    model = Estado
    fields = ["nome", "uf"]
    template_name = "cadastro/form.html"
    success_url = reverse_lazy("listar-estado")

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['nome', 'data_nascimento', 'telefone1', 'telefone2', 'email', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class EnderecoArmazenamentoUpdate(UpdateView):
    model = Endereco_Armazenamento
    fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'cidade']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class ItemDescartavelUpdate(UpdateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'data_cadastro', 'perfil', 'categoria', 'endereco_armazenamento']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

############# Delete #############
class EstadoDelete(DeleteView):
    model = Estado
    template_name = "cadastro/form-delete.html"
    success_url = reverse_lazy("listar-estado")

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = "cadastro/form-delete.html"
    success_url = reverse_lazy("index")

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = "cadastro/form-delete.html"
    success_url = reverse_lazy('index')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "cadastro/form-delete.html"
    success_url = reverse_lazy('index')

class EnderecoArmazenamentoDelete(DeleteView):
    model = Endereco_Armazenamento
    template_name = "cadastro/form-delete.html"
    success_url = reverse_lazy('index')

class ItemDescartavelDelete(DeleteView):
    model = Item_Descartavel
    template_name = "cadastro/form-delete.html"
    success_url = reverse_lazy('index')


############# List #############
class EstadoList(ListView):
    model = Estado
    template_name = "cadastro/listas/estados.html"