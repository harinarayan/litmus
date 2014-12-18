from django.conf.urls import patterns, url

from rip.views import ServiceListView, OperationListView

urlpatterns = patterns('',
    url(r'^$', ServiceListView.as_view(), name='service-list'),
    url(r'^service/?$', ServiceListView.as_view(), name='service-list'),
    url(r'^service/(?P<id>\d+)/operation/?$', OperationListView.as_view(), name='operation-list'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)

