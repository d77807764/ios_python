import requests
from bs4 import BeautifulSoup
import lxml
from xpinyin import Pinyin

p = Pinyin() 
a = "北京"
pinyin = p.get_pinyin(u"{}".format(a),'')

h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
url = 'http://tianqi.hao123.com/'+ pinyin + '.html'
content = requests.get(url, headers=h).content
soup = BeautifulSoup(content,'html5lib')
today = soup.findAll('div', class_='temp')[2].text
print(today)


