from django.db.models import Count, Avg
from django.views.generic.base import TemplateView
from lab1.models import Order, Employee, Dept


class IndexPageView(TemplateView):
    template_name = 'lab2/index.html'


class OrdersPerDatePageView(TemplateView):
    template_name = 'lab2/orders_per_date.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_vs_orders_count'] = OrdersPerDatePageView.get_date_vs_orders_count_data()
        return context

    @staticmethod
    def get_date_vs_orders_count_data():
        orders_count_per_date = list(Order.objects.values("date_ordered").annotate(Count("id")))
        orders_count_per_date_timestamp = map(OrdersPerDatePageView.convert_date, orders_count_per_date)
        return list_of_dicts_to_list_of_lists(orders_count_per_date_timestamp)

    @staticmethod
    def convert_date(x):
        x['date_ordered'] = x['date_ordered'].timestamp() * 1000
        return x

class EmployeesPerDeptPageView(TemplateView):
    template_name = 'lab2/employees_per_dept.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees_per_dept'] = EmployeesPerDeptPageView.get_employees_per_dept_data()
        return context

    @staticmethod
    def get_employees_per_dept_data():
        aggregated = list(Dept.objects.values('name').annotate(number_of_employees=Count('employee')))
        data = list_of_dicts_to_list_of_lists(aggregated)
        return data

class AvgSalaryPerDeptPageView(TemplateView):
    template_name = 'lab2/avg_salary_per_dept.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avg_salary_per_dept'] = AvgSalaryPerDeptPageView.get_avg_salary_per_dept_data()
        return context

    @staticmethod
    def get_avg_salary_per_dept_data():
        aggregated = list(Dept.objects.values('name').annotate(avg_salary=Avg('employee__salary')))
        data = list_of_dicts_to_list_of_lists(aggregated)
        return data

def list_of_dicts_to_list_of_lists(list_of_dicts):
    return [list(t.values()) for t in list_of_dicts]