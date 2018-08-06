from django_filters import FilterSet, ModelChoiceFilter
from .models import Indicator

class IndicatorFilter(FilterSet):
    # sector = ModelChoiceFilter(queryset = Indicator.objects.order_by().values('sector').distinct())
    class Meta:
        model = Indicator
        fields = {
            'level':['exact'],
            'sector':['exact'],
            'name': ['icontains']
        }
