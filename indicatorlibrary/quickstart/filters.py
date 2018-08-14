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
    ('Agriculture', 'Agriculture'),
    ('Basic Needs','Basic Needs'),
    ('Capacity development','Capacity development'),
    ('Child Health & Nutrition', 'Child Health & Nutrition'),
    ('Climate Change Adaptation & Disaster Risk Reduction','Climate Change Adaptation & Disaster Risk Reduction'),
    ('Conflict Management','Conflict Management'),
    ('Early Recovery','Early Recovery'),
    ('Economic and Market Development','Economic and Market Development'),
    ('Education','Education'),
    ('Emergency Response','Emergency Response'),
    ('Energy','Energy'),
    ('Financial services', 'Financial services'),
    ('Food Security','Food Security'),
    ('Gender','Gender'),
    ('Governance', 'Governance'),
    ('Health', 'Health'),
    ('Human rights', 'Human rights'),
    ('Information Dissemination and Knowledge Management', 'Information Dissemination and Knowledge Management'),
    ('Infrastructure','Infrastructure'),
    ('Natural Resource Management','Natural Resource Management'),
    ('Nutrition','Nutrition'),
    ('Protection','Protection'),
    ('Resilience','Resilience'),
    ('Rural Development, Agriculture, and Food Security ','Rural Development, Agriculture, and Food Security '),
    ('Results and Indicators for Mitigating the Impacts of Displacement and Resettlement ','Results and Indicators for Mitigating the Impacts of Displacement and Resettlement '),
    ('Transport','Transport'),
    ('Urban Development ','Urban Development '),
    ('Water, Sanitation, and Hygiene (WASH)','Water, Sanitation, and Hygiene (WASH)'),
    ('Youth Development','Youth Development')

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
