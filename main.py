phone = []
sunday = []
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []


def get_last_day_hour(day_range: str):
    if day_range == '':
        return 0

    last_time = (day_range.split("-")[1]).split(":")

    return int(last_time[0]) + int(last_time[1]) / 60


def get_first_day_hour(day_range: str):
    if day_range == '':
        return 23

    last_time = (day_range.split("-")[0]).split(":")

    return int(last_time[0]) + int(last_time[1]) / 60


import csv

with open("D:\\python\\random_test\\03.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    # These 3 skips are the first row and 2 tests
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        phone.append(line[2])
        sunday.append(line[3])
        monday.append(line[4])
        tuesday.append(line[5])
        wednesday.append(line[6])
        thursday.append(line[7])
        friday.append(line[8])

number_of_students = len(phone)

csv_file.close()

for i in range(0, number_of_students):
    for j in range(0, number_of_students):
        if get_last_day_hour(sunday[i]) < get_first_day_hour(sunday[j]) \
                and get_last_day_hour(monday[i]) < get_first_day_hour(monday[j]) \
                and get_last_day_hour(tuesday[i]) < get_first_day_hour(tuesday[j]) \
                and get_last_day_hour(wednesday[i]) < get_first_day_hour(wednesday[j]) \
                and get_last_day_hour(thursday[i]) < get_first_day_hour(thursday[j]) \
                and get_last_day_hour(friday[i]) < get_first_day_hour(friday[j]):
            print(phone[j])
    print("End of matches for " + phone[i])
    print("______________________________")
