import django_tables2 as tables


class DeptsViewTableMixin(tables.Table):
    region = tables.Column(accessor='region.name', verbose_name='Region Name')


class EmployeesViewTableMixin(tables.Table):
    dept = tables.Column(accessor='dept.name', verbose_name='Dept name')
    manager = tables.Column(accessor='manager.id', verbose_name='Manager ID')


class CustomersViewTableMixin(tables.Table):
    region = tables.Column(accessor='region.name', verbose_name='Region Name')
    sales_rep = tables.Column(accessor='sales_rep.last_name', verbose_name='Sales Rep Last name')


class OrdersViewTableMixin(tables.Table):
    customer = tables.Column(accessor='customer.id', verbose_name='Customer ID')

