import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json


url='https://mogi.vn/gia-nha-dat-quan-2-qd367'


# Đường dẫn đến trình điều khiển ChromeDriver
webdriver_service = Service('path/to/chromedriver')

# Khởi tạo trình điều khiển Chrome
driver = webdriver.Chrome(service=webdriver_service)

# Mở trang web
driver.get(url)

driver.implicitly_wait(10)

html_content = driver.page_source

try:
    soup = BeautifulSoup(html_content, 'html.parser')
    type_elements = [i.text for i in soup.find_all('div', class_='mt-street')]
    price_elements = [i.text for i in soup.find_all('div', class_='mt-vol text-right number')]
except:
    print('Cannot connect to website:' + url)

driver.quit()

type = []
price = []
result = []
if type_elements is not None:
    
    for i in range(len(price_elements)):
        price.append(price_elements[i].replace('\n', ' ').strip())
            
    
    for i in range(len(type_elements)):
        type.append(type_elements[i].replace('\n', ' ').replace('\t', ' ').strip())
    
    type = [x for x in type if x not in ["Loại", "Đường"]]
    
    for i in range(len(type)):
        item = {
            'Type Property': type[i],
            'Value Property': price[i]
        }
        result.append(item)

    with open('District2_Estimate.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)
else:
    print('Cannot connected to website')


    