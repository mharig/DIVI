from urllib.request import urlopen
import time
t = time.localtime()
url = f'https://www.divi.de/joomlatools-files/docman-files/divi-intensivregister-tagesreports-csv/DIVI-Intensivregister_{t.tm_year}-{t.tm_month}_{t.tm_day}-12-15.csv'
r = urlopen(url)
data = r.read().decode()
with open('DIVI.csv', 'ta') as f:
    f.write(data+'\n')
