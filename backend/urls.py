from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authentication.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^djoser-auth/', include('djoser.urls')),
    url(r'^$', 'backend.views.home', name='home'),
)