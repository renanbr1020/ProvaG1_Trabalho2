from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    def __str__ (self):
        return ' {}'.format (self.nome)

class Tipo (models.Model):
    nome = models.CharField(max_length=15)

    def __str__ (self):
        return ' {}'.format (self.nome)

class Agenda (models.Model):
    nome = models.CharField(max_length=128) 
    tipo = models.ForeignKey(Tipo)

    def __str__ (self):
        return ' {}'.format (self.nome)

class Compromisso (models.Model):
    nome = models.CharField(max_length=128)
    data_e_hora_de_inicio = models.DateTimeField(blank=True, null=True)
    descricao = models.TextField()
    local = models.TextField()
    agenda = models.ForeignKey(Agenda)
    def __str__ (self):
        return self.nome

class CompromissoUsuario (models.Model):
    compromisso = models.ForeignKey(Compromisso)
    usuario = models.ForeignKey(Usuario)

class AgendaUsuario (models.Model):
    agenda = models.ForeignKey(Agenda)
    usuario = models.ForeignKey(Usuario)
