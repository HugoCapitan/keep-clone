from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^notes/', include('notes.urls')),
    url(r'^accounts/', include('accounts.urls')),
]