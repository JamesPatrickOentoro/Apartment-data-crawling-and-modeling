import requests
from bs4 import BeautifulSoup
import csv

key = 'hotel'
loc = 'surabaya'
url = 'https://www.tiket.com/{}/indonesia/city/{}-108001534490276270/page-'.format(key,loc)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34'
}

req = requests.get(url,headers=headers)
print(req)