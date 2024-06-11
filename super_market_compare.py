import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}

def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price

    laughs_content = requests.get(product_laughs).content
    soup_laughs = BeautifulSoup(laughs_content, 'html.parser')

    glomark_content = requests.get(product_glomark).content
    soup_glomark = BeautifulSoup(glomark_content, 'html.parser')

    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    l_price_tag = soup_laughs.find('div', class_='price-box')
    price_laughs = float(l_price_tag.text.strip()[3:])

    l_name_tag = soup_laughs.find('div', class_='product-name')
    product_name_laughs = l_name_tag.text.strip()
    

    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    g_script_tag = soup_glomark.find('script', {'type': 'application/ld+json'})
    g_json_data = json.loads(g_script_tag.string.strip())

    g_price_tag = g_json_data['offers'][0]
    price_glomark = float(g_price_tag["price"])

    product_name_glomark = g_json_data['name']
    
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')

