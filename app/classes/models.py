from django.db import models


class Subject(models.Model):
    name = models.CharField('Nome', max_length=200)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField('RG', max_length=20, unique=True)
    phone_number = models.CharField('Telefone', max_length=20)
    address = models.TextField('Endereço')
    subjects = models.ManyToManyField(
        Subject,
        through='Class',
        verbose_name='Matérias'
    )

    def __str__(self):
        return self.name


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Professor')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Matéria')

    def __str__(self):
        return f"{self.teacher.name} - {self.subject.name}"
