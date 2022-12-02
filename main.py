'''
    Stage: Development-01
    @author: Umut Geyik, 120200145
    @author: Caner Gülay, 11811012
'''
from bs4 import BeautifulSoup
import requests


url_to_fetch="https://www.zomato.com/istanbul/galata-restaurants"

with open("./zomato.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

main_div = soup.find_all('div', class_ = 'sc-1mo3ldo-0 sc-jjbLbC cXGlSn') 

restaurant_name = soup.find_all('h4', class_ = 'sc-1hp8d8a-0 sc-gUlUPW jWSmKx')
restaurant_rate = soup.find_all('div', class_ = 'sc-1q7bklc-1 cILgox')

print(len(restaurant_name))
print(len(restaurant_rate))
       
for index in range(len(restaurant_name)):
    print(restaurant_name[index].get_text(), '\t', restaurant_rate[index].get_text())


