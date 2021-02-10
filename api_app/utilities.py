
from datetime import datetime
import time
from pytz import timezone

from api_app.constants import DATE_TIME_FORMAT, DATE_FORMAT, TIME_FORMAT
from api_app.constants import (SHIFT_A_START, SHIFT_A_END,
							   SHIFT_B_START, SHIFT_B_END,
							   SHIFT_C_START, SHIFT_C_END)


def getDateTimeObj(datetime_str):
	datetime_obj = datetime.strptime(datetime_str, DATE_TIME_FORMAT)
	return datetime_obj

def getDateTime(datetime_str):
	datetime_obj = getDateTimeObj(datetime_str)
	return datetime_obj.date(), datetime_obj.time()


def getDate(date_str):
	date_obj = datetime.strptime(date_str, DATE_FORMAT)
	return date_obj.date()


def getTime(time_str):
	time_obj = datetime.strptime(time_str, TIME_FORMAT)
	return time_obj.time()


def getDateTimeSeparate(datetime_str):
	return datetime_str.split(' ')


def getFileDateTime(datetime_str):
	date, time = getDateTimeSeparate(datetime_str)
	date, time = getDate(date), getTime(time)
	return date, time


def getShiftATime():
	start = datetime.strptime(SHIFT_A_START, TIME_FORMAT)
	end = datetime.strptime(SHIFT_A_END, TIME_FORMAT)
	return start.time(), end.time()


def getShiftBTime():
	start = datetime.strptime(SHIFT_B_START, TIME_FORMAT)
	end = datetime.strptime(SHIFT_B_END, TIME_FORMAT)
	return start.time(), end.time()


def getShiftCTime():
	start = datetime.strptime(SHIFT_C_START, TIME_FORMAT)
	end = datetime.strptime(SHIFT_C_END, TIME_FORMAT)
	return start.time(), end.time()


def convertSecToTime(seconds):
	return time.strftime("%Hh:%Mm:%Ss", time.gmtime(seconds))

