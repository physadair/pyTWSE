#!/usr/bin/env python

import csv
import urllib3
import urllib.request
from io import BytesIO, StringIO, TextIOWrapper


url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report201606/201606_F3_1_8_2303.php&type=csv'

r = urllib.request.urlopen(url)
print(dir(r))
#print(r.data.decode('cp950'))
csvreader = csv.reader(TextIOWrapper(r, encoding='cp950'))
print(csvreader)
print(dir(csvreader))
#print(csvreader)
for i in csvreader:
    print(i)
