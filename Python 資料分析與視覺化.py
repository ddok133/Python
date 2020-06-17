# =============================================================================
#                              DATE : 20200601
# =============================================================================


*** 網頁資料擷取與分析 ***
    ＠主題
        1. 資料處理
        2. 網頁資料擷取(必須會網頁結構或網頁設計 HTML5 , CSS3)與轉換
        3. 資料分析
        4. 資料視覺化
        5. 產出報告
        

    ＠Python第三方函式庫
        *Python 函式庫
            1. Python官方
            2. 協力廠商開發
            
    ＠jieba : 中文分詞函式庫
        *使用於中文自然語言處理(Nature Language Processing;NLP)
        *人工智慧應用，功用為：
            1. 分析文章主題
            2. 分析文章內容
            3. 文章分數關聯
            4. 作者撰寫習慣
        *步驟：
            1. 取得文章(注意版權)
            2. 將內容切割為一個個字詞
            3. 以 tf-idf 分析每個字詞的重要性
                tf:term freguency 字詞頻率(某字詞的出現次數/所有字詞出現次數的總和：字詞在文章中的重要性)
                
                idf:inverse document frequency 逆向檔案頻率(總文章數/某詞出現的文章數：越常出現的字詞越不重要)
        *安裝 Python 函式庫：以命令列 Anacouda Prompt 輸入指令 -> pip install jieba    

# Exercise==================================================================

# 讀取文章，找出最重要的字詞
# -> jieba.analyse.extract_tags(文章 , 提取分析權重最大值的字詞（依據tf-idf）傳回的數量（預設20）)

# =============================================================================

1. 
import jieba
import jieba.analyse
f = open(r'/Users/martychen/Documents/Python/article.txt' , 'r' , encoding = 'utf-8')
article = f.read()
tags = jieba.analyse.extract_tags(article,5) # 抓取 10 個最重要的字詞
print('最重要字詞：', tags)









＊＊＊ open data:開放資料 ＊＊＊
    ＠建議格式：JSON , XML , 試算表 (MS Excel) , CSV(以透號分隔的) , 文書(PDF , Word , ODF) , 純文字(*.txt)



＊ HTML 轉 PDF
    pdfkit
        1. 安裝函式庫 pdfkit
        2. 安裝 wkhtmltopdf
            -> pdfkit.from_url(網址 , 轉存的pdf檔 , 組態（執行的wkhtmltopdf程式）) ＃將網頁轉存PDF檔
            -> pdfkit.from_string(字串 , 轉存的pdf檔 , 組態) ＃將字串轉存PDF檔
            -> pdfkit.from_file(檔案 , 轉存的pdf檔 , 組態) ＃將檔案轉存PDF檔
    



# Exercise================================================================
import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r'/usr/local/bin/wkhtmltopdf')

pdfkit.from_file('/Users/martychen/Documents/Python/test.html', r'/Users/martychen/Documents/Python/out4.pdf' , configuration=config)
pdfkit.from_url('https://tw.yahoo.com/', r'/Users/martychen/Documents/Python/out1.pdf' , configuration=config)
pdfkit.from_string('Hello World!', r'/Users/martychen/Documents/Python/out2.pdf' ,configuration=config)
pdfkit.from_file('/Users/martychen/Documents/Python/CSF.html',r'/Users/martychen/Documents/Python/out3.pdf' , configuration=config)







*** HTML 語法架構 ***
<html>

<head>    </head>

<body>

    <table>
       <tr>
           <td>
           <td>
           <td>
           <td>
       </tr>
       <tr>
           <td>
           <td>
           <td>
           <td>
       </tr>
       <tr>
           <td>
           <td>
           <td>
           <td>
       </tr>
       
         
    </table>


</bopdy>
</html>







＊ HTML 轉 PDF
    pypdf2:
        1. 安裝函式庫 pypdf2
        2. 執行pdf寫入,讀取,合併,分割....
             
        -> PdfFileReader(PDF檔案)：讀取PDF檔案
        -> PDF物件.getDocumentInfo():取得頁面資訊
        -> PDF物件.getPageLayout():取得頁面配置
        -> PDF物件.getPageMode():取得頁面模式
        -> PDF物件.getXmpMeTadate():取得檢索資料
        -> PDF物件.getNumPages():取得頁數          
        -> PdfFileWriter(物件).addPage(寫入的頁面)# PageObj : 加入每一頁
        -> PdfFileReader(物件).getPage(頁面索引)＃ 取得頁面(每一頁)PageObj
        -> PdfFileWriter(物件).write(寫入的檔案) # 將加入的每一頁寫到檔案
        -> PdfFileWriter(物件).addBlankPage() # 加入空白頁



# Exercise================================================================

1. 取得PDF 檔案資訊

from PyPDF2 import PdfFileReader , PdfFileWriter #import PyPDF2
pdffile = r'/Users/martychen/Documents/Python/water.pdf'

pfr = PdfFileReader(pdffile)

documentInfo = pfr.getDocumentInfo()

print('documentInfo = %s' % documentInfo)

pageLayout = pfr.getPageLayout()

print('pagelayout = %s' % pageLayout)

pagemode = pfr.getPageMode()

print('pagemode = %s' % pagemode)

xmpmetadata = pfr.getXmpMetadata()

print('xmpmetadata = %s' % xmpmetadata)

pagecount = pfr.getNumPages()

print('pagecount = %s' % pagecount)




2. 增加PDF檔案頁面

from PyPDF2 import PdfFileReader , PdfFileWriter #import PyPDF2
pdffile = r'/Users/martychen/Documents/Python/health.pdf'
#設定檔案來源為 pdffile 變數
pfr = PdfFileReader(pdffile,strict=False)
#讀取檔案並設定給 pfr 變數
documentInfo = pfr.getDocumentInfo()
#取得檔案資訊並設定給 documentInfo 變數
outfile = r'/Users/martychen/Documents/Python/health_output.pdf'
#設定輸出檔案名稱為 outfile 變數
pfw = PdfFileWriter()
#將檔案寫入方法設定給 pfw 變數
numPages = pfr.getNumPages()
for index in range(0,numPages):
    pageObj = pfr.getPage(index)
    
    pfw.addPage(pageObj)
    pfw.write(open(outfile , 'wb'))

pfw.addBlankPage()
pfw.write(open(outfile , 'wb'))



# =============================================================================
#                              DATE : 20200603
# =============================================================================






3. 分割PDF檔案

