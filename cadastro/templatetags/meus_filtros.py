from dataclasses import replace
from django import template
import re

register = template.Library()


@register.filter(name="remover")
def remover(texto, r):
    return texto,replace(r, "")


@register.filter(name="cep_eh_Valido")
def cep_eh_Valido(cep):
    if len(cep) == 8:
        padrao_cep = re.compile(r'(\d){5}(\d){3}')
        if(padrao_cep.match(cep)):
            return True
        else:
            return False
    else:
        return False