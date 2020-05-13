from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        label="Nome",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome',
        })
    )
    document = forms.CharField(
        label="CPF/CNPJ",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'CPF/CNPJ',
        })
    )
    class Meta:
        model = Person
        fields = [
            'name',
            'document',
        ]
