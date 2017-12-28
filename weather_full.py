# -*- coding: utf-8 -*-

'''
这次实现了函数形式的封装。
get_weather_bydate(date)实现获得某一天的天气数据，并保存在一个Series中。
get_date(yr)实现获得某一年每一天的日期（其实实现的复杂了一些，可以直接调用timestamp的）
get_weather(yr)使用上述两个函数获取某一年每一天的天气数据，保存在一个dataframe中。
未解决的问题是：
1. 数据清洗，有很多nan行与缺失数据行。
2. 数据结构改变，理想的结构应该是每一行日期对应各项天气变量的数值。（这个加个T就行了啊！
3. 关系数据，需要将天气数据与沪企指数数据整合起来。
'''

from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
from pandas import Series

def get_weather_bydate(date):
    url = 'https://www.wunderground.com/history/airport/ZSPD/'+ date +'/DailyHistory.html'
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
        
    df = Series(l3, index = l1)
    df.name = str(date)
    return(df)
    
def get_date(yr):
    l1 = []
    for m in range(1, 13): # 获得天气数据的已有实现方案
        for d in range(1, 32):
            if (m == 2 and d > 28):
                break
            elif (m in [4,6,9,11] and d > 30):
                break
            
            if len(str(m)) < 2:
                mStamp = '0' + str(m)
            else:
                mStamp = str(m)
            
            if len(str(d)) < 2:
                dStamp = '0' + str(d)
            else:
                dStamp = str(d)
            
            timestamp = str(yr) + '/' + mStamp + '/' + dStamp
            # timestamp = str(yr) + str(m) + str(d)
                
            l1.append(timestamp)
    return(l1)
    
def get_weather(yr):
    l0 = get_date(yr)
    for each in l0:
        temp = get_weather_bydate(each)
        if each == l0[0]:
            temp_df = temp
        else:
            temp_df = pd.concat([temp_df, temp], axis = 1)
        print(each, temp[0])
    temp_df = temp_df.T
    return(temp_df)
    
