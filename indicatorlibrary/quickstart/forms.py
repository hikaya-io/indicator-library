from django.forms import modelform_factory as mmf
from django.contrib.auth.models import User
from .models import Profile, Indicator
from django import forms
from django.contrib.auth.forms import UserCreationForm


# UserForm = mmf(User, fields = ('first_name', 'last_name', 'email'))
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

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('organization',)

# class UserProfileForm(forms.ModelForm):
#     def __init__(self, instance=None, *args, **kwargs):
#         # Add these fields from the user object
#         _fields = ('first_name', 'last_name', 'email',)
#         # Retrieve initial (current) data from the user object
#         _initial = model_to_dict(instance.user, _fields) if instance is not None else {}
#         # Pass the initial data to the base
#         super(UserProfileForm, self).__init__(initial=_initial, instance=instance, *args, **kwargs)
#         # Retrieve the fields from the user model and update the fields with it
#         self.fields.update(fields_for_model(User, _fields))
#
#     class Meta:
#         model = UserProfile
#         exclude = ('user',)
#
#     def save(self, *args, **kwargs):
#         u = self.instance.user
#         u.first_name = self.cleaned_data['first_name']
#         u.last_name = self.cleaned_data['last_name']
#         u.email = self.cleaned_data['email']
#         u.save()
#         profile = super(UserProfileForm, self).save(*args,**kwargs)
#         return profile