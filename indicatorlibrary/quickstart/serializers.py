from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Indicator, Source, Frequency, AdditionalFields


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    indicator_key = serializers.UUIDField(read_only=True)
    id = serializers.ReadOnlyField()
    actuals = serializers.ReadOnlyField()

    class Meta:
        model = Indicator
        fields='__all__'

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    source_key = serializers.UUIDField(read_only=True)
    id = serializers.ReadOnlyField()
    actuals = serializers.ReadOnlyField()

    class Meta:
        model = Source
        fields='__all__'

class FrequencySerializer(serializers.HyperlinkedModelSerializer):
    frequency_key = serializers.UUIDField(read_only=True)
    id = serializers.ReadOnlyField()
    actuals = serializers.ReadOnlyField()

    class Meta:
        model = Frequency
        fields='__all__'

class AdditionalFieldsSerializer(serializers.HyperlinkedModelSerializer):
    additional_fields_key = serializers.UUIDField(read_only=True)
    id = serializers.ReadOnlyField()
    actuals = serializers.ReadOnlyField()

    class Meta:
        model = AdditionalFields
        fields='__all__'


fields = '__all__'
