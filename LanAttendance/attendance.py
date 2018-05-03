import csv
import datetime
from dateutil import parser
from collections import defaultdict

start=datetime.datetime.strptime('8:58:00','%H:%M:%S')
end =datetime.datetime.strptime('18:00:00','%H:%M:%S')
dnow=datetime.datetime.now()
print( dnow.time() < start.time(), dnow.time() < end.time())

rivers = {}
id_names = {}
with open('2018_05lanlan.csv', mode='rU', encoding='gb2312') as f:
    reader = csv.reader(f, delimiter=',')
    for n, row in enumerate(reader):
        if not n:
            # Skip header row (n = 0).
            continue  
        no, name, ID, t4, date, time, t7, t8 = row
        if name not in rivers:
            rivers[name] = list()
            id_names[ID] = name
        rivers[name].append((date, time))

id_names = dict(sorted(id_names.items()))
# print(id_names)

name_workdays = {}
for key, value in rivers.items():
    records = value
    # print(key, '#'*10, records)
    groups = defaultdict(list)

    for obj in records:
        groups[obj[0]].append(parser.parse(obj[0]+' ' + obj[1]))

    new_list = groups.values()
    count = 0
    for single_day in new_list:
        # print(min(single_day), max(single_day))
        # min_d = datetime.datetime.strptime(min(single_day),'%H:%M:%S')
        # max_d = datetime.datetime.strptime(max(single_day),'%H:%M:%S')

        min_d = min(single_day)
        max_d = max(single_day)
        if min_d.time() < start.time() and max_d.time() >= end.time():
            print(min(single_day), max(single_day))
            count += 1
    name_workdays[key] = count
    # print(key, count)
outputlist = []
for key, value in id_names.items():
    item = (key, value, name_workdays[value])
    outputlist.append(item)

print(outputlist)
print('总人数:', len(rivers))


def csv_writer_book_to_local(books, dateid , filename):
    with open(filename, 'a') as csvfile:
        fieldnames = ['员工ID', '期间ID','姓名','实际出勤天数']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow({ '员工ID': book[0], '期间ID':dateid,
                             '姓名':book[1], '实际出勤天数':book[2]})

csv_writer_book_to_local(outputlist, '201004','outputlist.csv')