from django.db import models
from classes.models import Class
from .choices import GradeChoices


class Parent(models.Model):
    name = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    rg = models.CharField('RG', max_length=20, unique=True)
    phone_number = models.CharField('Telefone', max_length=20)
    address = models.TextField('Endereço')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField('Nome', max_length=200)
    rg = models.CharField('RG', max_length=11, unique=True)
    parents = models.ManyToManyField(
        Parent,
        through='StudentParent',
        verbose_name="Responsável"
    )
    grade = models.CharField('Série', max_length=2, choices=GradeChoices.choices)
    classes = models.ManyToManyField(
        Class,
        through='StudentClass',
        verbose_name="Classe"
    )

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    '''
    Using only one score as an example
    '''
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Aluno')
    _class = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Classe')
    score = models.FloatField('Nota', null=True, blank=True)

    def __str__(self):
        return f"{self.student} ({self._class})"


class StudentParent(models.Model):
    '''
    As one student can have multiple guardians
    and a guardian more than one child
    '''
    parent = models.ForeignKey(Parent, on_delete=models.PROTECT, verbose_name='Responsável')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Aluno')

    class Meta:
        unique_together = (('parent', 'student'),)

    def __str__(self):
        return f"{self.student.name} - {self.parent.name}"
