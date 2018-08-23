from .models import Indicator
from rest_framework import viewsets
from indicatorlibrary.quickstart.serializers import *
from .models import Frequency, Indicator, Source
from django.http import HttpResponse
from django.views import generic
from .filters import IndicatorFilter
from django.shortcuts import render,redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, IndicatorAddForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('catalog')
    else:
        form = SignUpForm()
    return render(request, 'quickstart/signup_form.html', {'form': form})

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'quickstart/Profile.html', args)

def about(request):
    return render(request, 'quickstart/about.html')

def add_indicator(request):
    form  = IndicatorAddForm
    return render(request, 'quickstart/add_indicator.html', {'form': form})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FrequencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows frequency to be viewed or edited.
    """
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer

class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows source to be viewed or edited.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class IndicatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows indicators to be viewed or edited.
    """
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer

class AdditionalFieldsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows additional fields to be viewed or edited.
    """
    queryset = AdditionalFields.objects.all()
    serializer_class = AdditionalFieldsSerializer


class IndexView(generic.ListView): # class for indexing and filtering the indicators
    model = Indicator
    template_name = "quickstart/index.html"
    def get_queryset(self):
        return Indicator.objects.filter(level__startswith ="Outcome")

class IndicatorDetailView(generic.DetailView):
    model = Indicator
    paginate_by = 10


def search(request):
    indi_list = Indicator.objects.all()
    indi_filter = IndicatorFilter(request.GET, queryset = indi_list)
    return render(request, 'quickstart/indilist.html', {'filter': indi_filter})

