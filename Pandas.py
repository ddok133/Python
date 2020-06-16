'''
# =============================================================================
#                              DATE : 20200615
# =============================================================================
'''


＊Pandas
    ＠專為 Python 編寫的外部模組，執行數據處理及分析。
    ＠主要資料結構：panel , dataframe , series 。 ＃ 這也是 pandas 的名稱由來。
    ＠Series
        1. 一維資料結構(類似二維)
        2. 可存放整數，浮點，字串，Python 物件...
        3. 類似 Python list , 具有索引結構。
        4. 建立 Series 物件
            -> pandas.Series(data , index , dtype , name...)
        5. 資料合併
            -> pandas.concat()
            -> concat 參數 axis 預設為0(預設的合併方式為直向合併)。
        6. axis = 1 ，設定欄位名稱
            -> Series資料.columns = 欄位名稱
        7. 以 name 參數指定columns
            -> Series資料.name = 名稱
                資料在concat時, 以名稱做為column名稱
            
            



'''
Exercise - Series
'''


1. 建立 Series

import pandas as pd
years = range(2020, 2023) # 設定年變數
beijing = pd.Series([20,21,19] , index = years) # 設定北京資料20,21,19 , 對應到索引 years。
hongkong = pd.Series([25,26,27] , index = years)
singapore = pd.Series([30,29,31] , index = years)

citytemp = pd.concat([beijing, hongkong, singapore])
print(type(citytemp))
print(citytemp)



2. concat 合併參數 asix 設定


import pandas as pd
years = range(2020, 2023) # 設定年變數
beijing = pd.Series([20,21,19] , index = years) # 設定北京資料20,21,19 , 對應到索引 years。
hongkong = pd.Series([25,26,27] , index = years)
singapore = pd.Series([30,29,31] , index = years)

citytemp = pd.concat([beijing, hongkong, singapore] , axis=1) # 設定合併方式axis ＝1
print(type(citytemp))
print(citytemp)



3. 加入 columns 資料欄位

import pandas as pd
years = range(2020, 2023) # 設定年變數
beijing = pd.Series([20,21,19] , index = years) # 設定北京資料20,21,19 , 對應到索引 years。
hongkong = pd.Series([25,26,27] , index = years)
singapore = pd.Series([30,29,31] , index = years)

citytemp = pd.concat([beijing, hongkong, singapore] , axis=1) # 設定合併方式axis ＝1
cities = ['Beihing' , 'HongKong' , 'Singapore'] # 設定欄位名稱
citytemp.columns = cities # 使用columns 設定欄位名稱
print(citytemp)



4. 設定 name 參數, 對應到欄位名稱

import pandas as pd
years = range(2020, 2023) # 設定年變數
beijing = pd.Series([20,21,19] , index = years) # 設定北京資料20,21,19 , 對應到索引 years。
hongkong = pd.Series([25,26,27] , index = years)
singapore = pd.Series([30,29,31] , index = years)

beijing.name = 'Beihing' # 設定 name , 就不需要使用 columns 參數設定欄位名稱。
hongkong.name = 'HongKong'
singapore.name = 'Singapore'
citytemp = pd.concat([beijing, hongkong, singapore] , axis=1) # 設定合併方式axis ＝1

print(citytemp)





    ＠DataFrame
        1. 為二維資料結構
        2. 可存放整數，浮點數，字串，Python物件...
        3. 建立 DataFrame 物件
            -> pandas.DataFrame(data , index , dtype , name...)
        4. DataFrame 的資料結構
            字典的串列 [{},{},{},...]
            字典的key若無對應，則對應處將填入'Nan'
        5. 以 index 參數設定row 名稱



'''
Exersise - dataFrame
'''

1. 字串裡的字典結構

import pandas as pd
data = [{'apple':50 , 'Orange':30 , 'Grape':80},{'apple':50 , 'Grape':30}]
fruits = pd.DataFrame(data)
print(fruits)




2. 字典結構

import pandas as pd
cities = {'country':['China','Japan','Singapore'] , 'town':['Beijing','Tokyo','Singapore'] ,
          'population':[2000,1600,600]}

citydf = pd.DataFrame(cities)
print(citydf)



3. 建立index 為row名稱

import pandas as pd
cities = {'country':['China','Japan','Singapore'] , 'town':['Beijing','Tokyo','Singapore'] ,
          'population':[2000,1600,600]}
