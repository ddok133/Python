＊鳶尾花資料集分析 Iris
    ＠數據分析中有名的資料集
    ＠為加州大學爾灣分校為機器學習(machine learning)之常用資料集
    ＠數據資料150筆，包含以下資料：
        1. 花瓣長度 petal length
        2. 花瓣寬度 petal width
        3. 花萼長度 sepal length
        4. 花萼寬度 sepal width
        5. 類別 species , setosa , versicolor , virginica

@step1 資料集iris.data並儲存為csv檔


import requests

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
try:
    htmlfile = requests.get(url)
    print('Download success')
except Exception as err:
    print('Download fail')

fn = '/Users/martychen/Desktop/Python/iris.csv'
with open(fn, 'wb') as fileobj:
    for diskstorage in htmlfile.iter_content(10240):
        size = fileobj.write(diskstorage)


@step2 讀取 csv 檔並轉換為DataFrame

import pandas as pd

colName = ['sepal_len' , 'sepal_wd' , 'pental_len' , 'petal_wd' , 'species']
iris = pd.read_csv(r'/Users/martychen/Desktop/Python/iris.csv', names = colName)
print('資料集長度：', len(iris))
print(iris)
s = iris.describe()
print(s)


@step3 資料視覺化

import pandas
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length' , 'sepal-width' , 'petal-length' , 'petal-width' , 'class']
dataset = pandas.read_csv(url, names=names)
print(dataset.describe())
dataset.hist()







