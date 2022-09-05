from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, Cidade, Perfil, Categoria, Endereco_Armazenamento, Item_Descartavel
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #Impedir que usuários não autenticados acessem uma determinada página
from braces.views import GroupRequiredMixin #Controle de acesso dos login de adm e cliente
from django.shortcuts import get_object_or_404
from django.db.models import Q

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

    def form_valid(self, form):

        # Ante do super, não existe objeto.
        # Estamos trabalhando com os dados do formulário
        form.instance.usuario = self.request.user

        # Valida os dados e da um INSERT no banco
        url = super().form_valid(form)

        # Neste ponto, exite o objeto que foi criado no banco relacional
        # self.object.codigo = hash(self.object.pk)
        # self.object.save()
        return url

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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class ItemDescartavelCreate(LoginRequiredMixin, CreateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'categoria', 'endereco_armazenamento']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-item-descartavel')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

    def get_context_data(self, *args, **kwargs):
        dados = super().get_context_data(*args, **kwargs)
        
        dados['form'].fields['endereco_armazenamento'].queryset = Endereco_Armazenamento.objects.filter(
            Q(usuario=self.request.user) | Q(endereco_compartilhado = True) #Condição OU
        )
        return dados

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

    def get_object(self):
        self.object = get_object_or_404(
            Endereco_Armazenamento, 
            usuario=self.request.user, 
            pk=self.kwargs['pk']
        )

        return self.object 

class ItemDescartavelUpdate(LoginRequiredMixin, UpdateView):
    model = Item_Descartavel
    fields = ['nome', 'quantidade', 'observacao', 'categoria', 'endereco_armazenamento']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-item-descartavel')

    def get_object(self):
        self.object = get_object_or_404(
            Item_Descartavel, 
            usuario=self.request.user, 
            pk=self.kwargs['pk']
        )

        return self.object 


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
    paginate_by = 5

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Cidade
    group_required = u"Administrador"
    template_name = "cadastro/listas/cidades.html"
    paginate_by = 5

class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Categoria
    group_required = u"Administrador"
    template_name = "cadastro/listas/categorias.html"
    paginate_by = 5

class ItemDescartavelList(LoginRequiredMixin, ListView):
    model = Item_Descartavel
    template_name = "cadastro/listas/itens_descartaveis.html"
    paginate_by = 5

    def get_queryset(self):
        self.object_list = Item_Descartavel.objects.filter(usuario = self.request.user)
        return self.object_list

class EnderecoArmazenamentoList(LoginRequiredMixin, ListView):
    model = Endereco_Armazenamento
    template_name = "cadastro/listas/enderecos.html"
    paginate_by = 5

    # Modifica a query padrão de select que vai no banco
    def get_queryset(self):

        # Faz com que apenas os dados pertencentas aquele usuário seja mostrado
        self.object_list = Endereco_Armazenamento.objects.filter(usuario=self.request.user)

        return self.object_list

############# Sobre #############
class Index(LoginRequiredMixin, TemplateView):
    template_name = 'sobre/sobre.html'