from PyPDF2 import PdfFileReader , PdfFileWriter #import PyPDF2
pdfFile = r'/Users/martychen/Documents/Python/health.pdf'
#設定檔案來源為 pdfFile 變數
pfr = PdfFileReader(pdfFile,strict=False)
#讀取檔案並設定給 pfr 變數
documentInfo = pfr.getDocumentInfo()
#取得檔案資訊並設定給 documentInfo 變數
outFile = r'/Users/martychen/Documents/Python/health_cut.pdf'
#設定輸出檔案名稱為 outFile 變數
pfw = PdfFileWriter()
#將檔案寫入方法設定給 pfw 變數
numPages = pfr.getNumPages()
#讀取檔案頁數並設定給 numPages 變數
if numPages > 3: #若是頁數大於 3 
    
    for index in range(3, numPages): #則將頁數帶入迴圈，從3開始到最後的頁數
        pageObj = pfr.getPage(index) #以迴圈每一圈的index值取得該頁並設定給pageObj變數
        pfw.addPage(pageObj) #將取得的頁面加入
        
    pfw.write(open(outFile, 'wb')) #將所有加入的頁面寫入輸出檔案
    
    
    

    
    





4. 合併 PDF 檔案

import PyPDF2
pdfFiles = [r'/Users/martychen/Documents/Python/out1.pdf', 
            r'/Users/martychen/Documents/Python/out2.pdf' ,
            r'/Users/martychen/Documents/Python/out3.pdf'] 
#設定檔案來源為 pdfFile 變數 #設定要讀取的檔案
pdfWriter = PyPDF2.PdfFileWriter() #將檔案寫入方法設定給 pdfWriter 變數 # pdfWriter = PdfFileWriter()
pdfOutput = open(r'/Users/martychen/Documents/Python/comb.pdf' , 'wb')
#以寫入模式開啟檔案comb.pdf，若不存在則建立，並設定給 pdfOutput 變數(輸出檔案)
for fileName in pdfFiles: #以檔案名稱做為迴圈的執行參數fileName 
    pdfReader = PyPDF2.PdfFileReader(open(fileName,'rb')) #以讀取模式開啟檔案並設定給 pdfReader  變數
    for pageNum in range(pdfReader.numPages): #以開啟的檔案頁數作為迴圈執行的次數
        print(pdfReader.getPage(pageNum)) #將讀取的頁面印出
        pdfWriter.addPage(pdfReader.getPage(pageNum)) #將讀取的頁面加入
pdfWriter.write(pdfOutput) #將所有加入的頁面寫入輸出檔案
pdfOutput.close() #關閉寫入後的檔案
    






＊＊＊ 讀取/寫入 txt 檔案 ＊＊＊

 -> math.ceil(數值) : 取得大於或等於該數值得最小整數
 -> math.floor(數值) : 取得小於或等於該數值得最大整數


1. 讀取

f = open(r'/Users/martychen/Documents/Python/score.txt') #開啟檔案(唯讀)
a = f.read() #以 read()方法讀取 f 並設定給變數a
l = a.split() #以 split() 方法分割資料成為一個串列 l，串列中的資料為整數字串
for i in range(0,len(l)): #以串列資料做為迴圈執行的次數
    l[i] = int(l[i]) #以索引帶入串列l中取得每一個元素並轉成整數後設定回給元素自己
# 分類統計個級別人數到列表 c
c = [0,0,0,0,0,0]
for x in l: #以串列l中的元素作為迴圈執行依據
    if x >=90: #若串列l元素>=90，則將串列c的第一個元素值加1
        c[0] += 1
    elif x >= 80: #若串列l元素>=80，則將串列c的第二個元素值加1
        c[1] += 1
    elif x >= 70: #若串列l元素>=70，則將串列c的第二個元素值加1
        c[2] += 1
    elif x >= 60: #若串列l元素>=60，則將串列c的第二個元素值加1
        c[3] += 1
    elif x >= 40: #若串列l元素>=40，則將串列c的第二個元素值加1
        c[4] += 1
    else:         #其餘則將串列c的第六個元素值加1
        c[5] += 1
# 輸出各級別統計結果
print('90 分以上 %d 人' % c[0])
print('89-80 分 %d 人' % c[1])
print('79-70 分 %d 人' % c[2])
print('69-60 分 %d 人' % c[3])
print('59-40 分 %d 人' % c[4])
print('39 分以下 %d 人' % c[5])




2. 寫入

import math #載入數學模組
with open(r'/Users/martychen/Documents/Python/data5.txt' , 'r') as fin:
#以讀取模式開啟data5.txt設定給變數fin
    with open(r'/Users/martychen/Documents/Python/data5_w.txt' , 'w') as fout:
    #以寫入模式開啟data5.txt設定給變數fout
        for line in fin: #以讀取的檔案作為迴圈執行依據，逐一讀取data5.txt的資料
            data = math.ceil(20/(float(line)*0.001425))
            #執行數學模組的ceil()方法：取得大於或等於該數值得最小整數，運算後設定給data變數
            print('每股價格：%5.2f, 每日需購股數：%5.0f' % (float(line),data))
            fout.write(str(data)+'\n')
            #將data寫入fout
            


 
    

＊＊＊ 讀取/寫入 CSV 檔案 ＊＊＊


1. ubike數據
import csv #載入csv套件
with open(r'/Users/martychen/Documents/Python/ubike_1.csv' , 'r' , encoding = 'utf8') as csvfile:
#以讀取模式開啟CSV檔並設定給變數 csvfile
    
    #delimiter指定分割字元
    plots = csv.reader(csvfile,delimiter=',')
    #以reader方法讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    #並設定給變數plots(為串列物件)
    for row in plots:
        print(row[0]+' '+row[1]+' '+row[3]+' '+row[5]+' '+row[12])
        #每一個欄位(row)以索引取出該欄位資料
        


2. 空氣品質數據
import csv
with open(r'/Users/martychen/Desktop/Python/air.csv' , 'r' , encoding = 'utf8') as csvfile:
#以讀取模式開啟CSV檔並設定給變數 csvfile
    
    #delimiter指定分割字元
    plots = csv.reader(csvfile,delimiter=',')
    #以reader方法讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    #並設定給變數plots(為串列物件)
    for row in plots:
        print(row[0]+' '+row[2]+' '+row[3])
        #每一個欄位(row)以索引取出該欄位資料



3. 

import csv #載入csv套件
with open(r'/Users/martychen/Desktop/Python/stock.csv' , 'r') as fin:
#以讀取模式開啟檔案stock.csv並設定為變數fin
    with open(r'/Users/martychen/Desktop/Python/stock_out.csv' , 'w') as fout:
    #以寫入模式開啟檔案stock_out.csv，若檔案不存在則建立，並設定為變數out
        csvreader = csv.reader(fin,delimiter=',')
        #以csv套件的reader方法將檔案fin讀入並設定給變數csvreader(為一個讀取物件)
        csvwriter = csv.writer(fout,delimiter=',')
        #以csv套件的writer方法將寫入檔案fout並設定給變數csvwriter(為一個寫入物件)
        header = next(csvreader) #取得讀取資料的表頭設定給變數header
        print(header) #印出表頭
        csvwriter.writerow(header) #將表頭寫入檔案
        for row in csvreader: #以迴圈逐行讀取資料
            row[6] = row[6].replace('/', '-') #將每一行日期字串中的 / 改為 -
            print(','.join(row)) #使用join()方法將字串合併並印出
            csvwriter.writerow(row) #以寫入物件利用writerow()方法將每列資料寫入
            
            

