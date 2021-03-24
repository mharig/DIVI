from urllib.request import urlopen
from datetime import datetime, timedelta
t = datetime.today() - timedelta(days=1)
url = f'https://www.divi.de/joomlatools-files/docman-files/divi-intensivregister-tagesreports-csv/DIVI-Intensivregister_{t.year}-{t.month}-{t.day}_12-15.csv'
r = urlopen(url)
data = r.read().decode()
with open('DIVI.csv', 'ta') as f:
    f.write(data+'\n')
