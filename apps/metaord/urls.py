from django.conf.urls import include, url
from django.contrib import admin, auth
from metaord import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('chief.urls')),
    url(r'', include('worker.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]