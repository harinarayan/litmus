from django.conf.urls import patterns, url

from rip.views import ServiceListView

urlpatterns = patterns('',
    url(r'^$', ServiceListView.as_view(), name='service-list'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)

