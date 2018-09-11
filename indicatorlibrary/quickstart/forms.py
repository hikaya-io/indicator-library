from django.forms import modelform_factory as mmf
from django.contrib.auth.models import User
from .models import Profile, Indicator
from django import forms
from django.contrib.auth.forms import UserCreationForm



IndicatorAddForm = mmf(Indicator, fields = ('name','level','sector','subsector',
                                            'number','definition',
                                            'justification','unit_of_measure',
                                            'disaggregation','direction_of_change',
                                            'baseline','rationale_for_target',
                                            'means_of_verification','question_format',
                                            'data_collection_method','denominator',
                                            'numerator','responsible_person',
                                            'method_of_analysis','information_use',
                                            'quality_assurance','data_issues','comments'))

class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('organization',)

