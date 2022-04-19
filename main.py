import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.x-rates.com/table/?from=GBP&amount=1"
data = requests.get(url).text

exchange = input("How much would You like to exchange? ")
if(exchange != ""):
   print('loading...')
   soup = BeautifulSoup(data, 'html.parser')

   tables = soup.find_all('table')
   table = soup.find('table', class_='tablesorter ratesTable')

   collumn_3_name = '%sGBP' % exchange

   df = pd.DataFrame(columns=['Value', '1 GBP', collumn_3_name, 'input'])

   for row in table.tbody.find_all('tr'):
       columns = row.find_all('td')

       if (columns != []):
           value = columns[0].text.strip()
           gbp = columns[1].text.strip()

           df = df.append(
               {'Value': value, '1 GBP': gbp, 'input': exchange}, ignore_index=True)
   df = df.astype({'1 GBP': float, collumn_3_name: float, 'input': float})

   df[collumn_3_name] = round(df['1 GBP'] * df['input'], 2)
   del df['input']
   print(df)



else:
   print("Can't be empty!")

