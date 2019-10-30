# Web Scrapping a real Page 

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table=soup.find('table', class_='wikitable')

print (right_table.prettify())


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll('tr'):
    # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
    # first row has 7 TH 
    states = row.findAll('th')
    # other than first row
    if len(cells) == 6:
        A.append(states[0].text.strip())
        #skip the sequence number column
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())


from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))


# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")

