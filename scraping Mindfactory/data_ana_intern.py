import warnings
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import traceback
warnings.filterwarnings("ignore")

# Empty lists to store the formatted data
sold = []
price = []
url = []
price_list = []
a = []
try:
    #Open file containing the URLs
    with open('urls.txt', 'r+')as f:

        #Store the URLs in a list
        data = f.readlines()
        # print(type(data))
        print(str(data))
        count = 0
        #Iterate over the list
        for l in data:

            #Replace new line characters while fetching the URLs
            new_data = l.replace('\n', '')
            count = count + 1
            print('URL ' + str(count) + ': ' + str(new_data))


            #Append the data to a new list
            url.append(new_data)

            #Make Http GET Request to the URL
            http_req = requests.get(new_data)
            soup = BeautifulSoup(http_req.text)

            #Find respective tags
            sold_page = soup.findAll("span", {"class": "pcountsold"})
            specialText = soup.find('span', class_ = 'specialPriceText')
            print(specialText)

            if specialText is not None:
                price_val = specialText.getText()
                if str(price_val).startswith('€'):
                    price_val = price_val.replace('€ ', '')

            else:
                price_val = soup.find('div', class_='pprice')
                try:
                    price_val = price_val.contents[4]
                except IndexError: # catch the error
                    price_val='0'
                

            #To replace the ',' with '.' in pricing  - enable the below line of code
            price_val = price_val.replace(',', '.')

            out = price_val
            out2 = sold_page[0].getText()

            # To replace the '.' with ',' in quantities sold -  enable the below line of code
            out2 = out2.replace('.', ',')

            price.append(out.replace('*','').strip())
            sold.append(out2)


# Check if file already exists
except Exception as e:
    print(str(e))
    print(traceback.print_exc())

if os.path.isfile('out_data.csv'):
    df = pd.read_csv('out_data.csv')

#Create new file if not created before
else:
    df = pd.DataFrame(columns = ['DATE','SOLD','PRICE','URL'])

#Current Date
date = datetime.today().strftime('%Y-%m-%d')

for i in range (len(sold)):
    df = df.append({'DATE': date,'SOLD': sold[i], 'PRICE': price[i], 'URL': url[i]}, ignore_index=True)
# print(df)
import numpy as np
df2=df.replace(0,np.nan).dropna(axis=1,how="all")
#Convert URL to string
df.URL = df.URL.astype(str)

#Create csv output file
df.to_csv('out_data.csv',index=False)
print('Csv created, kindly check')