from django.views.generic.base import TemplateView
import django_filters
from django.http import JsonResponse

from lab3.models import Temperature, MeasureDate


class IndexPageView(TemplateView):
    template_name = 'lab4/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month_options'] = get_month_options()
        return context

class T2mFilter(django_filters.FilterSet):
    class Meta:
        model = Temperature
        fields = {
            'date__value': ['iexact'],
            'lon__value': ['gt', 'lt'],
            'lat__value': ['gt', 'lt'],
            'value': ['gt', 'lt'],
        }

def t2m_filtered(request):
    filtered = T2mFilter(request.GET, queryset=Temperature.objects.all())
    data = list(filtered.qs.values(
        'value',
        'date__value',
        'lon__value',
        'lat__value',
    ))
    return JsonResponse({'t2m': data})

def get_month_options():
    dates = MeasureDate.objects.all()
    result = []
    for date in dates:
        item = {
            'value': date.value.strftime('%Y-%m-%d'),
            'title': date.value.strftime("%B"),
        }
        result.append(item)
    return result