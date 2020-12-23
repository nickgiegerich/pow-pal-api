from rest_framework import serializers
from .models import Station
from .models import State

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['state', 'state_id', 'stations']

        