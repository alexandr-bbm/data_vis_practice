from django.urls import path
from django.conf.urls import url

from lab1.views import DeptsView, EmployeesView, CustomersView, OrdersView, RegionsView
from . import views

urlpatterns = {
    path('', views.index, name='index'),
    url(r'^depts/$', DeptsView.as_view()),
    url(r'^employees/$', EmployeesView.as_view()),
    url(r'^customers/$', CustomersView.as_view()),
    url(r'^orders/$', OrdersView.as_view()),
    url(r'^regions/$', RegionsView.as_view()),
}
