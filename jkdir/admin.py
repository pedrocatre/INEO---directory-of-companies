from django.contrib import admin
from jkdir.models import  Empresa#, Membro ,Categoria

#class CategoriaAdmin(admin.ModelAdmin):
#	pass
	
#admin.site.register(Categoria, CategoriaAdmin)

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'ceo', 'email', 'validado')
	search_fields = ('titulo', 'descricao')
	ordering = ('validado', 'titulo')
	
	list_editable = ('email', 'validado')
	
admin.site.register(Empresa, EmpresaAdmin)

