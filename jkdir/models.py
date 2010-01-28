# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class Categoria(models.Model):
#	nome = models.CharField(max_length=20)
#	descricao = models.TextField('descrição', null=True, blank=True)
#	
#	def __unicode__(self):
#		return u'%s' % self.nome
#	
#	def get_absolute_url(self):
#		return u'/categorias/%d/' % self.id


	
class Empresa(models.Model):
	titulo = models.CharField('título', max_length=50)
	ceo=models.CharField('CEO', max_length=50)
	descricao = models.TextField('descrição', null=True, blank=True)
	
	email = models.CharField('email', max_length=20)
	homepage = models.URLField(verify_exists=True, null=True, blank=True)
	nomeTwitter = models.CharField('Nome de utilizador do twitter', max_length=50)
	telefone=models.CharField('telefone', max_length=50)
	#categorias = models.ManyToManyField(Categoria, null=True, blank=True)
	#membros = models.ManyToManyField(Membro, null=True, blank=True)
	dono = models.ForeignKey(User, unique=True, null=True)
	validado= models.BooleanField('validado', default= False)
	
	def __unicode__(self):
		return u'%s' % self.titulo
		
	def get_absolute_url(self):
		return u'/empresas/%d/' % self.id


