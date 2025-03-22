import requests


url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {'over18': '1'}
res = requests.get(url, cookies=cookies)
print(res.text)


