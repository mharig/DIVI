import requests
import time
t = time.localtime()
filename = f'https://www.divi.de/divi-intensivregister-tagesreport-archiv-csv/viewdocument/5549/divi-intensivregister-{t.tm_year}-{t.tm_month}-{t.tm_day}-12-15'
data = requests.get(filename).text
with open('data/DIVI.csv', 'ta') as f:
    f.write(data+'\n')
