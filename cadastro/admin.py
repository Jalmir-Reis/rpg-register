from django.contrib import admin
from .models import Registro
from django.utils.html import format_html

class RegistroAdm(admin.ModelAdmin):
    list_filter = ['campanha']
    readonly_fields = ['jogador', 'telemovel', 'idade', 'exp_rpg', 'classe', 'raca', 'disponivel', 'Atributos', 'data_registro', 'personagem', 'bg']
    list_display = ['jogador', 'telemovel', 'idade', 'exp_rpg', 'classe', 'raca', 'disponivel', 'Atributos', 'status']
    search_fields = ['personagem', 'classe', 'raca', 'campanha']
    list_per_page = 15
    # Organização dos campos no Admin
    fieldsets = [
        ('Mestre', {'fields': ['jogador', 'idade', 'telemovel', 'exp_rpg', 'disponivel']}),
        ('Personagem', {'fields': ['personagem', 'classe', 'raca', 'Atributos', 'bg', 'campanha', 'lvl', 'data_registro']})
    ]

    def status(self, obj):
        if obj.campanha == 'Pendente':
            color = '#fea95e'
        else:
            color = '#28a745'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.campanha))

    status.allow_tags = True

admin.site.register(Registro, RegistroAdm)


