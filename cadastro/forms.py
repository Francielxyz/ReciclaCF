from dal import autocomplete

from django import forms
from .models import Endereco_Armazenamento

class EnderecoArmazenamentoForm(forms.ModelForm):
    class Meta:
        model = Endereco_Armazenamento
        fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'cidade']
        widgets = {
            'cidade': autocomplete.ModelSelect2(
                url='buscar-cidade',
                attrs={
                        # Set some placeholder
                        'data-placeholder': 'Buscar cidade...',
                        # Only trigger autocompletion after 3 characters have been typed
                        'data-minimum-input-length': 3,
                    },
                )
        }