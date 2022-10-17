from django import forms
from .models import Registro, CLASSES, RACA
from django.forms import RadioSelect
from django.core.validators import RegexValidator

# Funções dentro dos formularios

#UpperCase
class Uppercase(forms.CharField):
	def to_python(self, value):
		return value.upper()

class RegistroForm(forms.ModelForm):
    # VALIDATIONS
    jogador = Uppercase(
    label='Jogador:', max_length=30,
    validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    message="Apenas letras são permitidas !")],
    widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome...'})
)
    telemovel = forms.CharField(
    label='Telemóvel:', max_length=12,
    validators=[RegexValidator(r'^[0-9]*$',
    message="Apenas numeros são permitidos !")],
    widget=forms.TextInput(attrs={'placeholder': 'Digite seu numero de contato...'})
)
    idade = forms.CharField(
    label='Idade:', max_length=2,
    validators=[RegexValidator(r'^[0-9]*$',
    message="Apenas numeros são permitidos !")],
    widget=forms.TextInput(attrs={'placeholder': 'Digite sua idade...'})
)
    personagem = forms.CharField(
    label='Personagem:', max_length=30,
    validators=[RegexValidator(r'^[a-zA-ZÀ-ÿ\s]*$',
    message="Apenas letras são permitidas !")],
    widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do seu personagem...'})
)
    bg = forms.CharField(
    label='Background:', min_length=40, max_length=1000,
    required=False,
    widget=forms.Textarea(attrs={'placeholder': 'Conte um pouco sobre seu personagem...', 'rows':4})
)

# Select Box

    classe = forms.CharField(
        label='Sua Classe:',
        widget=forms.Select(attrs={'class': 'form-control'}, choices=CLASSES))

    raca = forms.CharField(
        label='Sua Raça:',
        widget=forms.Select(attrs={'class': 'form-control'}, choices=RACA))

# RadioSelects

    DIA = [('S', 'Sábado'), ('D', 'Domingo')]
    disponivel = forms.CharField(label='Melhor Dia', widget=RadioSelect(choices=DIA))

    EXP = [('S', 'Sim'), ('N', 'Não')]
    exp_rpg = forms.CharField(label='Já Jogou?', widget=RadioSelect(choices=EXP))

# Class Meta - Outsider
    class Meta:
        model = Registro
        #fields = '__all__'
        exclude = ['Atributos', 'campanha', 'data_registro', 'lvl']


        widgets = {


        }




