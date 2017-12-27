from bs4 import BeautifulSoup
import urllib.request
import re

'''
这次是一个尝试，成功地获取了某一天的一共13类的数据，但是仍然储存在一个字符串列表中。
下一步需要考虑怎样从列表raw中获取数据。
'''

url = 'https://www.wunderground.com/history/airport/ZSPD/2017/12/26/DailyHistory.html'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'lxml')

indexs = soup.find_all(attrs = {'class':'indent'})
l1 = []
for index in indexs:
    ind = index.string.strip()
    l1.append(ind)
    
raw = soup.select('tr')
l2 = []
for each in raw:
    straw = str(each)
    if re.search('"indent"(.*)', straw) != None:
        l2.append(straw)
        
print(raw)
