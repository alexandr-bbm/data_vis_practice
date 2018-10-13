from django.shortcuts import render
from lab1.models import Dept, Employee, Region, Customer, Order
from lab1.util.create_filtered_list_view import create_filtered_list_view
from lab1.util.view_tables import DeptsViewTableMixin, EmployeesViewTableMixin, CustomersViewTableMixin, \
    OrdersViewTableMixin


def index(request):
    return render(request, 'lab1/index.html')


DeptsView = create_filtered_list_view(
    db_model=Dept,
    table_mixin=DeptsViewTableMixin,
    filter_fields={
        'id': ['iexact'],
        'name': ['icontains'],
        'region__name': ['icontains']
    },
    columns_sequence=('id', 'name')
)


EmployeesView = create_filtered_list_view(
    db_model=Employee,
    table_mixin=EmployeesViewTableMixin,
    filter_fields={
        'id': ['iexact'],
        'last_name': ['icontains'],
        'first_name': ['icontains'],
        'title': ['icontains'],
        'salary': ['gt', 'lt'],
        'dept__name': ['icontains'],
    },
    columns_sequence=('id', 'last_name', 'first_name', 'title', 'salary')
)


CustomersView = create_filtered_list_view(
    db_model=Customer,
    table_mixin=CustomersViewTableMixin,
    filter_fields={
        'id': ['iexact'],
        'name': ['icontains'],
        'phone': ['icontains'],
        'region__name': ['icontains'],
        'sales_rep__last_name': ['icontains'],
    },
    columns_sequence=('id', 'name', 'phone', 'region')
)


OrdersView = create_filtered_list_view(
    db_model=Order,
    table_mixin=OrdersViewTableMixin,
    filter_fields={
        'id': ['iexact'],
        'total': ['lt', 'gt'],
    },
    columns_sequence=('id', 'date_ordered', 'date_shipped', 'total')

)


RegionsView = create_filtered_list_view(
    db_model=Region,
    filter_fields={
        'id': ['iexact'],
        'name': ['icontains'],
    }
)
