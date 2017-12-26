import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import tushare as ts

'''
这是将主要代码封装成函数形式的尝试。
在函数get_wt中仍然需要调整爬取数据的维度。
'''


def get_date(yr): # 使用函数形式封装的调用某一年天气方式，尚在调试。
    l1 = []
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
            
            timestamp = str(yr) + '-' + mStamp + '-' + dStamp
            # timestamp = str(yr) + str(m) + str(d)
                
            l1.append(timestamp)
    return(l1)
    
a = get_date(2015)+get_date(2016)+get_date(2017)

def get_hz(): # 使用函数形式封装的获得沪企指数方式
    df1 = ts.get_k_data(code = '000062', index = True)
    return(df1)
    
b = get(hz)
    
def get_wt(yr): # 使用函数形式封装的获得天气方式
    l2 = []
    for m in range(1, 13): # 获得天气数据的已有实现方案
        for d in range(1, 32):
            if (m == 2 and d > 28):
                break
            elif (m in [4,6,9,11] and d > 29):
                break
            url = 'https://www.wunderground.com/history/airport/ZSSS/'+ str(yr) + '/' + str(m) + '/' + str(d) + '/DailyHistory.html'
            page = urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'lxml')
            dayTemp = soup.findAll(attrs = {'class':'wx-data'})[1].span.string # 除了daytemp还有其他数据要爬，待实现。
            l2.append(dayTemp)
    return(l2)
    
c = get_wt(2015)
    
