#!/usr/bin/env python

import csv
import urllib.request as rq

url = 'http://winterolympicsmedals.com/medals.csv'
response = rq.urlopen(url)
cr = csv.reader(response.read().decode('utf-8'))
data = [row for row in cr]
print(data)
