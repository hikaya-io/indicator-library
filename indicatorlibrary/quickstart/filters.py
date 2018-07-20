import django_filters
from .models import Indicator

class IndicatorFilter(django_filters.FilterSet):
    class Meta:
        model = Indicator
        fields = ['level',]