from django import forms
from . import models

class FormCadFilmes(forms.ModelForm):
    # id_categoria = forms.DateField(label='Selecione a categoria',
    #             widget=forms.DateInput(
    #                 attrs={
    #                     'class' : 'form-control'
    #                 }
    #             ),
    #             )
   
    class Meta:
        model = models.Filmes
        fields = '__all__'


class FormCategoria(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = '__all__'