＊＊＊ 讀取 JSON 檔案 ＊＊＊



#JSON：JavaScritp Object Notation
→JavaScript 開放資料交換格式
→JSON 為JavaScript程式的一個子集合

    ＠JSON型態轉換到Python型態的對照：
        object→dict
        array→list
        string→unicode
        number(int)→int,long
        number(real)→float
        true→True
        false→False
        null→None

    ＠資料格式如下：
        menu = \
            {
            "breakfast" : {
                "hours": "7-10",
                "items": {
                "breakfast burritos": "$60",
                "pancakes": "$35"
                }
                    },
            "lunch" : {
                .....
                }
                    },
            "dinner" : {
                .....
                }
                    }
            }
       
    

    -> separators(item符號(數組),dict符號(字典))
    

 
1. json 格式練習       
import json #載入JSON套件
print(json.dumps(['two' , {'bar':('jaz' , None , 2.0 ,1)}]))
print(json.dumps('\two\bar'))
print(json.dumps('\u4321'))
print(json.dumps('\\'))
print(json.dumps({'c':0,'b':0,'d':0},sort_keys=True))
print(json.dumps([0,1,2,3,{'4':5,'6':7}],separators=(',',':')))
print(json.dumps({'4':5,'6':7},sort_keys=True,indent=3))
#json.dumps()：將Python中的文件序列化為json格式字串
#json.loads()：為json.dumps()的反向，將已編碼的json字串解碼為Python物件
d1 = {'b':789,'c':456,'a':123}
d2 = json.dumps(d1,sort_keys = True , indent = 4)
print(d2)
    
    
    
2. 讀取 json檔案

import json #載入JSON套件
with open(r'/Users/martychen/Desktop/Python/ubike_1.json' , encoding = 'utf8') as file: 
#開啟JSON檔並設定給變數file
    data = json.load(file)
    #執行load()方法將JSON檔案解碼為Python物件，並設定給data變數
    for item in data:
        print([item['sno'],item['sna'],item['tot']])
        #以索引列印item各欄位資料
    
    





＊＊＊ XML 檔案 ＊＊＊

    @XML：eXtensible Markup Language；可延伸標記語言
        →是一種電腦標記語言
        →規則特性：
        →是一種標籤語法
        →以<名稱>開頭，後面接一段內容，再以</名稱>結尾。
        →忽略空格
        →<名稱>下可能有<子名稱>，層層結構。
        →<名稱>可稱為一個節點
        →<名稱 屬性=屬性值>：代表該名稱的設定功能
        →通常用於資料傳遞與消息發佈，如RSS....，一般業界會自訂客製化的XML格式。

1. 
import xml.etree.ElementTree as et #載入xml.etree.ElementTree套件
tree = et.ElementTree(file = r'/Users/martychen/Desktop/Python/menu.xml')
#讀取XML檔，儲存到 tree 變數
root = tree.getroot() #取得根節點(即XML標籤)

print(root.tag) #輸出根節點(menu標籤名)
for child in root: #(menu標籤下的子標籤)
    print('tag:' , child.tag , 'attributes:' , child.attrib)
    #tag：取得標籤、attrib：取得標籤屬性
    for grandchild in child: #子標籤下的子標籤
        print('\ttag' , grandchild.tag , 'attributes:' , grandchild.attrib)
print(len(root)) # 菜單選項的數目
print(len(root[0])) # 早餐選項的數目



2. 讀取 HML 檔案

# =============================================================================
# #每個 Element (元素；標籤)有以下的特性：
# 	#tag(標籤)
# 	#attributes(屬性)
# 	#text(文字)

    -> Element.iter(目標)
        尋找所有元素內符合目標值的項目
        尋找符合所有目標的tag
# =============================================================================
import xml.etree.ElementTree as ET #載入 xml.etree.ElementTree 套件

tree = ET.parse(r'/Users/martychen/Desktop/Python/country_data.xml')
#以parse讀取解析XML檔案
root = tree.getroot() #取得根節點
print('coutry_data.xml的根節點：' + root.tag) #輸出根節點(標籤名)
print('根節點標籤裡的屬性和屬性值:' + str(root.attrib)) #輸出根節點的屬性與屬性值

for child in root: #以迴圈取得子節點標籤、屬性、屬性值
    print(child.tag, child.attrib)
    
print('排名:'+root[0][0].text , '國內生產總額:'+root[0][2].text,)
#以 text 輸出 country 標籤下的子標籤內容

for neighbor in root.iter('neighbor'): #以迴圈取得 neighbor 標籤屬性與屬性值
    print(neighbor.attrib)
    
for country in root.findall('country'): #以 findall() 方法取得根節點下的子節點標籤中符合的標籤取出顯示
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)










# =============================================================================
#                              DATE : 20200604
# =============================================================================





3. 寫入 HML檔案

import xml.etree.ElementTree as ET #載入 xml.etree.ElementTree 套件

tree = ET.parse(r'/Users/martychen/Desktop/Python/country_data.xml')
#以parse讀取解析XML檔案
root = tree.getroot() #取得根節點

for rank in root.iter('rank'): #以迴圈取得<root>節點下符合rank的節點，執行修改 rank 標籤
    new_rank = int(rank.text)+1 #設定 rank 標籤顯示的文字轉換為整數後 + 1，並設定給變數new_rank
    rank.text=str(new_rank) #將加 1 後的顯示文字轉換為字串，並設定給變數rank.text
    rank.set('updated', 'yes')
    #以set()方法設定 rank 標籤的屬性、屬性值
    #Element.set(屬性 , 屬性值)：設定元素的屬性、屬性值
    
tree.write(r'/Users/martychen/Desktop/Python/country_data_output.xml' , encoding='utf-8')   
#利用write()方法寫入 XML 資料
    
    
    
4. 

import xml.etree.ElementTree as ET #載入 xml.etree.ElementTree 套件

tree = ET.parse(r'/Users/martychen/Desktop/Python/country_data.xml')
#以parse讀取解析XML檔案
root = tree.getroot() #取得根節點

for country in root.findall('country'): 
#以 findall() 方法取得根節點下的子節點標籤中符合country的標籤取出
#再以迴圈執行根節點下所有 country 標籤
    rank=int(country.find('rank').text) 
    #以find()方法尋找 country 標籤下的子節點 rank 標籤的文字並轉換為整數
    
    if rank>50: #若 rank 標籤顯示文字大於 50
        #則使用 remove() 方法移除根節點下的 country 標籤
        root.remove(country)
        
