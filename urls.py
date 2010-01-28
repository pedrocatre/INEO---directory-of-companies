from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^jkdirectory/', include('jkdirectory.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

        # Pagina inicial
    (r'^$', 'jkdir.views.pagina_inicial'),

	# Pagina visitantes
    (r'^visitantes/$', 'jkdir.views.pagina_visitantes'),
	(r'^empresas/(?P<empresa_id>\d+)/$', 'jkdir.views.detalhe_empresa'),
	
    # Empresas
    (r'^empresas/$', 'jkdir.views.lista_empresa'),
	
	# Empresas
    (r'^change/$', 'jkdir.views.change'),

    # Login
	
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html', 'redirect_field_name':'/'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/?next=/'}),

    (r'^register/$', 'jkdir.views.register'),
)
