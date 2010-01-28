from django.contrib import admin
from jkdir.models import  Empresa#, Membro ,Categoria

#class CategoriaAdmin(admin.ModelAdmin):
#	pass
	
#admin.site.register(Categoria, CategoriaAdmin)

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'ceo', 'email',)
	search_fields = ('titulo', 'descricao')
	ordering = ('titulo',)
	
	list_editable = ('email',)
	
admin.site.register(Empresa, EmpresaAdmin)

