#!/usr/bin/env python

import csv
import urllib3
import matplotlib.pyplot as plt
import datetime
import locale



def fetch_data(month):
    url = 'http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY_print.php?genpage=genpage/Report2016{0:02d}/2016{0:02d}_F3_1_8_2303.php&type=csv'.format(month)

    http = urllib3.PoolManager()
    r = http.request('GET', url)
    csvreader = csv.reader(r.data.decode('cp950').splitlines())
    next(csvreader)
    next(csvreader)
    #price_data = [data[6] for data in csvreader]
    price_data = [float(data[8].replace(',', '')) for data in csvreader]

    return price_data

def serial_fetch(months=3):
    data = []
    this_month = datetime.date.today().month
    for month in range(this_month-3, this_month):
        data += fetch_data(month)
    return data


plt.plot(serial_fetch(5))
plt.show()