index = ['1st' , '2nd' , '3rd']

citydf = pd.DataFrame(cities , index)
print(citydf)



4. 改變結構


import pandas as pd
cities = {'country':['China','Japan','Singapore'] , 'town':['Beijing','Tokyo','Singapore'] ,
          'population':[2000,1600,600]}

citydf = pd.DataFrame(cities , columns=['town' , 'population'] , index = cities['country'])
# 自己設定 columns and index
print(citydf)



or



import pandas as pd
cities = { 'town':['Beijing','Tokyo','Singapore'] ,'population':[2000,1600,600]}
index = ['China' , 'Japan' , 'Singapore']

citydf = pd.DataFrame(cities , index)
citydf.to_csv(r'/Users/martychen/Desktop/Python/out_c.csv')
print(citydf)



'''
Exercise - 用 Numpy 建立 DataFrame
'''

1. 

import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['X','Y','Z','S'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['X','Y','Z','S'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['X','Y','Z','S'])

print(df1)
print(df2)
print(df3)



2. 


import pandas as pd
import numpy as np

name = ['Frank' , 'Peter' , 'John']
score = ['1st' , '2nd' , 'final']

df = pd.DataFrame(np.random.randint(60,100,size=(3,3)),columns=name,index=score)
#  建立 3x3 陣列，每一格的數據在 60~99之間。
print(df)




    ＠寫入 CSV 檔
        CSV: Comma Separated Values
        1. 以 to_csv() 將 DataFrame 物件寫入 csv 檔
            -> to_csv(path , sep , header , index , encoding , ...)
                path : 檔案路徑
                sep : 分隔符號
                header : 是否保留header ,預設為True
                index : 是否保留index ,預設為True
                excoding : 檔案編碼



1. 

import pandas as pd

course = ['Chinese' , 'English' , 'Math' , 'Natural' , 'Society']
chinese = [14,12,13,10,13]
eng = [13,14,11,10,15]
math = [15,9,12,8,15]
nature = [15,10,13,10,15]
social = [12,11,14,9,14]

df = pd.DataFrame([chinese , eng , math , nature , social] , columns = course ,
                  index = range(1,6))
df.to_csv(r'/Users/martychen/Desktop/Python/out_a.csv')
df.to_csv(r'/Users/martychen/Desktop/Python/out_b.csv',header=False , index = False)
# 不顯示 columns and index





    ＠讀入 CSV 檔
        CSV: Comma Separated Values
        1. 以 read_csv() 將 csv 檔案讀入(也可讀取 txt 檔)
            -> read_csv(path , sep , header , encoding , index_col , usecols , nrows)
                path : 檔案路徑
                sep : 分隔符號
                header : 設定哪一個row為欄位名稱
                encoding : 檔案編碼
                index_col : 欄位 column 索引
                usecols : 讀取哪些欄位
                nrows : 讀取哪些列
                




1. 

import pandas as pd

course = ['1.Chinese' , '2.English' , '3.Math' , '4.Natural' , '5.Society']
x = pd.read_csv(r'/Users/martychen/Desktop/Python/out_a.csv' , index_col=0)
y = pd.read_csv(r'/Users/martychen/Desktop/Python/out_b.csv' , names=course)

print(x)
print(y)






    ＠繪圖
        1. 將數據建立為 Series ，以 Pandas 繪圖
        2. Pandas 繪圖使用 plot()方法
        3. 將數據建立為DataFrame以Pandas繪圖
    
    
    
    
1. 

import pandas as pd
import matplotlib.pyplot as plt

population = [860,1100,1450,1800,2020,2200,2260]
tw = pd.Series(population , index=range(1950,2011,10))
tw.plot(title='Population in Taiwan')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()




2. 曲線圖

import pandas as pd
import matplotlib.pyplot as plt


cities = {'population':[1000,850,800,1500,600,800],
          'town':['New York','Chicago','Bangkok','Tokyo','Singapore','HongKong']}
world = pd.DataFrame(cities, columns=['population'],index=cities['town'])

world.plot(title='Population in the World')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()






3. 柱狀圖

import pandas as pd
import matplotlib.pyplot as plt


cities = {'population':[1000,850,800,1500,600,800],
          'town':['New York','Chicago','Bangkok','Tokyo','Singapore','HongKong']}
world = pd.DataFrame(cities, columns=['population'],index=cities['town'])

world.plot(title='Population in the World',kind='bar') # kind 設定繪圖模式
plt.xlabel('City')
plt.ylabel('Population')
plt.show()


4. 兩個數據


import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[8399,2706,8281,9273,5639,7451],'area':[783,606,1569,622,721,1106],
          'town':['New York','Chicago','Bangkok','Tokyo','Singapore','HongKong']}
world = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])


world.plot(title='Population in the World')
plt.xlabel('City')
plt.show()



5. 人口數量實際化


import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[8399000,2706000,8281000,9273000,5639000,7451000],
          'area':[783,606,1569,622,721,1106],
          'town':['New York','Chicago','Bangkok','Tokyo','Singapore','HongKong']}
world = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])


world.plot(title='Population in the World')
plt.xlabel('City')
plt.show()




6. 改變比例


import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[8399000,2706000,8281000,9273000,5639000,7451000],
          'area':[783,606,1569,622,721,1106],
          'town':['New York','Chicago','Bangkok','Tokyo','Singapore','HongKong']}
world = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])

fig, ax = plt.subplots() 
fig.suptitle('City Statistics') # 標題
ax.set_ylabel('Population') # 設定y軸標題文字
ax.set_xlabel('City') # 設定x軸標題文字

ax2 = ax.twinx() # ax.twinx：產生一個新軸
ax2.set_ylabel('Area')
world['population'].plot(ax=ax,rot=45) # rot：旋轉座標刻度
world['area'].plot(ax=ax2, style='g') # style : 顏色
ax.legend(loc=1) # loc =1  左上
ax2.legend(loc=2) # loc =2  右上
plt.show()



# =============================================================================
# fig：整體圖表物件
# ax：第一個軸
# subplots：在一個圖表中繪製不同軸的數據
# =============================================================================


7. 圓餅圖

# =============================================================================
# 只能一組數據
# 數值格式化為百分比 autopct
# 切開圓形圖 explode
# =============================================================================


import pandas as pd
import matplotlib.pyplot as plt

fruits = ['Apples' , 'Bananas' , 'Grapes' , 'Pears' , 'Oranges']
s = pd.Series([2300,5000,1200,2500,2900], index=fruits,name='Fruits Shop')
explode = [0.4,0,0,0.2,0]
s.plot.pie(explode = explode, autopct= '%1.2f%%')
plt.show()










＊時間序列
    ＠數據由時間順序列出，時間為一系列的時間戳記。
        匯入時間模組
            from datetime import datetime
            
        1. 設定特定時間
            -> 時間變數 = datetime(年,月,日,時,分,秒)
            
        2. 時間區間
            -> 時間變數 = timedelta(weeks,days,hours,minutes,seconds)


Example:
    
from datetime import datetime
tn = datetime.now()
print(type(tn))
print('現在時間：',tn)




1. 


from datetime import datetime

timenow = datetime.now()

print(type(timenow))
print('Now:',timenow)
print('Year:',timenow.year)
print('Month:',timenow.month)
print('Day:',timenow.day)
print('Hour:',timenow.hour)
print('Min:',timenow.minute)
print('Sec:',timenow.second)




2.  timedelta 練習

import pandas as pd
from datetime import datetime

ndays = 5
start = datetime(2019,3,11)
dates = [start + timedelta(days=x) for x in range(0,ndays)]
data = [34,44,65,53,39]
ts = pd.Series(data, index=dates)
print(type(ts))
print(ts)



3. 兩組時間

import pandas as pd
from datetime import datetime

ndays = 5
start = datetime(2019,3,11,12,50,59)
dates = [start + timedelta(days=x) for x in range(0,ndays)]
data1 = [34,44,65,53,39]
ts1 = pd.Series(data1, index=dates)

data2 = [4,4,5,3,3]
ts2 = pd.Series(data2, index=dates)

addts = ts1 + ts2
print('ts1+ts2')
print(addts)

meants = (ts1 + ts2)/2
print('(ts1 + ts2)/2')
print(meants)



4. 

import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('3/11/2019' , '3/15/2019') # date_range(起始日期 , 終止日期)
data = [34,44,65,53,39]
ts = pd.Series(data, index = dates)
ts.plot(title='Data in Time Series')
plt.xlabel('Date')
plt.ylabel('Data')
plt.show()

















