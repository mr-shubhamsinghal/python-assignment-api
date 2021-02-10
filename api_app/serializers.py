
from rest_framework import serializers


class StartEndTimeFormSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