tree.write(r'/Users/martychen/Desktop/Python/country_data_output01.xml' , encoding='utf-8')   
#利用write()方法寫入 XML 資料





'''
* SQL 資料庫
    @SQLite：
    →是包含在一個相對小的C程式庫中的關聯式資料庫管理系統。
    →不是一個用戶端/伺服器端結構的資料庫引擎。
    →被整合在用戶程式中，使用動態的SQL語法操作。
    →特性：
        →支援交易ACID(單一性、一致性、孤立性、耐久性)
        →無需設定與管理，因此若要管理，需要搭配第三方套件所提供的工具。
        →支援ANSI-SQL92語法(資料庫查詢語言標準)
        →資料庫系統是一個檔案。
        →檔案大小最大支援到2TB。
        →記憶體需求小：原始程式採用不到30000行的C語言撰寫，僅需要小於250KB的程式空間。
        →免費使用。
        →使用 unicode。

    @Python使用sqlite3模組(2.5版以上已內建)
    →使用方法：
        →sqlite3.connect(路徑)：開啟資料庫的連結，成功開啟則傳回一個連線物件。
        →sqlite3.cursor()：建立cursor(資料指標)
        →sqlite3.execute()：執行SQL語法
        →sqlite3.commit()：提交目前的交易(執行資料庫的操作)
        →sqlite3.rollback()：回復上一次呼叫commit()對資料庫的更改。
        →sqlite3.close()：關閉資料庫連結。

'''

1. 
import sqlite3 #載入 sqlite3 模組

conn = sqlite3.connect(r'/Users/martychen/Desktop/Python/test.db')
print('Opened database successfully')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案

c = conn.cursor() #建立 cursor(游標物件) 供資料庫後續操作

#執行 SQL 指令
#建立資料表(create table)
c.execute('''CREATE TABLE COMPANY1
          (ID INT PRIMARY KEY NOT NULL,
          NAME TEXT NOT NULL,
          AGE INT NOT NULL,
          ADDRESS CHAR(50),
          SALARY REAL);''')
print('Table created successfully')



conn.commit() #執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令

conn.close() #關閉資料庫(不會自動呼叫 commit())


2. 新增資料

import sqlite3 #載入 sqlite3 模組

