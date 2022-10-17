from django.db import models

CLASSES = (
    ('', 'Escolha sua classe'),
    ('Artificer', 'Artificer'),
    ('Barbarian', 'Barbarian'),
    ('Bard', 'Bard'),
    ('Cleric', 'Cleric'),
    ('Druid', 'Druid'),
    ('Fighter', 'Fighter'),
    ('Monk', 'Monk'),
    ('Paladin', 'Paladin'),
    ('Ranger', 'Ranger'),
    ('Rogue', 'Rogue'),
    ('Sorcerer', 'Sorcerer'),
    ('Warlock', 'Warlock'),
    ('Wizard', 'Wizard')
)

RACA = (
    ('', 'Escolha sua raça'),
    ('Human', 'Human'),
    ('Elf', 'Elf'),
    ('Dwarf', 'Dwarf'),
    ('Halfling', 'Halfling'),
    ('Tiefling', 'Tiefling'),
    ('Half-elf', 'Half-elf'),
    ('Orc', 'Orc')
)

DIA = (
    ('S', 'Sábado'),
    ('D', 'Domingo')
)

EXP = (
    ('S', 'Sim'),
    ('N', 'Não')
)

CAMPANHA = (
    ('Pendente', 'Pendente'),
    ('Ilha do Desespero', 'Ilha do Desespero'),
    ('Novo Mundo', 'Novo Mundo')
)

class Registro(models.Model):
    jogador = models.CharField(max_length=20, verbose_name='Jogador')
    telemovel = models.CharField(max_length=12, verbose_name='Contato')
    idade = models.CharField(max_length=3, verbose_name='Idade')
    data_registro = models.DateTimeField(auto_now=True, verbose_name='Data de Registro')
    personagem = models.CharField(max_length=20, verbose_name='Personagem')
    classe = models.CharField(max_length=20, choices=CLASSES, verbose_name='Classe')
    raca = models.CharField(max_length=20, choices=RACA, verbose_name='Raça')
    disponivel = models.CharField(max_length=20, choices=DIA, verbose_name='Pode Jogar nos')
    exp_rpg = models.CharField(max_length=10, choices=EXP, default='2', verbose_name='Jogou RPG')
    campanha = models.CharField(max_length=50, null=True, choices=CAMPANHA, default='Pendente', verbose_name='Campanha')
    Atributos = models.CharField(max_length=50)
    lvl = models.IntegerField(default=1, verbose_name='Nivel')
    bg = models.TextField(verbose_name='Background')


    def __str__(self):
        return self.jogador