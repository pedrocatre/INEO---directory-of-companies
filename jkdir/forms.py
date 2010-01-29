# -*- coding: utf-8 -*-

from django.forms import *
from jkdir.models import *
from django.contrib.auth.forms import UserChangeForm

class EmpresaForm(ModelForm):
	class Meta:
		model= Empresa
		exclude = ("validado","dono")
		
class UserEditForm(UserChangeForm):
	class Meta:
		model=User
		fields= ('username',)