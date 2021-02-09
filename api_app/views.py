from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api_app.serializers import StartEndTimeFormSerializer

from api_app.utilities import getDateTime
from api_app.services import ProductionJSONFile, getShiftWiseCount
from api_app.services import MachineJSONFile, getTotalUtilization
from api_app.services import BeltJSONFile, getAverageBeltValue


@api_view(['GET'])
def QuestionSolutionLinks(request):
	api_urls = {
		'Question 1': '/getPlantProductionUnit/',
		'Question 2': '/getMachineUtilization/',
		'Question 3': '/getAverageBelt/'
	}
	return Response(api_urls)


@api_view(['POST'])
def PlantProduction(request):
	serializer = StartEndTimeFormSerializer(data=request.data)
	if serializer.is_valid():
		startDate, startTime = getDateTime(serializer.data['start_time'])
		endDate, endTime = getDateTime(serializer.data['end_time'])
		data_list = ProductionJSONFile(startDate, startTime, endDate, endTime)
		shift_wise_count_dict = getShiftWiseCount(data_list)
		return Response(shift_wise_count_dict, status=status.HTTP_200_OK)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def MachineUtilization(request):
	serializer = StartEndTimeFormSerializer(data=request.data)
	if serializer.is_valid():
		startDate, startTime = getDateTime(serializer.data['start_time'])
		endDate, endTime = getDateTime(serializer.data['end_time'])
		data_list = MachineJSONFile(startDate, startTime, endDate, endTime)
		total_utilization_dict = getTotalUtilization(data_list)
		return Response(total_utilization_dict, status=status.HTTP_200_OK)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def AverageBelt(request):
	serializer = StartEndTimeFormSerializer(data=request.data)
	if serializer.is_valid():
		startDate, startTime = getDateTime(serializer.data['start_time'])
		endDate, endTime = getDateTime(serializer.data['end_time'])
		data_list = BeltJSONFile(startDate, startTime, endDate, endTime)
		average_belt_dict = getAverageBeltValue(data_list)
		return Response(average_belt_dict, status=status.HTTP_200_OK)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
