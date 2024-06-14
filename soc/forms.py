from django import forms
from .models import Tema

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nazov', 'popis', 'konzultant', 'student', 'odbor', 'konzultacie', 'dostupnost']
        widgets = {
            'nazov': forms.TextInput(attrs={'class': 'form-control'}),
            'popis': forms.Textarea(attrs={'class': 'form-control'}),
            'konzultant': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'odbor': forms.Select(attrs={'class': 'form-control'}),
            'konzultacie': forms.NumberInput(attrs={'class': 'form-control'}),
            'dostupnost': forms.Select(attrs={'class': 'form-control'}),
        }
