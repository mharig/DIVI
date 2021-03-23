import requests
import time
t = time.localtime()
filename = f'https://www.divi.de/joomlatools-files/docman-files/divi-intensivregister-tagesreports-csv/DIVI-Intensivregister_{t.tm_year}-{t.tm_month}_{t.tm_day}-12-15.csv'
data = requests.get(filename).text
with open('DIVI.csv', 'ta') as f:
    f.write(data+'\n')
