from django.db.models import Count
from django.views.generic.base import TemplateView
from lab1.models import Order


class IndexPageView(TemplateView):

    template_name = 'lab2/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_vs_orders_count'] = get_date_vs_orders_count_data()
        return context


def get_date_vs_orders_count_data():
    orders_count_per_date = list(Order.objects.values("date_ordered").annotate(Count("id")))
    orders_count_per_date_timestamp = map(convert_date, orders_count_per_date)
    return list_of_dicts_to_list_of_lists(orders_count_per_date_timestamp)

def convert_date(x):
    x['date_ordered'] = x['date_ordered'].timestamp() * 1000
    return x


def list_of_dicts_to_list_of_lists(list_of_dicts):
    return [list(t.values()) for t in list_of_dicts]
