# -*- coding: utf-8 -*-
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

	# Pagina visitantes - index
	(r'^$', 'django.views.generic.simple.redirect_to',{'url':'/empresas/'}),
	
	# Empresas
	(r'^empresas/$', 'jkdir.views.lista_empresa'),
	(r'^empresas/(?P<empresa_id>\d+)/$', 'jkdir.views.detalhe_empresa'),

	# Register
	(r'^register/$', 'jkdir.views.register'),

	# Login
	(r'^login/$', 'jkdir.views.proteger_login',{'template_name': 'login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/'}),
	
	
	# Pagina inicial para quem está logged-in
	(r'^account/$', 'jkdir.views.change'),
	(r'^account/change/$', 'jkdir.views.change'),
	
	(r'^account/password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'password_change.html'}), 
	(r'^account/password_change/done/$', 'django.contrib.auth.views.password_change_done', {'template_name': 'password_change_done.html'}), 
	
	
	# Password recovery
	(r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name': 'password_reset.html'}),
	(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'password_reset_done.html'}),
	(r'^password_reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'password_reset_confirm.html'}),
	(r'^password_reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'password_change_done.html'}),
)
