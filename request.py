import requests
from bs4 import BeautifulSoup

URL = 'https://www.mercadolibre.com.co/ofertas#c_id=/home/promotions-recommendations&c_uid=c94e30b7-3651-4915-ad6d-d5f6773349a7'   
html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, "html.parser")
items= soup.find_all('li',{"class":"promotion-item avg"})
array_title = []
array_price = []
array_img = []
for item in items:
    try:
        href_item_img_info = item.find("img", class_="promotion-item__img")
        span_item_price = item.find("span", class_="andes-money-amount__fraction").getText()
        alt_item_title = href_item_img_info['alt']
        src_item_img = href_item_img_info['data-src']
        array_title.append(alt_item_title)
        array_price.append(span_item_price)
        array_img.append(src_item_img)
        print(src_item_img)
    except (KeyError, AttributeError) as e:
        print(f"Error al procesar un elemento: {e}")
        continue 
 


with open ('datos.xls','w') as f:
    for index in range(len(array_img)):
        f.write(array_title[index] + ';')
        f.write(array_price[index] + ';')
        f.write(array_img[index] + '\n')


