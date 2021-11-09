#!/usr/bin/python3

from datetime import datetime, timedelta

def change_weekday_to_friday(datetime_object):
    weekday = datetime_object.isoweekday()

    if weekday > 5:
        datetime_object += timedelta(days = weekday - 5)
    elif weekday < 5:
        datetime_object -= timedelta(days = weekday + 2)

    return datetime_object


def change_hrs_mins_secs_to_zeroes(datetime_object):
    datetime_object -= timedelta(hours = datetime_object.hour)
    datetime_object -= timedelta(minutes = datetime_object.minute)
    datetime_object -= timedelta(seconds = datetime_object.second)
    
    return datetime_object

def normalise(epoch_time: int) -> int:
    datetime_object = datetime.fromtimestamp(epoch_time)
    new_datetime = (change_hrs_mins_secs_to_zeroes(change_weekday_to_friday(datetime_object)))
    
    return epoch_time, new_datetime.strftime('%s')

    

