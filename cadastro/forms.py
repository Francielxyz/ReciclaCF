from dal import autocomplete

from django import forms
from .models import Endereco_Armazenamento, Perfil, Item_Descartavel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class EnderecoArmazenamentoForm(forms.ModelForm):
    class Meta:
        model = Endereco_Armazenamento
        fields = ['cep', 'bairro', 'rua', 'numero', 'endereco_compartilhado', 'observacao', 'cidade',]
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

class ItemDescatavelForm(forms.ModelForm):
    class Meta:
        model = Item_Descartavel
        fields = ['nome', 'quantidade', 'categoria', 'endereco_armazenamento', 'observacao',]
        widgets = {
            'categoria': autocomplete.ModelSelect2(
                url='buscar-categoria',
                attrs={
                        # Set some placeholder
                        'data-placeholder': 'Buscar categoria...',
                        # Only trigger autocompletion after 3 characters have been typed
                        'data-minimum-input-length': 3,
                    },
                ),
            # 'endereco_armazenamento': autocomplete.ModelSelect2(
            #     url='buscar-endereco',
            #     attrs={
            #             # Set some placeholder
            #             'data-placeholder': 'Buscar endereço...',
            #             # Only trigger autocompletion after 3 characters have been typed
            #             'data-minimum-input-length': 3,
            #         },
            #     ),             
        }

class PerfilCreateForm(UserCreationForm):
    nome = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    telefone = forms.CharField(max_length=18)

    class Meta:
        model = User
        fields = ['nome', 'email', 'telefone', 'username', 'password1', 'password2']

    def clean_email(self):
        emailDigitado = self.cleaned_data['email']
        if User.objects.filter(email=emailDigitado).exists():
            raise ValidationError("O email {} já está em uso.".format(emailDigitado))

        return emailDigitado

    def clean_telefone(self):
        telefoneDigitado = self.cleaned_data['telefone']
        if Perfil.objects.filter(telefone=telefoneDigitado).exists():
            raise ValidationError("O telefone {} já está em uso.".format(telefoneDigitado))

        return telefoneDigitado