# -*- encoding: utf-8 -*-

from django.db import models

class Enquete(models.Model):
    
    titulo = models.CharField(max_length=100)
    pergunta = models.TextField()

    def __unicode__(self):
        return self.titulo

class Opcao(models.Model):
    
    enquete = models.ForeignKey('Enquete')
    valor = models.CharField(max_length=255)
    total_votos = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return self.valor

    class Meta:
        verbose_name = u'Opção'

