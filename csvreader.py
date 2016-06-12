#!/usr/bin/env python 

import csv 
import locale
import datetime
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

infile = '201606_F3_1_8_2303.csv'

with open(infile, encoding='cp950')  as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    for row in reader:
        datestr = row[0].split('/')
        year = int(datestr[0]) + 1911
        month = int(datestr[1])
        day = int(datestr[2])
        date = datetime.date(year, month, day)
        print(date, [locale.atof(i) for i in row[1:]])
