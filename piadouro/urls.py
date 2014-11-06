from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'piadouro_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^new_piado$', 'piadouro_website.views.piado_add', name='new_piado'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name="my_login"),
    url(r'^logout/$', 'piadouro_website.views.sair', name='logout'),
    url(r'^meus_piados/$', 'piadouro_website.views.meus_piados', name='meus_piados'),
    url(r'^users/$', 'piadouro_website.views.users', name='users'),


    url(r'^admin/', include(admin.site.urls)),
)
