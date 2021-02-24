import django_filters
from occurrences.models import Occurrence


class OccurrenceFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__id', lookup_expr='iexact')
    category =django_filters.CharFilter(field_name='category__id', lookup_expr='iexact')

    class Meta:
        model = Occurrence
        fields = ('author', 'category', 'status')
