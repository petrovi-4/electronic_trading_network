import django_filters

from company.models import Company

class CompanyFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(
        field_name='country',
        lookup_expr='icontains'
    )

    class Meta:
        model = Company
        fields = ('country',)
