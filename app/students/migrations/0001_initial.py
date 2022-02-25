# Generated by Django 3.2.12 on 2022-02-25 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, unique=True, verbose_name='RG')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefone')),
                ('address', models.TextField(verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('rg', models.CharField(max_length=11, unique=True, verbose_name='RG')),
                ('grade', models.CharField(choices=[('1', '1º Ano'), ('2', '2º Ano'), ('3', '3º Ano'), ('4', '4º Ano'), ('5', '5º Ano'), ('6', '6º Ano'), ('7', '7º Ano'), ('8', '8º Ano'), ('9', '9º Ano'), ('1E', '1º Ano do Ensino Médio'), ('2E', '2º Ano do Ensino Médio'), ('3E', '3º Ano do Ensino Médio'), ('CO', 'Concluído'), ('CA', 'Cancelado')], max_length=2, verbose_name='Série')),
            ],
        ),
        migrations.CreateModel(
            name='StudentParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.parent', verbose_name='Responsável')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(blank=True, null=True, verbose_name='Nota')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class', verbose_name='Classe')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='Aluno')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ManyToManyField(through='students.StudentClass', to='classes.Class', verbose_name='Classe'),
        ),
        migrations.AddField(
            model_name='student',
            name='parents',
            field=models.ManyToManyField(through='students.StudentParent', to='students.Parent', verbose_name='Responsável'),
        ),
    ]