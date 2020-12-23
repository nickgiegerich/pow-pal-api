from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Station
from .models import State
from .serializers import StationSerializer
from .serializers import StateSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class StateAPIView(APIView):
    def get(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StationAPIView(APIView):

    def get(self, request):
        stations = Station.objects.all()
        serializer = StationSerializer(stations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StationDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Station.objects.get(id=id)
        except Station.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_NOT_FOUND)

    def get(self, request, id):
        station = self.get_object(id)
        serializer = StationSerializer(station)
        return Response(serializer.data)

    def put(self, request, id):
        station = self.get_object(id)
        serializer = StationSerializer(station, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        station = self.get_object(id)
        station.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
