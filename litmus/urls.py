from django.conf.urls import patterns, include, url
from django.contrib import admin
from rip import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'litmus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rip/', include('rip.urls')),
)
