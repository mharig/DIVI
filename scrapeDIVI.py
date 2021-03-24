from urllib.request import urlopen
from datetime import datetime, timedelta
t = datetime.today() - timedelta(days=1)
url = f'https://www.divi.de/joomlatools-files/docman-files/divi-intensivregister-tagesreports-csv/DIVI-Intensivregister_{t.year}-{t.month:02d}-{t.day:02d}_12-15.csv'
print(f'Fetching: {url}') 
r = urlopen(url)
data = r.read().decode()
# remove first line (header)
data2 = data[data.find('\n')+1:]
with open('DIVI.csv', 'ta') as f:
    f.write(data2+'\n')
