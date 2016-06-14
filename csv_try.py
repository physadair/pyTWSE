#!/usr/bin/env python

import requests
import csv

url = 'http://winterolympicsmedals.com/medals.csv'
r =  requests.get(url)
text = r.iter_lines()
reader = csv.reader(text, delimiter=',')
print(dir(reader))
