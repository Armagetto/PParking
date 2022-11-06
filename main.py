import time
from datetime import datetime, timedelta


def get_last_day_hour(day_range: str):
    if day_range == '':
        return ''

    last_time = (day_range.split("-")[1]).split(":")

    return int(last_time[0]) + int(last_time[1])/60


def get_first_day_hour(day_range: str):
    if day_range == '':
        return ''

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

with open("D:\\python\\random_test\\01.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # ignor the first one

    for line in csv_reader:
        # get the hours for parker
        parker = Parker(phone=str(line[2]), sunday=str(line[3]), monday=line[4], tuesday=line[5],
                        wednesday=line[6], thursday=line[7], friday=line[8])
        print(parker.sunday)
        print(get_first_day_hour(parker.sunday))
        print(get_last_day_hour(parker.sunday))
        # for line_to_look in csv_reader:
        #     if int(parker.sunday.split(":")) < int(line_to_look[0][5:]):
        #         print(parker.phone)

        # TODO: logic loop for the compare part of days and hours
        # go day by day and see if free for the other guys

        # monday
