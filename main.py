from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_dkr=1&iconV2Request=true&_blrs=recall_filtering&_ssn=cache610&_sacat=15709&store_name=cache610llc&_oac=1'

s = HTMLSession()

r = s.get(url)

r.html.render(sleep = 1)



siteHtml = r.html.html
soup = BeautifulSoup(siteHtml,'lxml')


products = soup.find_all('li',class_ = 's-item s-item__pl-on-bottom')

product_list = []
for item in products:
    item_infos = item.find_all('div', class_ = 's-item__wrapper clearfix')[0]
    itemName = item_infos.find_all('div',class_ = 's-item__subtitle')[0].text
    item_details = item_infos.find_all('div', class_ = 's-item__details clearfix')[0]
    fullyName = item_infos.find_all('a',class_ = 's-item__link')[0]
    fullyName = fullyName.find_all('div',class_ = 's-item__title')[0].text

    item_details = item_details.find_all('div',class_ = 's-item__details-section--primary')[0]
    itemPrice = item_details.find_all('div',class_ = 's-item__detail s-item__detail--primary')[0].text
    itemPrice = itemPrice[1:].replace('.00','')
    itemPrice = itemPrice.replace('.99','')
    itemPrice = int(itemPrice)
    shoeProperties = {
        'Full_name': fullyName,
        'Subtitle' : itemName,
        'Price'    : itemPrice
    }
    product_list.append(shoeProperties)
df = pd.DataFrame(product_list)
df = df.sort_values('Price',ascending= False)
df.to_excel('shoes.xlsx')
df.to_csv('shoes.csv')



            
    
    



















