from django.conf.urls import patterns, url

from rip.views import ServiceListView, OperationListView, TestCaseListView
from rip.views import OperationDetailView
from rip.views import ServiceCreateView #, OperationCreateView, TestCaseCreateView

urlpatterns = patterns('',
    url(r'^$', ServiceListView.as_view(), name='service-list'),
    url(r'^service/?$', ServiceListView.as_view(), name='service-list'),
    url(r'^service/create/?$', ServiceCreateView.as_view(), name='service-create'),
    url(r'^service/(?P<id>\d+)/operation/?$', OperationListView.as_view(), name='operation-list'),
    url(r'^service/(?P<id>\d+)/operation/(?P<pk>\d+)/?$', OperationDetailView.as_view(), name='operation-detail'),
    url(r'^service/(?P<id>\d+)/operation/(?P<operation_id>\d+)/testcase/?$', TestCaseListView.as_view(), name='testcase-list'),
)