conn = sqlite3.connect(r'/Users/martychen/Desktop/Python/test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor() #建立 cursor(游標物件) 供資料庫後續操作
print('Opened database successfully')

#執行 SQL 指令
#新增記錄(insert into) 
c.execute('INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES (1,"Paul",32,"California",20000.00)');
c.execute('INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES (2,"Allen",25,"Texas",15000.00)');
c.execute('INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES (3,"Teddy",23,"Norway",20000.00)');
c.execute('INSERT INTO COMPANY1 (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES (4,"Mark",25,"Rich-Mond",65000.00)');
         


conn.commit() #執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
print('Records created syccessfullu')
conn.close() #關閉資料庫(不會自動呼叫 commit())

          
 3. 查詢資料

import sqlite3 #載入 sqlite3 模組

conn = sqlite3.connect(r'/Users/martychen/Desktop/Python/test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor() #建立 cursor(游標物件) 供資料庫後續操作
print('Opened database successfully')        
  
#執行 SQL 指令
#查詢記錄(select)       
cursor = c.execute('SELECT id, name , address , salary from COMPANY1')
#以 cursor 物件c 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
for row in cursor: #以迴圈將查詢結果 cursor 中每一筆記錄取出(row物件)，
    print('ID = ' , row[0]) #再以索引將記錄的欄位資料取得後設定給對應的變數。
    print('NAME = ' , row[1])
    print('ADDRESS = ' , row[2])
    print('SALARY = ' , row[3],'\n')


#再以索引將記錄的欄位資料取得後設定給對應的變數。
    
print('Operation done successfully')
conn.close()


4. 更新修改


import sqlite3 #載入 sqlite3 模組

conn = sqlite3.connect(r'/Users/martychen/Desktop/Python/test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor() #建立 cursor(游標物件) 供資料庫後續操作
print('Opened database successfully')        

#執行 SQL 指令
#更新記錄(update set)
c.execute('UPDATE COMPANY set SALARY = 25000.00 where ID=1')
conn.commit() #執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
print('Total number of rows updated :' , conn.total_changes)
#conn.total_changes：取得資料庫改變(修改、新增)的總次數。

#執行 SQL 指令
#更新記錄(select)
cursor = conn.execute('SELECT id , name , address , salary from COMPANY')
#以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
for row in cursor: #以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
    print('ID = ' , row[0]) #再以索引將記錄的欄位資料取得後顯示。
    print('NAME = ' , row[1])
    print('ADDRESS = ' , row[2])
    print('SALARY = ' , row[3],'\n')    
print('Operation done successfully')
conn.close()#關閉資料庫(不會自動呼叫 commit())
    
    
    
5. 刪除


import sqlite3 #載入 sqlite3 模組

conn = sqlite3.connect(r'/Users/martychen/Desktop/Python/test.db')
#建立資料庫檔案的連結並開啟，如果開啟成功便建立一個連線物件
#如果檔案不存在則建立檔案
c = conn.cursor() #建立 cursor(游標物件) 供資料庫後續操作
print('Opened database successfully')        

#執行 SQL 指令
#刪除記錄(delete)
c.execute('DELETE from COMPANY1 where ID=2;')
conn.commit() #執行資料庫的所有操作(執行交易)，即資料庫操作動作與指令
print('Total number of rows deleted :' , conn.total_changes)
#conn.total_changes：取得資料庫改變(修改、新增)的總次數。

#執行 SQL 指令
#更新記錄(select)
cursor = conn.execute('SELECT id , name , address , salary from COMPANY')
#以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
for row in cursor: #以連線物件 conn 執行 SQL 查詢指令後，得到查詢結果，設定給變數 cursor
    print('ID = ' , row[0]) #再以索引將記錄的欄位資料取得後顯示。
    print('NAME = ' , row[1])
    print('ADDRESS = ' , row[2])
    print('SALARY = ' , row[3],'\n')   
print('Operation done successfully')
conn.close()#關閉資料庫(不會自動呼叫 commit())    
    
    
    
'''
* SUMMARY
    ＠資料處理
        資料檔格式以 *.csv , *.xml , *.json 為主。
        讀取/寫入為基礎操作。
'''








'''
* 網頁資料擷取,轉換
    ＠Python擷取網頁的流程：
        1. 存取網站取得內容
        2. 解析取得的內容
        3. 處理資料(分析，視覺化)
        

    ＠Python取得網頁資料
        1. 靜態網頁資料
            - 網站中不含*.js檔
            - 伺服器回傳的是一整個網頁
            - 靜態網頁：解析 HTML 檔案
            - HTML 網頁架構:標籤(Tag)，屬性(attribute)，內容(content)
            - HTML 標籤結構：
                <標籤名 屬性...>內容</標籤>
            - 常用標籤：
                <header> 表頭 , <title> 標題, <body> 網頁主體 , <div> 區塊 ,
                <h1> 標題文字第一級 , <a href> 超連結 , <form> 表單 , <tr><td> 表格列/表格欄
            - 常用屬性:
                id 網頁識別
                class 元素分類
                href 超連結
        2. 動態網頁資料
        

    ＠BeautifulSoup 網頁資料分析與擷取(網頁解析)
        官方：html.parser
        第三方：lxml , xml , html5lib
        -> BeautifulSoup物件＝BeautifulSoup(網頁原始碼 , 'html.parser')
        
        
        ＊find():傳回第一個符合的標籤內容，傳回值為一字串。
        ＊fond_all():傳回所有符合的標籤內容，傳回值為串列。
                -> find or fond_all(標籤名稱,{屬性名稱：屬性值})  
                                        ＃字典型別
                                        
        ＊select(): 以CSS選擇器的方式讀取指定的資料，傳回值為串列。
            1. 讀取 CSS id:必須於 id 前加上#
                如 <div id = 'first'> 內容 </div>
                    -> data = BeautifulSoup物件.select('#first')
            2. 讀取 CSS 類別：必須於類別前加上 .
                如 <p class='second'> 內容 </p>
                    -> data = BeautifulSoup物件.select('.second')
            3. 多層標籤: 逐層依序寫出
                如 <html><head><title> 內容 </title></head></html>
                    -> data = BeautifulSoup物件.select('html head title')
                 
        
        
    ＠urllib
        使用urllib.request 的urlopen方法取得遠端網頁，再使用read()方法讀取內容。
        
        
        
    ＠讀取網站檔案：requests
        發送 GET 請求
            1. 瀏覽器輸入網址，再由伺服器回應到使用者端。
            2.requests 可不經過瀏覽器發送 GET 直接存取網頁。
        -> import requests
           變數 = requests.get(網址)
           

    ＠session / cookie
        client 拜訪-> Server
        Server 產生憑證(識別用)發給-> client
        儲存在 client 端的 browser, 即為 cookie
        儲存在 Server 端的, 即為 session
        
        建立 session: 身分認證通常是搭配 session 使用。
            -> requests.Session()
            
        網頁擷取(在身分認證頁面)：
            建立 session 以 post 方式帶入參數登入，再使用 cookie 帶入參數進入頁面。




'''

＠＠＠！！！爬蟲練習 台灣銀行匯率

import csv #載入 csv 模組，處理csv檔案格式
import requests #載入 requests 模組，存取網站取得內容
from bs4 import BeautifulSoup #載入 BeautifulSoup 模組，解析網頁。
# BeautifulSoup讀取 HTML 原始碼，自動進行解析並產生一個 BeautifulSoup 物件，此物件中包含了整個 HTML 文件的結構。
from time import localtime , strftime , strptime , mktime #處理時間系列
from datetime import datetime #處理日期時間
from os.path import exists #處理檔案儲存路徑、查看特定的路徑是否存在，不分檔案或目錄

html = requests.get('https://rate.bot.com.tw/xrt?lang=zh-Tw') #取得網站內容
# -> request.get(網址)
bsObj = BeautifulSoup(html.content, 'lxml') #將取得的網站內容分析並建立物件bsObj
# bsObj 是經過分析後的網站樹狀結構。

#靜態網頁中的資訊結構為table→tbody→tr，很多tr，故使用findall找出所有tr
for single_tr in bsObj.find('table' , {'title':'牌告匯率'}).find('tbody').findAll('tr'):
    #findall找出所有的td儲存到cell
    cell = single_tr.findAll('td')
    #在cell[0]下找到class屬性是visible-phone的欄位
    #以contents回傳欄位內容給currency_name(匯率名稱)
    currency_name = cell[0].find('div',{'class':'visible-phone'}).contents[0]
    #刪除表格中不必要的資料如\r , \n , 空白鍵
    currency_name = currency_name.replace('\r','')
    currency_name = currency_name.replace('\n','')
    currency_name = currency_name.replace(' ','')
    #以contents回傳欄位內容給currency_rate(匯率)
    currency_rate = cell[2].contents[0]
    print(currency_name, currency_rate)
    #建立csv檔案
    file_name = r'/Users/martychen/Desktop/Python/bkt_rate' + currency_name + '.csv'
    #取得目前時間
    now_time = strftime('%Y-%m-%d %H:%M:%S' , localtime())
    
    #寫入csv檔，如果檔案不存在，則抓取網頁上的時間及匯率寫入，若檔案存在，即使用原資料
    #如果檔案不存在，加入一行資料，以串列中的串列處理每天的匯率資料。
    #每一個串列代表擷取得每一筆匯率資料。
    if not exists(file_name):
        data = [['時間' , '匯率'] , [now_time , currency_rate]] # data 是二維串列
    else:
        data = [[now_time,currency_rate]]
    f = open(file_name,'a') #開啟csv檔
    w = csv.writer(f) #寫入csv檔
    w.writerows(data) #寫入data物件
    f.close()  #關閉csv檔案
    
    
    
    
    
    

# Homework=====================================================================
# 前往環保署下載「細懸浮微粒資料PM2.5」
# 共分三種格式 JSON , CSV , XML。 
# 請分別寫出三種Python程式，將PM2.5讀出，觀察各地測站的PM2.5的偵測值。
# =============================================================================



import csv
with open(r'/Users/martychen/Desktop/Python/pm25tw.csv' , 'r' , encoding = 'utf8') as csvfile:
#以讀取模式開啟CSV檔並設定給變數 csvfile
    
    #delimiter指定分割字元
    plots = csv.reader(csvfile,delimiter=',')
    #以reader方法讀取CSV檔案，每一列資料以delimiter設定資料的分隔字元，藉以取出每一個資料
    #並設定給變數plots(為串列物件)
    for row in plots:
        print(row[0]+' '+row[2]+' '+row[3])
        #每一個欄位(row)以索引取出該欄位資料








import json #載入JSON套件
with open(r'/Users/martychen/Desktop/Python/pm25tw.json' , encoding = 'utf8') as file: 
#開啟JSON檔並設定給變數file
    data = json.load(file)
    #執行load()方法將JSON檔案解碼為Python物件，並設定給data變數
    for item in data:
        print([item['Site'],item['county'],item['PM25']])
        #以索引列印item各欄位資料







import xml.etree.ElementTree as ET #載入 xml.etree.ElementTree 套件

tree = ET.parse(r'/Users/martychen/Desktop/Python/pm25tw.xml')
#以parse讀取解析XML檔案
root = tree.getroot() #取得根節點

for s in root.findall('Data'): #以findall方法取得根節點下的子節點標籤中符合的標籤取出顯示
    site = s.find('Site').text
    county = s.find('county').text
    pm = s.find('PM25').text
    print('測站：' , site , '--縣市' , county , '--PM25', pm)









# =============================================================================
#                              DATE : 20200605
# =============================================================================



1. 網頁擷取統一發票資料


#設定Python程式中新舊版本對unicode字串與輸出入的相容性
from __future__ import unicode_literals, print_function
import urllib    #存取網頁
from bs4 import BeautifulSoup	#解析網頁
import urllib.request    #存取網頁

# 財政部官網
request_url = 'http://invoice.etax.nat.gov.tw/' 

# 以urllib.request.urlopen開啟網頁物件並以read()讀取網頁內容
htmlContent = urllib.request.urlopen(request_url).read()

#將取得的網站內容分析並建立物件soup，以html.parser方法解析(解析HTML、XHTML)
soup = BeautifulSoup(htmlContent, "html.parser")

#搜尋所有網頁中標籤為span，且class屬性為t18Red者設定給results
results = soup.find_all("span", class_="t18Red")

subTitle = ['特別獎', '特獎', '頭獎', '增開六獎']     # 設定獎項串列

#搜尋所有網頁中標籤為h2，且id屬性為tabTitle者設定給months
months = soup.find_all('h2', {'id': 'tabTitle'})
# 最新一期，使用months物件的find_next_sibling方法找尋標籤為'h2'下的內容
month_newest = months[0].find_next_sibling('h2').text
# 上一期
month_previous = months[1].find_next_sibling('h2').text
print("最新一期統一發票開獎號碼 ({0})：".format(month_newest))
for index, item in enumerate(results[:4]):    #enumerate：列舉資料中的每一個項目
	print('>> {0} : {1}'.format(subTitle[index], item.text))
print ("上期統一發票開獎號碼 ({0})：".format(month_previous))
for index2, item2 in enumerate(results[4:8]):
	print ('>> {0} : {1}'.format(subTitle[index2], item2.text))




# enumerate 用法================================================================
# a1 = [1,2,3,4,5,6]
# for index,value in enumerate(a1):
#     print('%d,%d' % (index,value))
# =============================================================================

# print 之 format 格式==========================================================
# -> print(輸出字串參數.format(輸出資料1,2,....))
# example : print('{}{}{}'.format('a','b','c'))
#    好處：彈性調整{}{}{}的輸出順序與是否要輸出
# =============================================================================




2. 讀取 Yahoo 網頁原始碼

import requests
url = 'https://tw.yahoo.com/'
html = requests.get(url)
html.encoding='utf-8'

#以status_code 取得伺服器回應狀態碼。正確即回傳 request.codes.ok(=200)
if html.status_code == requests.codes.ok: 
    print(html.text)

3. requests 練習

import requests
payload = {'key1': 'value1', 'key2': 'value2'} #字典格式
html = requests.get('http://httpbin.org/get', payload)
print(html.url)


# =============================================================================
#     ＠httpbin.org
#         測試網站request(請求)及response(回應)的服務。
#         請求網址:http://httpbin.org/get
#                 http://httpbin.org/post
#         若帶參數請求，則以？＆合併於網址後。
# =============================================================================


4. requests 練習


import requests
payload = {'key1': 'value1', 'key2': 'value2'} #字典格式

html = requests.post('http://httpbin.org/post', payload)
print(html.text)
print(html.url)




5. 擷取 ptt 資料練習

import requests
from bs4 import BeautifulSoup
payload = {'from':'https://www.ptt.cc/bbs/Gossiping/index.html','yes':'yes'}

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Max OS X 10_12_3)'\
           'AppleWebKit/537.36 (KHTML, like Geoko) Chrome/56.0.2924.87 safari/537.36'}
            # 讓程式模擬瀏覽器的動作，騙過網頁伺服器。
    
rs = requests.session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html',headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text,\
          item.select('.title')[0].text)










6. select 練習

html = '''
<html><head><title>網頁標題</head></title>
<p class="header"><h2>文件標題</h2></p>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
'''

from bs4 import BeautifulSoup
sp = BeautifulSoup(html , 'html.parser') # sp 是網頁程式碼的內容
print(sp.title) # 可以取得網頁的標題內容
print(sp.find('h2')) # 找h2的標籤內容
print(sp.find_all('a')) # 找出所有a標籤的內容
print(sp.find_all('a',{'class':'red'}))  # 讀取所有a標籤中, 屬性等於 red 的內容。
data1 = sp.find('a',{'href':'http://example.com/one'}) #找到a標籤屬性是http://example.com/one的標籤內容，傳回的是串列。
print(data1.text)
data2 = sp.select('#link1') #傳回的是串列
print(data2[0].text) 
print(data2[0].get('href')) # 取得元素的屬性
print(data2[0]['href']) # 取得元素的屬性
print(sp.find_all(['title','h2'])) #找到標題是 title and h2的內容
print(sp.select('div img')[0]['src']) # 找到div裡面的img的第一筆資料的src







'''
＊瀏覽器自動化操作：Selenium
    ＠藉由程式指令，自動操作網頁。
        安裝 selenium 模組 pip install selenium
        下載並解壓 chrome WebDriver
    ＠取得網頁元素
        -> find_element_by_id (元素id)
        -> find_element_by_name (元素名稱)
        -> find_element_by_tag_name (元素標籤名)
        -> find_element_by_css_selector (元素css選擇器)
        -> find_element_by_css_link_text (元素連結文字)


'''

1. 自動登入 facebook

from selenium import webdriver

driver_path = r'/Users/martychen/Desktop/Python/chromedriver'
url = 'https://www.facebook.com/'
email = 'ddok133@gmail.com'
password = 'josh0220'
driver = webdriver.Chrome(driver_path)

driver.maximize_window() #瀏覽器視窗最大化
driver.get(url)

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()



2. 中央氣象局

from selenium import webdriver
import time

driver_path = r'/Users/martychen/Desktop/Python/chromedriver'
web = webdriver.Chrome(driver_path)
web.get('http://www.cwb.gov.tw/V7/')

web.set_window_position(0,0) # 設定瀏覽器的位置
web.set_window_size(700,700) # 設定瀏覽器的大小
time.sleep(5) # 暫停5秒
web.find_element_by_link_text('衛星').click()
time.sleep(5)
web.close()


3. Yahoo 自動搜尋關鍵字

from selenium import webdriver
url = 'https://tw.yahoo.com/'
driver_path = r'/Users/martychen/Desktop/Python/chromedriver'
browser = webdriver.Chrome(driver_path)
browser.get(url)

element = browser.find_element_by_id('UHSearchBox')
element.send_keys('C slass coupe')
submit = browser.find_element_by_id('UHSearchWeb').click()



4. Python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = r'/Users/martychen/Desktop/Python/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get('http://www.python.org')
print(driver.title)
assert 'Python' in driver.title # assert:當條件成立則執行...，不成立則呼叫例外。
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
print(driver.page_source)
driver.close()






5. IMDB


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = r'/Users/martychen/Desktop/Python/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get('http://www.imdb.com/')
search_elem = driver.find_element_by_css_selector('#navbar-query')
search_elem.send_keys('The Shape of Water')
time.sleep(3)
search_button_elem = driver.find_element_by_css_selector('#navbar-submit-button .navbarsprite')
search_button_elem.click()
time.sleep(3)
first_result_elem = driver.find_element_by_css_selector('#findSubHeader+ .findSection .odd:nth-child(1) .result_text a')
first_result_elem.click()
time.sleep(3)
rating_elem = driver.find_element_by_css_selector('strong span')
rating = float(rating_elem.text)
cast_elem = driver.find_element_by_css_selector('.itemprop .itemprop')
cast_list = [cast.text for cast in cast_elem]
driver.close()
print(rating, cast_list)




6. Yahoo 股市自動 


from selenium import webdriver
driver_path = r'/Users/martychen/Desktop/Python/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get('https://tw.finance.yahoo.com/')
more_rank_elem = driver.find_element_by_css_selector('.yui-text-left .yui-text-left table tr:nth-child(1) .stext div a')
more_rank_elem.click()
price_rank_elem = driver.find_element_by_css_selector('.yui-text-left+ .yui-text-left tr:nth-child(5) a')
price_rank_elem.click()
top_100_elem = driver.find_element_by_css_selector('p a+ a')
top_100_elem.click()
ticket_name_elem = driver.find_element_by_css_selector('.name')
ticket_name = [tn.text for tn in ticket_name_elem]
# driver.close()
print(ticket_name_elem)












# =============================================================================
#                              DATE : 20200608
# =============================================================================


'''
＊資料分析
    ＠Pandas 模組(資料存取)
        功能：
            - 自動讀取網頁表格資料
            - 匯入外部資料
            - 資料修改
            - 資料排序
            - 繪製圖表
        DataFrame:
            - Pandas 資料儲存型態
            - 為一個二維資料結構
            -> pandas.DataFrame(data(存放的二維資料) , columns(標題列) , index(標題欄))
            
        DataFrame 的資料儲存方式：
            - to_csv 儲存為csv格式
            - to_excel 儲存為Excel格式
            - to_sgl 儲存為SQLite格式
            - to_json 儲存為JSON格式
            - to_html 儲存為HTML格式
            
        pandas 讀取csv方法
            -> read_csv
            






'''



1. pandas 格式資料，輸出csv檔案

import pandas as pd #匯入pandas 模組. 並設定pd為此模組。
datas = [[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]
# 創建二維串列
index = ['李大年' , '王大同' , '黃美娟' , '陳美玲']
# 創建姓名
column = ['國文' , '數學' , '英文' , '自然' , '社會']
# 創建科目
df = pd.DataFrame(datas, columns=column, index = index)
# pd = pandas。帶入相關資料，建立pandas格式的資料。
print(df)

df.to_csv(r'/Users/martychen/Desktop/Python/pdout.csv' , encoding='utf-8-sig')



2. pandas 讀取 csv
import pandas as pd
rd = pd.read_csv(r'/Users/martychen/Desktop/Python/pdout.csv',encoding = 'utf-8-sig',index_col=0)
# index_col=0 : 設定第一欄為index值
print(rd)





'''
    ＠numpy 模組：建立資料矩陣
        *產生間隔數列
            -> numpy.linspace(起始,終止,數量,其他參數)
        
        
'''

1. numpy 舉例

import numpy as np
arr = np.array([[1,2,3],[4,5,6]]) # 建立 numpy 陣列(矩陣) 2*3 矩陣
print(arr)
ran_arr=np.random.random((4,2)) # 建立隨機分布於 0~1 的 4*2 矩陣
print(ran_arr)

2. 

import numpy
x = numpy.linspace(1,10,20)
print(x)



'''
＊資料視覺化：繪圖
    ＠Matplotlib模組：
        *大多繪圖功能放在 matplotlib.pyplot中
        *主要功能：繪製 x,y 座標圖 (通常將 x,y 放在串列中傳給matplotlip繪圖)
        
    ＠曲線圖    
        -> 模組名稱.plot( X座標串列 , Y座標串列 , 其他參數) ＃匯入繪圖座標
        -> 模組名稱.show() ＃顯示繪圖
    
    
'''



1. 曲線圖練習

import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx , listy)
plt.show()
    

2. 

import matplotlib.pyplot as plt

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.plot(listx1, listy1, label='Male') # 設定label 設定圖例
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.plot(listx2, listy2, color='red', linewidth=5, linestyle=':', label='Female')
# 設定color 預設為藍色 。 
# 設定 linewidth 預設值為1，可簡寫為lw。
# 設定 linestyle 預設為實線，可簡寫為le。常用 -- , -. , :
plt.legend() # legend 把圖例顯示出來
plt.xlim(0,20)
plt.ylim(0,100)
# lim(limit)，設定x,y軸的範圍。可省略讓程式自己抓。
plt.title('Pocket Money')
plt.xlabel('Age')
plt.ylabel('Money')
plt.show()




3. 結合 numpy 繪製曲線圖


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0 , 3*np.pi , 0.1) 
# na.arange = 迴圈的range 
# np.pi : 取numpy內建的pi值
y = np.sin(x)# 將 x 帶入三角函數 sin
plt.title('sine wave form')
plt.plot(x, y)
plt.show()


4.  一次繪製四個曲線表

import matplotlib.pyplot as plt
plt.figure() # 啟動多圖形函數 # figure : 繪圖畫面中可在容納多個小圖形# 啟動多圖形函數
plt.subplot(2,2,1) # subplot (列數,欄數,位置) ：將figure區域以欄列數劃分並將子圖繪製在位置處
plt.plot([0,1],[0,1])
plt.xlim(0,1)
plt.ylim(0,5)
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])
plt.xlim(0,1)
plt.ylim(0,5)
plt.subplot(2,2,3)
plt.plot([0,1],[0,3])
plt.xlim(0,1)
plt.ylim(0,5)
plt.subplot(2,2,4)
plt.plot([0,1],[0,5])
plt.xlim(0,1)
plt.ylim(0,5)
plt.show





