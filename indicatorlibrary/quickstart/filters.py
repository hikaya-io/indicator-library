from django_filters import FilterSet, ModelChoiceFilter, ChoiceFilter
from .models import Indicator


STATUS_CHOICES_LEVEL = (
    ('Goal','Goal'),
    ('Outcome','Outcome'),
    ('Output','Output'),
    ('Activity','Activity'),
    ('Input','Input'),
    ('No level','No level')
)

STATUS_CHOICES_SECTOR = (
    ('Natural Resource Management','Natural Resource Management'),
    ('Nutrition','Nutrition'),
    ('Water, Sanitation, and Hygiene (WASH)','Water, Sanitation, and Hygiene (WASH)'),
    ('Education','Education'),
    ('Agriculture','Agriculture'),
    ('Basic Needs','Basic Needs'),
    ('Conflict Management','Conflict Management'),
    ('Energy','Energy'),
    ('Climate Change Adaptation & Disaster Risk Reduction','Climate Change Adaptation & Disaster Risk Reduction'),
    ('Gender','Gender'),( 'Child Health & Nutrition', 'Child Health & Nutrition'), ('Health','Health'),
    ('Emergency Response','Emergency Response'),('Food Security','Food Security'),('Protection','Protection'),
    ('Early Recovery','Early Recovery'),
    ('Financial services','Financial services'),
    ('Governance','Governance'),
    ('Human rights','Human rights'),
    ('Information Dissemination and Knowledge Management','Information Dissemination and Knowledge Management'),
    ('Youth Development','Youth Development'),
    ('Economic and Market Development','Economic and Market Development'),
    ('Resilience','Resilience'),
    ('Rural Development, Agriculture, and Food Security ','Rural Development, Agriculture, and Food Security '),
    ('Transport','Transport'),
    ('Urban Development ','Urban Development '),
    ('Results and Indicators for Mitigating the Impacts of Displacement and Resettlement ','Results and Indicators for Mitigating the Impacts of Displacement and Resettlement '),
    ('Infrastructure','Infrastructure'),
    ('Capacity development','Capacity development')
)


class IndicatorFilter(FilterSet):
    #level = ModelChoiceFilter(queryset = Indicator.objects.values('level').distinct())
    level = ChoiceFilter(choices = STATUS_CHOICES_LEVEL)
    sector = ChoiceFilter(choices = STATUS_CHOICES_SECTOR)
    class Meta:
        model = Indicator
        fields = {
            'level':['exact'],
            'sector':['exact'],
            'name': ['icontains']
        }
