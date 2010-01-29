# -*- coding: utf-8 -*-

from jkdir.models import Empresa
from jkdir.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

# Função que facilita o render das páginas

def render(request,template,context={}):
	return render_to_response(template,context,context_instance=RequestContext(request))


# Create your views here.

def pagina_visitantes(request):
	empresas=Empresa.objects.all()
	
	return render(request, 'visitantes.html', {'empresas':empresas}) #view para ir buscar todas as empresas
	
def proteger_login(request, *args, **kwargs):
	if request.method == 'POST':
		usern=request.POST['username']
		
		emp= Empresa.objects.filter(dono__username=usern)
		if len(emp) >0:
			print emp[0].validado
			if not emp[0].validado:
				erro = 'A conta ainda não está validada.'
				return render(request, 'erro.html', {'erro':erro})
		else:
			erro ='A empresa não existe.'
			return render(request, 'erro.html', {'erro':erro})
			
		
	return login(request, *args, **kwargs)

@login_required
def pagina_inicial(request):
	#eu=request.user
	#request.user.empresa_set.all()
	print request.user.empresa_set.all() 
	users = User.objects.all().order_by('-id')[:5]
	#livros = Livro.objects.all().order_by('-id')[:5]
	#categorias = Categoria.objects.all().order_by('-id')[:5]
	
	return render(request, 'index.html', {'users':users})
	
def detalhe_empresa(request, empresa_id):
	empresa = Empresa.objects.get(id=empresa_id)
	return render(request, 'detalhe_empresa.html', {'empresa': empresa})
	
@login_required
def change(request):

	emp=request.user.empresa_set.all()[0]
	if request.method == 'POST':
			user_form = UserEditForm(request.POST, request.FILES, instance = request.user)
			emp_form = EmpresaForm(request.POST, request.FILES, instance = emp)
			
			if emp_form.is_valid():
				emp = emp_form.save()
				if user_form.is_valid():
					user = user_form.save()
					user.email=emp.email
					user.save()
				
				
				return HttpResponseRedirect("/")
	else:
		user_form = UserEditForm(instance = request.user)
	
		emp_form = EmpresaForm(instance = emp)
			
	return render(request, "register.html", {
		'user_form' : user_form, 'emp_form' : emp_form, 'editing' : True})

		
	
def lista_empresa(request):
	empresas=Empresa.objects.all();
	
	return render(request, 'lista_empresa.html', {'empresas':empresas}) #view para ir buscar todas as empresas



def register(request):

	if request.method == 'POST':
		user_form = UserCreationForm(request.POST, request.FILES)
		emp_form = EmpresaForm(request.POST, request.FILES)
		
		if emp_form.is_valid():
			emp = emp_form.save()
			if user_form.is_valid():
				user = user_form.save()
				user.email=emp.email
				user.save()
				emp.dono=user
				emp.save()
            
            
			return HttpResponseRedirect("/")
	else:
		user_form = UserCreationForm()
		emp_form = EmpresaForm()
		
	return render(request, "register.html", {
		'user_form' : user_form, 'emp_form' : emp_form
	})
