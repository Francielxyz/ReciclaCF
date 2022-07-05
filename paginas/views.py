from django.views.generic import TemplateView
#Impedir que usuários não autenticados acessem uma determinada página
from django.contrib.auth.mixins import LoginRequiredMixin

from cadastro.models import Endereco_Armazenamento

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/modelo.html'
    