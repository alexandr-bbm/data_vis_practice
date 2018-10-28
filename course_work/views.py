from django.views.generic.base import TemplateView

from lab1.models import Dept


class IndexPageView(TemplateView):
    template_name = 'course_work/index.html'


class MapView(TemplateView):
    template_name = 'course_work/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depts'] = list(Dept.objects.all().values())
        return context
