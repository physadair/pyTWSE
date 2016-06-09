#!/usr/bin/env python 

import csv 
import urllib3


url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report201606/201606_F3_1_8_2303.php&type=csv'

http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.status)
print(r.data.decode('cp950'))
