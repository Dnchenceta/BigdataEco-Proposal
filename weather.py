import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

'''
使用的天气数据来自https://www.wunderground.com/，具体地点是上海浦东的机场，代码为ZSPD

具体实现要求的云层覆盖率(CC);温度(TEMP，单位:摄氏度);相对湿度(HUM);露点温度(DP，单位:摄氏度);
气压(PRE，单位:hPa);能见度(VIS，单位:公里);风速(WSP，单位:公里/小时);风向(WDIR)

先都爬下来吧，风向不做；云层覆盖率由晴与多云这样的，具体见文章。

使用的上证沪企指数sh000062数据来自tushare包的接口get_k_data
'''

l1 = []
l2 = []

for m in range(1, 13): # 获得天气数据的已有实现方案，待封装成函数
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
        l1.append(timestamp) # 生成时间戳
        print('Getting data for ' + timestamp) # 调试用
        url = 'https://www.wunderground.com/history/airport/ZSPD/2015/' + str(m) + '/' + str(d) + '/DailyHistory.html'
        page = urllib.request.urlopen(url)
      
        soup = BeautifulSoup(page, 'lxml') # 使用beautifulsoup解析页面
        dayTemp = soup.findAll(attrs = {'class':'wx-data'})[1].span.string # 得到日气温数据                
        l2.append(dayTemp)
    
    we_df = DataFrame({'date': l1, 'temp': l2})

import tushare as ts
df1 = ts.get_k_data(code = '000062', index = True) #获取sh000062数据

# 应该把两个数据生成dataframe，然后再用关系数据库或者python/R的处理方法整合，再进行建模回归。

