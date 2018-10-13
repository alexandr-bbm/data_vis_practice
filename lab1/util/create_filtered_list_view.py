from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
import django_filters
import django_tables2 as tables


class EmptyTableMixin(tables.Table):
    pass


def create_filtered_list_view(db_model, filter_fields, table_mixin=EmptyTableMixin, columns_sequence=None):
    class Table(table_mixin, tables.Table):
        class Meta:
            if columns_sequence:
                sequence = columns_sequence
            model = db_model

    class Filter(django_filters.FilterSet):
        class Meta:
            model = db_model
            fields = filter_fields

    class FilteredListView(SingleTableMixin, FilterView):
        template_name = 'lab1/generic_table.html'
        model = db_model

        table_class = Table
        filterset_class = Filter

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['verbose_name'] = db_model._meta.verbose_name_plural
            return context

    return FilteredListView
