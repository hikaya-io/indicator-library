from django.forms import modelform_factory as mmf
from django.contrib.auth.models import User
from .models import Profile, Indicator
from django import forms
from django.contrib.auth.forms import UserCreationForm


# UserForm = mmf(User, fields = ('first_name', 'last_name', 'email'))
IndicatorAddForm = mmf(Indicator, fields = ('level','sector','subsector',
                                            'number','definition',
                                            'justification','unit_of_measure',
                                            'disaggregation','direction_of_change',
                                            'baseline','rationale_for_target',
                                            'means_of_verification','question_format',
                                            'data_collection_method','denominator',
                                            'numnerator','responsible_person',
                                            'methods_of_analysis','information_use',
                                            'quality_assurance','data_issues','comments'))

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )