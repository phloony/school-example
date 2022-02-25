from django.db import models


class GradeChoices(models.TextChoices):
    PRIMEIRO = '1', '1º Ano'
    SEGUNDO = '2', '2º Ano'
    TERCEIRO = '3', '3º Ano'
    QUARTO = '4', '4º Ano'
    QUINTO = '5', '5º Ano'
    SEXTO = '6', '6º Ano'
    SETIMO = '7', '7º Ano'
    OITAVO = '8', '8º Ano'
    NONO = '9', '9º Ano'
    PRIMEIRO_EM = '1E', '1º Ano do Ensino Médio'
    SEGUNDO_EM = '2E', '2º Ano do Ensino Médio'
    TERCEIRO_EM = '3E', '3º Ano do Ensino Médio'
    CONCLUIDO = 'CO', 'Concluído'
    CANCELADO = 'CA', 'Cancelado'
