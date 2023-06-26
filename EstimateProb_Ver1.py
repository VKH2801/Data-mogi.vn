import requests
from bs4 import BeautifulSoup
import json

url = 'https://mogi.vn/gia-nha-dat'

# Gửi yêu cầu HTTP GET để tải trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu thành công hay không (status code 200 là thành công)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích cú pháp HTML của trang web
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Tìm các phần tử HTML chứa thông tin dữ liệu bạn muốn crawl
    # và trích xuất dữ liệu từ các phần tử đó
    districts_info_row  = soup.find_all('div', class_='mt-row clearfix')

    results = []
    for i, prob in enumerate(districts_info_row): 
        if i >= 24:
            break
        
        location_element = prob.find('a', class_='link-overlay')
        location = location_element.get_text(strip = True)
        span_element = prob.find('span')
        value = span_element.get_text(strip = True)
        sup_element = prob.find('sup', class_='change')
        percentage = sup_element.get_text(strip = True)

        item = {
            'District': location,
            'value': value,
            'ratio': percentage
        }

        results.append(item)

        
    with open('EstimateProb_Ver1.json', 'w', encoding='utf-8') as outfiles:
        json.dump(results, outfiles, ensure_ascii=False)

else:
    print('Failed to retrieve data from the website.')


