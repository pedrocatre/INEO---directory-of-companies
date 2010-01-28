# Create your views here.
# -*- coding: utf-8 -*-

from jkdir.models import Empresa
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template.context import RequestContext


# Função que facilita o render das páginas

def render(request,template,context={}):
	return render_to_response(template,context,context_instance=RequestContext(request))


# Create your views here.

def pagina_visitantes(request):
	empresas=Empresa.objects.all();
	
	return render(request, 'visitantes.html', {'empresas':empresas}) #view para ir buscar todas as empresas

@login_required
def pagina_inicial(request):
	#eu=request.user
	#request.user.empresa_set.all()
	print request.user.empresa_set.all() 
	users = User.objects.all().order_by('-id')[:5]
	#livros = Livro.objects.all().order_by('-id')[:5]
	#categorias = Categoria.objects.all().order_by('-id')[:5]
	
	return render(request, 'index.html', {'users':users})
	
@login_required
def detalhe_empresa(request, empresa_id):
	empresa = Empresa.objects.get(id=empresa_id)
	return render(request, 'detalhe_empresa.html', {'empresa': empresa})
	
def change(request):
	empresas=Empresa.objects.all();
	
	return render(request, 'lista_empresa.html', {'empresas':empresas}) #view para ir buscar todas as empresas
		
	
@login_required #meter a protecao pas paginas pa ir antes po login
def lista_empresa(request):
	empresas=Empresa.objects.all();
	
	return render(request, 'lista_empresa.html', {'empresas':empresas}) #view para ir buscar todas as empresas

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            new_user = form.save()

            # DUDE, aqui fazes cenas antes de gravar o user.
            new_user.save()
            
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {
        'form' : form
    })
