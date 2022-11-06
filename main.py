import time
from datetime import datetime, timedelta


def get_last_day_hour(day_range: str):
    if day_range == '':
        return 0

    last_time = (day_range.split("-")[1]).split(":")

    return int(last_time[0]) + int(last_time[1])/60


def get_first_day_hour(day_range: str):
    if day_range == '':
        return 25

    last_time = (day_range.split("-")[0]).split(":")

    return int(last_time[0]) + int(last_time[1])/60


class Parker:

    def __init__(self, phone, sunday, monday, tuesday, wednesday, thursday, friday):
        self.phone = phone
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday


import csv

with open("D:\\python\\random_test\\02.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # ignor the first one

    for line in csv_reader:
        # get the hours for parker
        parker = Parker(phone=str(line[2]), sunday=str(line[3]), monday=line[4], tuesday=line[5],
                        wednesday=line[6], thursday=line[7], friday=line[8])

        for day in csv_reader:
            if get_last_day_hour(parker.sunday) or\
                    get_last_day_hour(parker.monday) or\
                    get_last_day_hour(parker.tuesday) or\
                    get_last_day_hour(parker.wednesday) or\
                    get_last_day_hour(parker.thursday) or\
                    get_last_day_hour(parker.friday) < get_first_day_hour(day[3]):
                print(day[2])


