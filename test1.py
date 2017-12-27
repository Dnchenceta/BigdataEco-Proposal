from bs4 import BeautifulSoup
import urllib.request
import re
from pandas import DataFrame

'''
这次是一个尝试，成功地获取了某一天的一共13类的数据，保存在了一个dataframe中。
接下来要做的是封装成为函数，希望能实现日期为横行的形式。
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
        
l3 = []
for each in l2:
    var = re.search('(\d+(\.\d+)?)', each)
    if var != None:
        var = var.group()
    else:
        var = 0
    l3.append(var)
    
data = {'items': l1, 'num': l3}
df = DataFrame(data)

# 应该转变为df.T的形式。
