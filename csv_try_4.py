import csv
import io
import urllib.request

url = "http://winterolympicsmedals.com/medals.csv"
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(ftpstream.read().decode('utf-8').splitlines()) #with the appropriate encoding
for row in csvfile:
    print(row)
