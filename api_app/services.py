
import json

from api_app.utilities import (getDate, getTime, getShiftATime, convertSecToTime,
							   getShiftBTime, getShiftCTime, getFileDateTime)
from api_app.constants import MACHINE_RUNTIME_EXCEDING_LIMIT


def ProductionJSONFile(startDate, startTime, endDate, endTime):
	jsonfile = open('api_app/sample_json_1.json', 'r')
	jsondata = jsonfile.read()

	objs = json.loads(jsondata)
	return filter_obj_with_date_time(objs, startDate, startTime, endDate, endTime)


def MachineJSONFile(startDate, startTime, endDate, endTime):
	jsonfile = open('api_app/sample_json_2.json', 'r')
	jsondata = jsonfile.read()

	objs = json.loads(jsondata)
	return filter_obj_with_date_time(objs, startDate, startTime, endDate, endTime)


def BeltJSONFile(startDate, startTime, endDate, endTime):
	jsonfile = open('api_app/sample_json_3.json', 'r')
	jsondata = jsonfile.read()

	objs = json.loads(jsondata)
	return filter_obj_with_date_time(objs, startDate, startTime, endDate, endTime)


def filter_obj_with_date_time(objects, startDate, startTime, endDate, endTime):
	filter_obj_list = []
	for obj in objects:
		date, time = getFileDateTime(obj['time'])
		if (date >= startDate and date <= endDate) and (time >= startTime and time <= endTime):
			filter_obj_list.append(obj)
	return filter_obj_list


def getAverageBeltValue(data_list):
	result_list = []
	unique_id_list = []

	for data in data_list:
		if data['state']:
			data['belt1'] = 0
		else:
			data['belt2'] = 0

		data['id'] = int(data['id'][2:])

		if data['id'] not in unique_id_list:
			unique_id_list.append(data['id'])

	unique_id_list.sort()

	for unique_id in unique_id_list:
		unique_id_dict = {}
		unique_id_dict['id'] = unique_id
		unique_id_dict['avg_belt1'] = 0
		unique_id_dict['avg_belt2'] = 0
		unique_id_dict['item_count'] = 0
		result_list.append(unique_id_dict)

	for index in range(len(result_list)):
		for data in data_list:
			if result_list[index]['id'] == data['id']:
				result_list[index]['avg_belt1'] += data['belt1']
				result_list[index]['avg_belt2'] += data['belt2']
				result_list[index]['item_count'] += 1

	for index in range(len(result_list)):
		result_list[index]['avg_belt1'] = int(result_list[index]['avg_belt1']/result_list[index]['item_count'])
		result_list[index]['avg_belt2'] = int(result_list[index]['avg_belt2']/result_list[index]['item_count'])
		del result_list[index]['item_count']

	return result_list


def getTotalUtilization(data_list):
	total_runtime = 0
	total_downtime = 0
	utilization = 0

	for data in data_list:
		if data['runtime'] > MACHINE_RUNTIME_EXCEDING_LIMIT:
			more_downtime = data['runtime'] - MACHINE_RUNTIME_EXCEDING_LIMIT
			data['runtime'] = MACHINE_RUNTIME_EXCEDING_LIMIT
			data['downtime'] += more_downtime

	for data in data_list:
		total_runtime += data['runtime']
		total_downtime += data['downtime']

	utilization = (total_runtime)/(total_runtime + total_downtime) * 100

	result = {
				'runtime': convertSecToTime(total_runtime),
				'downtime': convertSecToTime(total_downtime),
				'utilization': float('%.2f' % utilization)
	}

	return result


def getShiftWiseCount(data_list):
	shiftA = {"production_A_count": 0, "production_B_count": 0}
	shiftB = {"production_A_count": 0, "production_B_count": 0}
	shiftC = {"production_A_count": 0, "production_B_count": 0}

	shiftAStartTime, shiftAEndTime = getShiftATime()
	shiftBStartTime, shiftBEndTime = getShiftBTime()
	shiftCStartTime, shiftCEndTime = getShiftCTime()

	for data in data_list:
		time = getFileDateTime(data['time'])[1]
		# shift A time wise
		if time >= shiftAStartTime and time <= shiftAEndTime:
			if data['production_A']:
				shiftA['production_A_count'] += 1
			if data['production_B']:
				shiftA['production_B_count'] += 1

		# shift B time wise
		elif time >= shiftBStartTime and time <= shiftBEndTime:
			if data['production_A']:
				shiftB['production_A_count'] += 1
			if data['production_B']:
				shiftB['production_B_count'] += 1

		#shift C time wise
		elif time >= shiftCStartTime and time <= shiftCEndTime:
			if data['production_A']:
				shiftC['production_A_count'] += 1
			if data['production_B']:
				shiftC['production_B_count'] += 1

	result = {
				'shiftA': shiftA,
				'shiftB': shiftB,
				'shiftC': shiftC
			}

	return result


