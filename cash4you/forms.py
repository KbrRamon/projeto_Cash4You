from django import forms
from .models import Produto, Servico, ContaPagar

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'preco_custo', 'preco_venda']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: Camiseta'}),
            'quantidade': forms.NumberInput(attrs={'min': 0}),
            'preco_custo': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'preco_venda': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
        }

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: Consultoria'}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
        }

class ContaPagarForm(forms.ModelForm):
    class Meta:
        model = ContaPagar
        fields = ['nome', 'valor', 'vencimento', 'paga']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: Aluguel'}),
            'valor': forms.NumberInput(attrs={'step': '0.01', 'min': 0}),
            'vencimento': forms.DateInput(attrs={'type': 'date'}),
        }