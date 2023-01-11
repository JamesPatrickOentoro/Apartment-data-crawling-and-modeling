from urllib import response
from bs4 import BeautifulSoup
import requests
from csv import writer
import os
import re
import json

response = requests.get('https://www.pararius.com/apartments/nederland/page-')
soup = BeautifulSoup(response.text,"lxml")

scrapt_tag = soup.find("script",src=None)
pattern = "var data =(.+?);\n"
raw_data = re.findall(pattern, scrapt_tag.string, re.S)
print(raw_data)
if raw_data:
    data = json.loads(raw_data[0])
print(data)


# test_file = open(os.getcwd() + "/test.html")
# soup = BeautifulSoup(test_file)
# with open('coba.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = ['title', 'location', 'price', 'area', "no_rooms", "interior", "year"]
#     thewriter.writerow(header)
#     for page in range(1,66):
#         page = requests.get(url + str(page))
#         soup = BeautifulSoup(page.content, 'html.parser')
#         lists = soup.find_all('section', class_="listing-search-item")
#         for list in lists:
#             title = list.find('a', class_="listing-search-item__link--title")
#             location = list.find('div', class_="listing-search-item__sub-title")
#             new_link = list.find('a', class_="listing-search-item__link listing-search-item__link--title")['href']
#             new_page = requests.get(url)
#             soup = BeautifulSoup(new_page.content, 'html.parser')
#             print('masuk')
#             soupp = soup.find(class_="listing-features__description")
#             sub_p = soupp.find(class_="listing-features__description--for_rent_price")
#             print(sub_p)
#             price = sub_p.find('span', class_="listing-features__main-description")

#             sub_la = soup.find('dd', class_="listing-features__description listing-features__description--surface_area")
#             living_area = sub_la.find('span', class_="listing-features__main-description")

#             sub_v = soup.find('dd', class_="listing-features__description listing-features__description--volume")
#             volume = sub_v.find('span', class_="listing-features__main-description")

#             sub_t = soup.find('dd', class_="listing-features__description listing-features__description--dwelling_type")
#             type = sub_t.find('span', class_="listing-features__main-description")

#             sub_y = soup.find('dd', class_="listing-features__description listing-features__description--construction_period")
#             year = sub_y.find('span', class_="listing-features__main-description")

#             sub_r = soup.find('dd', class_="listing-features__description listing-features__description--number_of_rooms")
#             no_room = sub_r.find('span', class_="listing-features__main-description")

#             sub_b = soup.find('dd', class_="listing-features__description listing-features__description--number_of_bedrooms")
#             no_bed = sub_b.find('span', class_="listing-features__main-description")
            
#             sub_bth = soup.find('dd', class_="listing-features__description listing-features__description--number_of_bathrooms")
#             no_bath = sub_bth.find('span', class_="listing-features__main-description")

#             sub_floor = soup.find('dd', class_="listing-features__description listing-features__description--number_of_floors")
#             no_floor = sub_floor.find('span', class_="listing-features__main-description")

#             sub_balcon = soup.find('dd', class_="listing-features__description listing-features__description--balcony")
#             balcony = sub_balcon.find('span', class_="listing-features__main-description")

#             sub_g = soup.find('dd', class_="listing-features__description listing-features__description--garden")
#             garden = sub_g.find('span', class_="listing-features__main-description")

#             sub_i = soup.find('dd', class_="listing-features__description listing-features__description--interior")
#             interior = sub_i.find('span', class_="listing-features__main-description")

#             info = [title, location, price, interior, living_area, volume, type, year, no_room, no_bed, no_bath, no_floor, balcony, garden]
#             for i in range(len(info)):
#                 if info[i] != None:
#                     info[i] = info[i].text.replace('\n', '').replace(' ','')
#                 else:
#                     info[i]=None
#             thewriter.writerow(info)