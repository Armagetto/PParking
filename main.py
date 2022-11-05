import time
from datetime import datetime, timedelta


class Parker:

    def __init__(self, sunday, monday, tuesday, wednesday, thursday, friday):
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
        parker = Parker(line[3], line[4], line[5], line[6], line[7], line[8])
        # TODO: logic loop for the compare part of days and hours
        #see if free by day

        #free by hour
        # sunday
        #see if any match the same day

        # monday


print(parker.sunday)
