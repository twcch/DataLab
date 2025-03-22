from bs4 import BeautifulSoup

import requests


job_title = '資料科學家'

url = f'https://www.104.com.tw/jobs/search/?jobsource=index_s&keyword={job_title}&mode=s&page=1'

req = requests.get(url)
res = req.text

soup = BeautifulSoup(res, 'html5lib')

div_1 = soup.find_all('div', class_='vue-recycle-scroller__item-wrapper')

for div in div_1:
    div_2 = div.find('h2')
    print(div_2)