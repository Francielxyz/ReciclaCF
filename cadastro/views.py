from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, Cidade, Perfil, Categoria, Endereco_Armazenamento, Item_Descartavel
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #Impedir que usuários não autenticados acessem uma determinada página
from braces.views import GroupRequiredMixin #Controle de acesso dos login de adm e cliente

############# Create #############
class EstadoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Estado
    group_required = u"Administrador"
    fields = ['nome', 'uf']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-estado')

class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin,CreateView):
    model = Cidade
    group_required = u"Administrador"
    fields = ['nome', 'estado']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-cidade')

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome', 'data_nascimento', 'telefone1', 'telefone2', 'email', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Categoria
    group_required = u"Administrador"
    fields = ['nome', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-categoria')

class EnderecoArmazenamentoCreate(LoginRequiredMixin, CreateView):
    model = Endereco_Armazenamento
    fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'cidade']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-endereco')

class ItemDescartavelCreate(LoginRequiredMixin, CreateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'categoria', 'endereco_armazenamento', 'perfil']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-item-descartavel')


############# Update #############
class EstadoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Estado
    group_required = u"Administrador"
    fields = ["nome", "uf"]
    template_name = "cadastro/form.html"
    success_url = reverse_lazy("listar-estado")

class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Cidade
    group_required = u"Administrador"
    fields = ['nome', 'estado']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-cidade')

class PerfilUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = ['nome', 'data_nascimento', 'telefone1', 'telefone2', 'email', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Categoria
    group_required = u"Administrador"
    fields = ['nome', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-categoria')

class EnderecoArmazenamentoUpdate(LoginRequiredMixin, UpdateView):
    model = Endereco_Armazenamento
    fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'cidade']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-endereco')

class ItemDescartavelUpdate(LoginRequiredMixin, UpdateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'categoria', 'endereco_armazenamento', 'perfil']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-item-descartavel')


############# Delete #############
class EstadoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Estado
    group_required = u"Administrador"
    template_name = "cadastro/excluir/form-delete.html"
    success_url = reverse_lazy("listar-estado")

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Cidade
    group_required = u"Administrador"
    template_name = "cadastro/excluir/form-delete.html"
    success_url = reverse_lazy("index")

class PerfilDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "cadastro/excluir/form-delete.html"
    success_url = reverse_lazy('index')

class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Categoria
    group_required = u"Administrador"
    template_name = "cadastro/excluir/form-delete.html"
    success_url = reverse_lazy('index')

class EnderecoArmazenamentoDelete(LoginRequiredMixin, DeleteView):
    model = Endereco_Armazenamento
    template_name = "cadastro/excluir/form-delete.html"
    success_url = reverse_lazy('index')

class ItemDescartavelDelete(LoginRequiredMixin, DeleteView):
    model = Item_Descartavel
    template_name = "cadastro/excluir/form-delete.html"
    success_url = reverse_lazy('index')


############# List #############
class EstadoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Estado
    group_required = u"Administrador"
    template_name = "cadastro/listas/estados.html"

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Cidade
    group_required = u"Administrador"
    template_name = "cadastro/listas/cidades.html"

class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Categoria
    group_required = u"Administrador"
    template_name = "cadastro/listas/categorias.html"

class ItemDescartavelList(LoginRequiredMixin, ListView):
    model = Item_Descartavel
    template_name = "cadastro/listas/itens_descartaveis.html"

class EnderecoArmazenamentoList(LoginRequiredMixin, ListView):
    model = Endereco_Armazenamento
    template_name = "cadastro/listas/enderecos.html"

############# Sobre #############
class Index(LoginRequiredMixin, TemplateView):
    template_name = 'sobre/sobre.html'
