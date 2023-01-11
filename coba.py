from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
from csv import writer


url = "https://www.pararius.com/apartments/nederland/page-"
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

links = []
for i in range(1,66):
    sub_url = url+str(i)
    driver.get(sub_url)
    pages = driver.find_elements_by_class_name('listing-search-item__title')
    for page in pages:
        links.append(page.find_elements_by_class_name('listing-search-item__link--title')[0].get_attribute('href'))
with open('coba.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ["title", "price", "area","volume","type","year", "no_rooms","no_bed","no_bath","no_floor","balcony","garden", "interior"]
    thewriter.writerow(header)
    for link in links:
        driver.get(link)
        row = []
        sub = driver.find_elements(by=By.CLASS_NAME, value="listing-detail-summary__primary-information")
        title = sub[0].find_elements(by=By.CLASS_NAME, value="listing-detail-summary__title")[0].text
        row.append(title)
        attributes = [driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--for_rent_price'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--surface_area'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--volume'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--dwelling_type'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--construction_period'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--number_of_rooms'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--number_of_bedrooms'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--number_of_bathrooms'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--number_of_floors'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--balcony'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--garden'),
                        driver.find_elements(by=By.CLASS_NAME, value='listing-features__description--interior')]
        for attribute in attributes:
            if attribute != []:
                info = attribute[0].find_elements(by=By.CLASS_NAME, value="listing-features__main-description")[0].text
                row.append(info)
            else:
                row.append(np.nan)
        thewriter.writerow(row)