5. 

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
y = 2 * x + 5
plt.title('matplotlib demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.plot(x,y)
plt.show()




6. 間隔分布圖 numpy linspace 練習

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1 , 1 , 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.plot(x , y1)
plt.show()
plt.plot(x , y2)
plt.show()


7. 間隔分布圖 numpy linspace 練習


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1 , 1 , 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.plot(x , y2 , 'ob') # 曲線 o:形狀 , b:顏色


# =============================================================================
# o:圓標記
# s:實心方塊
# p:五邊行
# v:倒三角
# ^：正三角
# h , H : 六邊行

# r紅
# g綠
# b藍
# y黃
# w白
# k黑
# c青
# m洋紅
# =============================================================================




'''
    ＠柱狀圖
        -> 模組名稱.bar(X座標串列 , Y座標串列 , 其他參數)  ＃匯入繪圖座標
'''


1. 繪製柱狀圖

from matplotlib import pyplot as plt #import matplotlib.pyplot as plt
x = [5,8,10]
y = [12,16,6]
x2 = [5,9,11]
y2 = [6,15,7]
plt.bar(x , y , align = 'center')
plt.bar(x2 , y2 , color = 'b' , align = 'center')
plt.title('bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# =============================================================================
# align = 'center' : 直條中央對齊座標刻度
# align = 'edge' : 直條邊緣對齊座標刻度
# =============================================================================




2. 

import matplotlib.pyplot as plt
x = ['bk' , 'sw' , 'ph' , 'rd' , 'gu']
a = [8,7,1,6,5]
b = [12,2,9,5,3]
plt.bar(x , a , label = 'a' , align = 'edge' , width = 0.3)
plt.bar(x , b , label = 'b' , align = 'edge' , width = -0.3)
plt.legend()

# =============================================================================
# width : 正值往右 , 負值往左
# =============================================================================



# Test
import matplotlib.pyplot as plt
x = ['bk' , 'sw' , 'ph' , 'rd' , 'gu']
a = [8,7,1,6,5]
b = [12,2,9,5,3]
c = [5,3,7,1,8]
plt.bar(x , a , label = 'a' , align = 'edge' , width = 0.3)
plt.bar(x , b , label = 'b' , align = 'edge' , width = -0.3)
plt.bar(x , c , label = 'c' , align = 'center' , width = 0.5)
plt.legend()




'''
    ＠圓餅圖
        -> 模組名稱.pie(資料串列 , 其他參數) ＃匯入繪圖座標
            size:資料串列
            labels:資料標籤
            autopct：數值百分比格式
            labeldistance:資料標籤與圓心的距離是半徑的幾倍
            shadow:設定陰影
            startangle:繪圖的起始角度(逆時針為正)
            
                  90
                  
            180        0
            
                 270
            
            
            pctdistance:百分比文字與圓心的距離是半徑的幾倍
            explode:設定圓形分離區塊的距離，以串列設定對應至資料項目
        
        ＊ 解決中文顯示方法, 參閱附件'繪圖中文顯示'。
        
            
            
            
'''


1. 圓餅圖

import matplotlib.pyplot as plt
labels = 'A','B','C','D','E','F'
size = 33,52,12,17,62,48

plt.pie(size , labels = labels , autopct = '%1.1f%%')
plt.axis('equal')
plt.show()



2. 
import matplotlib.pyplot as plt

labels = ['East','South','North','Middle']
size = [5,10,20,15]
colors = ['red','green','blue','yellow']
explode = (0,0,0.05,0)
plt.pie(size,explode = explode,labels = labels, colors = colors,\
        labeldistance = 1.1 , autopct = '%3.1f%%' , shadow = True,\
            startangle = 90, pctdistance = 0.6)

plt.axis('equal')
plt.legend(loc = 'lower right') # loc = location
plt.show()

# 解決座標軸負數的負號的顯示問題





'''
    ＠散佈圖 Scatter
        -> 模組名稱.scatter(x , y , 其他參數)
            s 是數量格式
            c 是顏色
            alpha 是透明度
            marker 是圖示
    


'''

1. 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Fixing random state for reproducibility
np.random.seed(20180731) # 設定亂數種子 # 為了讓亂數更亂

x = np.arange(0.0,50.0,2.0)
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = np.random.rand(*x.shape) * 800 + 500

plt.scatter(x,y,s,c = 'g' , alpha = 0.5 , marker=r'$\clubsuit$' , label = 'Luck')
# s 是數量格式 , c 是顏色 , alpha 是透明度 , marker 是圖示 , 
plt.xlabel('Leprechauns')
plt.ylabel('Gold')
plt.legend(loc=2)
plt.show()



2.1
import matplotlib.pyplot as plt
x = [1,2,4,6,8,1,2,9,3]
y = [5,7,2,3,1,4,6,5,8]
plt.scatter(x, y)
plt.show()


2.2
import matplotlib.pyplot as plt
x = [1,2,4,6,8,1,2,9,3]
y = [5,7,2,3,1,4,6,5,8]

plt.scatter(x, y , s=[150 for i in range(len(x))],c='r',alpha=0.6) # (for i in range(len(x)))這段可省略
plt.title('Scatter Simple')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()






3. 匯入 CSV 

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = r'/Users/martychen/Desktop/Python/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = (int(row[1])-32)*5/9
            low = (int(row[3])-32)*5/9
        except ValueError: # ValueError 當資料處理錯誤時
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            
fig = plt.figure(dpi=128,figsize=(5,3)) #設定繪圖區域的大小
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha=0.1)

title = 'Daily high and low tempertures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=13)
plt.tick_params(axis= 'both', which= 'major', labelsize=13)

plt.show()
            
            
            
            
            
            
            
            
            
            
            
# =============================================================================
#                              DATE : 20200610
# =============================================================================           
            
            
            
1. 繪製兩個正弦波的圖        
            
            
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0 , 5* np.pi , 1000) 

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.plot(x , y1 , label = '$ y = sin(x) $')
plt.plot(x , y2 , label = '$ y = sin(2 * x) $')
plt.legend(loc = 3) 

plt.show()   
            
            
        
        
        
 2.  plt.fill 填充繪圖區域圖的顏色

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0 , 5 * np.pi , 10000)       

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.fill(x , y1 , color = 'g', alpha = 0.3) # plt.fill 填充繪圖區域圖的顏色
plt.fill(x , y2 , color = 'b', alpha = 0.3)

plt.show()   
            
        
3. 兩個繪圖圖形之間的填色

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0 , 5 * np.pi , 10000)       

y1 = np.sin(x)
y2 = np.sin(2 * x)

plt.plot(x , y1 , color = 'g')
plt.plot(x , y2 , color = 'b')
plt.fill_between(x,y1,y2,facecolor='k')

plt.show()



4. 兩個繪圖圖形之間的限制區域的填色

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0 , 4.0*np.pi , 0.01)
y = np.sin(x)

plt.plot(x,y)
plt.plot((x.min(),x.max()),(0,0)) # 繪製水平基準線

plt.xlabel('x')
plt.ylabel('y')

plt.fill_between(x,y,where=(2.3<x) & (x<4.3) | (x>10),facecolor='purple')
plt.fill_between(x,y,where=(7<x) & (x<8),facecolor='green')
plt.show()
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




































































        
































































