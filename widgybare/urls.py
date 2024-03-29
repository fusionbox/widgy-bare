from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from xxx.models import site as widgy_site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'widgybare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/widgy/', include(widgy_site.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^owner/(?P<pk>[^/]+)/$', 'xxx.views.owner_detail', name='owner_detail'),
    url(r'^owner/(?P<pk>[^/]+)/form/(?P<form_node_pk>[^/]+)/$', 'xxx.views.owner_form', name='owner_form'),
)
