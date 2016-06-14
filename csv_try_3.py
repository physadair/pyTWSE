import csv
import io
import urllib.request

url = "http://winterolympicsmedals.com/medals.csv"
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(io.TextIOWrapper(ftpstream)) #with the appropriate encoding
for row in csvfile:
    print(row)
