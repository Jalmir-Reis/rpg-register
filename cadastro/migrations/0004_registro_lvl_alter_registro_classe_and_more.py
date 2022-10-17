# Generated by Django 4.1.2 on 2022-10-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_registro_exp_rpg_alter_registro_campanha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='lvl',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='registro',
            name='classe',
            field=models.CharField(choices=[('', 'Escolha sua classe'), ('Guerreiro', 'Guerreiro'), ('Barbaro', 'Barbaro'), ('Paladino', 'Paladino'), ('Clerigo', 'Clerigo'), ('Mago', 'Mago'), ('Bruxo', 'Bruxo'), ('Ladino', 'Ladino')], max_length=20),
        ),
        migrations.AlterField(
            model_name='registro',
            name='disponivel',
            field=models.CharField(choices=[('S', 'Sábado'), ('D', 'Domingo')], max_length=20),
        ),
        migrations.AlterField(
            model_name='registro',
            name='exp_rpg',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='2', max_length=10),
        ),
        migrations.AlterField(
            model_name='registro',
            name='raca',
            field=models.CharField(choices=[('', 'Escolha sua raça'), ('Humano', 'Humano'), ('Elfo', 'Elfo'), ('Anão', 'Anão'), ('Gnomo', 'Gnomo'), ('Orc', 'Orc')], max_length=20),
        ),
    ]
