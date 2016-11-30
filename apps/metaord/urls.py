from django.conf.urls import include, url
from django.contrib import admin, auth
from metaord import settings


urlpatterns = [
    url(r'^', include('front.urls')),
    url(r'^chief/', include('chief.urls')),
    url(r'^worker/', include('worker.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]