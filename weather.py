import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

l1 = []
l2 = []

for m in range(1, 13): # 获得天气数据的已有实现方案
    for d in range(1, 32):
        if (m == 2 and d > 28):
            break
        elif (m in [4,6,9,11] and d > 29):
            break
        
        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)
        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)
        timestamp = '2015' + mStamp + dStamp
        timestamp = '2015' + str(m) + str(d)
        l1.append(timestamp)
        print('Getting data for ' + timestamp)
        url = 'https://www.wunderground.com/history/airport/ZSSS/2015/' + str(m) + '/' + str(d) + '/DailyHistory.html'
        page = urllib.request.urlopen(url)
      
        soup = BeautifulSoup(page, 'lxml')
        dayTemp = soup.findAll(attrs = {'class':'wx-data'})[1].span.string
        l2.append(dayTemp)
    
    we_df = DataFrame({'date': l1, 'temp': l2})

import tushare as ts
df1 = ts.get_k_data(code = '000062', index = True) #获取sh000062数据

