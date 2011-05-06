# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'enquete.views.enquetes'),
    (r'^enquetes/$', 'enquete.views.enquetes'),
    (r'^enquetes/(?P<id_enquete>\d+)/$', 'enquete.views.votar'),
    (r'^enquetes/(?P<id_enquete>\d+)/resultado/$', 'enquete.views.resultado'),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    )
