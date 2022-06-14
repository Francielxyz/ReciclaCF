from django.views.generic import TemplateView
#Impedir que usuários não autenticados acessem uma determinada página
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/modelo.html'
