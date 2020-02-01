import requests
from pprint import pprint
from bs4 import BeautifulSoup
link=requests.get("https://www.iplt20.com/stats/2019")
soup=BeautifulSoup(a.text,"html.parser")
table_row=soup.find_all("tr",class_=" ")
for i in table_row:
	print(i)