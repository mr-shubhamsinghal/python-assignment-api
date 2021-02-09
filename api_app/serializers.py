
from rest_framework import serializers


class StartEndTimeFormSerializer(serializers.Serializer):
	start_time = serializers.DateTimeField()
	end_time = serializers.DateTimeField()


class PlantProductionSerializer(serializers.Serializer):
	time = serializers.DateTimeField()
	production_A = serializers.BooleanField()
	production_B = serializers.BooleanField()
