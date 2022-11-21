from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Estado, Cidade, Perfil, Categoria, Endereco_Armazenamento, Item_Descartavel
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin #Impedir que usuários não autenticados acessem uma determinada página
from braces.views import GroupRequiredMixin #Controle de acesso dos login de adm e cliente
from django.shortcuts import get_object_or_404
from django.db.models import Q
from dal import autocomplete
from .models import Cidade
from .forms import EnderecoArmazenamentoForm, PerfilCreateForm, ItemDescatavelForm
from django.contrib.auth.models import Group

############# Create #############
class RegistrarPerfil(CreateView):
    template_name = '../../usuarios/templates/usuarios/registrar.html'
    form_class = PerfilCreateForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        try:

            # Valida os dados e da um INSERT no banco
            url = super().form_valid(form)

            grupo = get_object_or_404(Group, name="Cliente")
            self.object.groups.add(grupo)
            self.object.save()
            
            Perfil.objects.create(
                usuario = self.object, 
                nome = form.cleaned_data['nome'] ,
                email = self.object.email,
                telefone = form.cleaned_data['telefone'] ,
            )
        
        except:
            self.object.delete()
            form.add_error(None, "Erro ao criar usuário. Tente novamente")
            return self.form_invalid(form)
            
        # Neste ponto, exite o objeto que foi criado no banco relacional
        # self.object.codigo = hash(self.object.pk)
        # self.object.save()
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["botao"] = "Cadastrar"
        return context

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Categoria
    group_required = u"Administrador"
    fields = ['nome', 'observacao']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-categoria')

class EnderecoArmazenamentoCreate(LoginRequiredMixin, CreateView):
    model = Endereco_Armazenamento
    form_class = EnderecoArmazenamentoForm
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('listar-endereco')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class ItemDescartavelCreate(LoginRequiredMixin, CreateView):
    model = Item_Descartavel
    form_class = ItemDescatavelForm
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
class PerfilUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Perfil
    # group_required = u"Administrador", "Cliente"
    fields = ['nome', 'telefone', 'email']
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
    form_class = EnderecoArmazenamentoForm
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
    form_class = ItemDescatavelForm
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
class CategoriaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Categoria
    group_required = u"Administrador"
    template_name = "cadastro/listas/categorias.html"
    paginate_by = 6

    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            categorias = Categoria.objects.filter(nome__icontains=txt_nome)
        else:
            categorias = Categoria.objects.all()

        return categorias

class ItemDescartavelList(LoginRequiredMixin, ListView):
    model = Item_Descartavel
    template_name = "cadastro/listas/itens_descartaveis.html"
    paginate_by = 6

    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            itens = Item_Descartavel.objects.filter(
                usuario = self.request.user, nome__icontains=txt_nome
                ).select_related("categoria")
        else:
            itens = Item_Descartavel.objects.filter(
                usuario = self.request.user
                ).select_related("categoria")

        return itens

class EnderecoArmazenamentoList(LoginRequiredMixin, ListView):
    model = Endereco_Armazenamento
    template_name = "cadastro/listas/enderecos.html"
    paginate_by = 6

    def get_queryset(self):

        txt_rua = self.request.GET.get('rua')

        if txt_rua:
            enderecos = Endereco_Armazenamento.objects.filter(usuario = self.request.user, rua__icontains=txt_rua)
        else:
            enderecos = Endereco_Armazenamento.objects.filter(usuario = self.request.user)

        return enderecos

############# Sobre #############
class Index(LoginRequiredMixin, TemplateView):
    template_name = 'sobre/sobre.html'


############# Auto Complete #############
class CidadeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Cidade.objects.none()

        qs = Cidade.objects.all()

        if self.q:
            qs = qs.filter(nome__icontains=self.q)

        return qs

class CategoriaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Categoria.objects.none()

        qs = Categoria.objects.all()

        if self.q:
            qs = qs.filter(nome__icontains=self.q)

        return qs

class EnderecoArmazenamentoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Endereco_Armazenamento.objects.rua()

        qs = Endereco_Armazenamento.objects.all()

        if self.q:
            qs = qs.filter(nome__icontains=self.q)

        return qs