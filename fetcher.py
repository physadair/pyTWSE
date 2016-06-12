#!/usr/bin/env python 

import csv 
import urllib3
from io import BytesIO


url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report201606/201606_F3_1_8_2303.php&type=csv'

http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.data.decode('cp950'))
csvreader = csv.reader(r.data.decode('cp950'))
print(csvreader)
for i in csvreader:
    print(i)
