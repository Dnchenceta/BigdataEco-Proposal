# -*- coding: utf-8 -*-

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
    return(temp_df)
    