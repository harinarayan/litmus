from django.conf.urls import patterns, url

from rip.views import ServiceListView, OperationListView, TestCaseListView
from rip.views import OperationDetailView
from rip.views import ServiceCreateView, OperationCreateView, TestCaseCreateView
from rip.views import ServiceUpdateView, OperationUpdateView, TestCaseUpdateView
from rip.views import ServiceDeleteView, OperationDeleteView, TestCaseDeleteView
from rip.views import submit_testcase, run_testcase, run_operation

urlpatterns = patterns('',
    url(r'^$', ServiceListView.as_view(), name='service-list'),

    url(r'^service/?$', ServiceListView.as_view(), name='service-list'),
    url(r'^service/create/?$', ServiceCreateView.as_view(), name='service-create'),
    url(r'^service/(?P<pk>\d+)/update/?$', ServiceUpdateView.as_view(), name='service-update'),
    url(r'^service/(?P<pk>\d+)/delete/?$', ServiceDeleteView.as_view(), name='service-delete'),

    url(r'^service/(?P<id>\d+)/operation/?$', OperationListView.as_view(), name='operation-list'),
    url(r'^service/(?P<id>\d+)/operation/create/?$', OperationCreateView.as_view(), name='operation-create'),
    url(r'^service/(?P<id>\d+)/operation/(?P<pk>\d+)/?$', OperationDetailView.as_view(), name='operation-detail'),
    url(r'^service/(?P<id>\d+)/operation/(?P<pk>\d+)/update/?$', OperationUpdateView.as_view(), name='operation-update'),
    url(r'^service/(?P<id>\d+)/operation/(?P<pk>\d+)/delete/?$', OperationDeleteView.as_view(), name='operation-delete'),
    url(r'^service/(?P<id>\d+)/operation/(?P<pk>\d+)/run/?$', run_operation, name='operation-run'),

    url(r'^service/(?P<id>\d+)/operation/(?P<operation_id>\d+)/testcase/?$', TestCaseListView.as_view(), name='testcase-list'),
    url(r'^service/(?P<id>\d+)/operation/(?P<operation_id>\d+)/testcase/create/?$', submit_testcase, name='testcase-create'),
    url(r'^service/(?P<id>\d+)/operation/(?P<operation_id>\d+)/testcase/(?P<pk>\d+)/update/?$', submit_testcase, name='testcase-update'),
    url(r'^service/(?P<id>\d+)/operation/(?P<operation_id>\d+)/testcase/(?P<pk>\d+)/delete/?$', TestCaseDeleteView.as_view(), name='testcase-delete'),
    url(r'^service/(?P<id>\d+)/operation/(?P<operation_id>\d+)/testcase/(?P<pk>\d+)/run/?$', run_testcase, name='testcase-run'),
)

