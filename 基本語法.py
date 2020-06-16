Python


*基本語法
    1. 程式須區分英文大小寫
    2. 程式分行: \ , +
    3. 程式敘述以單行為主(一個完整的敘述語法)
    4. 若要在單行撰寫2個以上的完整語法,其間以 ; 隔開每一個完整的敘述。

*變數
    1.程式中儲存資料供程式使用，隨程式執行而變動其值
    2.直接寫出來使用，不需要特別宣告
    3.不須宣告其資料型態，系統會跟劇變數職自行設定
    
*命名規則:
    1. 第一個字元可以是英文的大小寫，底線符號，中文(不建議)
    2. 其他字元可以是英文的大小寫，底線符號，數字，中文(不建議)
    3. 英文大小寫視為不同的變數名稱
    4. 不可以使用關鍵字內建函式，內建類別名稱
    5. 建議:盡量以該變數在程式中代表的功能意義命名。如 age代表年齡         


    Example:
    a=10
    b=6.8
    c='Python'
    or
    a,b,c=10,6.8,'Python'
    



*資料型別
    1. Python動態型別(無須事先宣告)
    2. 另有強制型別宣告
    3. 型號
        int：整數
        bool：布林值，true or false。
        float：浮點數
        str：字串，以單(雙)引號前後括住。
        eval：數值
    4.相同型別的資料方可運算
    5.Python具備自動轉換型別的功能，若無法自動轉換，則採強制型別宣告。
        Ex: int(資料) , str(資料) , float(資料) , eval(資料)
    6.type(資料)：查詢資料型態



    Example:
    x=10
    y=x/3
    print(x)
    print(type(x)) # type(x)
    print(y)
    print(type(y)) # type(y)
        


    7.int 預設為10進位
        另有
        二進位:數值前加上 0b 
        八進位:數值前加上 0o
        十六進位:數值前加上 0x
    
    8. 轉換函數
        轉二進位 : bin(資料)
        轉八進位 : oct(資料)
        轉十六進位 : hex(資料)
 

    Example:
    x=0b01000001
    print(x)
    y=65
    print(bin(y))

          
        PS: 
            upper() : 將字串轉換為全部大寫英文
            str(s) : 字串函式, 轉換為字串
            ＼t : 是tab的意思
            end : 不換行
            input() : 供使用者輸資料之用，輸入時按下enter 及表示輸入完畢，將輸入資料存到變數中。
                -> 變數 ＝ input( '提示字串')
            print() : 輸出(格式化)
            sep= x : 使用x連接輸出元素 



#Exercise================================================
1. 求總合
a=1;b=100;print('*.*',a-b)


2. 求最大公因數
num1=int(input('Please input Num1:'))
num2=int(input('Please input Num2:'))
if num1<num2:
    tmp_num=num1
    num1=num2
    num2=tmp_num
while num2 !=0:
    tmp_num=num1 % num2
    num1=num2
    num2=tmp_num
    print('The max of common section is',num1)


3. \分行
a=b=c=12
y=a+ \
    b+ \
        c+ \
            20
print(y)


4. 學習函式input
score=input('請輸入國文成績:')
print(score)


5. eval 函式練習
score=eval(input('請輸入國文成績:'))
sum=score+20
print(score , sum)


6. spe 應用
print(100 , 'python',200,sep=' & ')





*運算式：由運算元(進行運算的資料)及運算子(執行運算的動作)組成。
    
    ＠運算子
        1. 單一運算子 ：運算元只有一個 , not a。
        2. 二元運算子 ：運算元有兩個，運算子放在兩個運算元之間 , a+b 。

    ＠函式 : function
        內建函式 ： 將特定功能予以包裝並將參數帶入資料運算執行，Python 已定義完成，直接依功能使用。
            -> 函式名稱(參數)
            -> 變數＝input( '提示字串' ) : 供使用者輸資料之用
                輸入時按下enter 及表示輸入完畢，將輸入資料存到變數中
            -> eval(資料) : 將字串(數值型字串)轉換為數值

            -> print() : 輸出(格式化)
            -> print(資料1 , 資料2 , sep=分隔字元 , end=結束字元)
                sep 預設為空白
                End 輸出後最後要加入的字元，預設為換行 \n。
                換行符號 ： \n
                Ex : print(‘\n’) 跟 print() 一樣

            -> print(格式參數1 格式參數2 …. % 資料1 資料2....) 
                格式參數 
                    ％s ：字串
                    %f ：浮點數
                    格式參數1 對應 資料1
                格式參數：
                    %5s : 輸出5個字元，小於5個字元於左方填入空白，大於5個字元則全數輸出。
                    %5d : 輸出5位整數，小於5位整數於左方填入空白，大於5位整數則全數輸出。
                    ％8.2f : 輸出8位數字( 含小數點)，小數取兩位。
				            若整數小於5位，則在數字左方填入空白。若小數小於2位，則在數字右方填入0。
					        ＋：於格式數值前加入。若數字為正，則在資料左方加上”+”。
					        -：輸出格式資料空間有多餘時，則資料靠左對齊。 
                            
 

# Exercise========================================================


格式參數練習
1.
a3=100
print('a=/%-6d/' % a3)
b=123456789.34287549875
print('b=/%-7.2f/' % b)
c='deep'
print('c=/%-6s/' % c)

2. 
a=int(input('請輸入國文成績：'))
b=int(input('請輸入英文成績：'))
c=int(input('請輸入數學成績：'))
d=a+b+c
e=d/3
print( '總成績:', a+b+c , '平均成績: %2.2f' % e)

form teacher:
    
chi=input('請輸入國文成績：')
math=input('請輸入數學成績：')
eng=input('請輸入英文成績：')
sum=int(chi)+int(math)+int(eng)
avg=sum/3
print('總成績：%d , 平均成績：%5.2f' % (sum , avg))
  

#========================================================                            
                            
                            
                            
                                                
                            

*流程控制
    1. 以特定結構控制程式的執行方式
    2. 條件式：
        必須以縮排進行程式結構化
		條件式下的敘述式一定要往右縮排(自動,tab)
    ＠If
        abs(x) : 計算x之絕對值
        1. If
            if 條件式：
               敘述式
               若條件成立，則執行敘述式

        2. If~else
            if 條件式：
               敘述式1
            else:
               敘述式2
               若條件成立，則執行敘述式1
               否則執行敘述式2

        3. If~elif
            if 條件式：
               敘述式1
            elif 條件2:
               敘述式2
            elif 條件n：
               敘述式n
            else:
               敘述式n+1
               逐一判斷條件，若成立則執行該敘述式後離開if
               當所有的條件都不成立，則執行敘述式 n+1

        4. 巢狀if : 可套用任何if條件
            if 條件式1:
            if 條件式2:
            if 條件式3:



#Exercise===============================================

if練習

1.
print()
num=eval(input('請輸入整數值'))
if(int(num)<0):
   num=abs(num)
print('絕對值是%d' % num)



if~else 練習

1.
print()
num=eval(input('請輸入整數值'))
rem=num % 2
if(rem==0):
    print('%d是偶數' % num)
else:
    print('%d是奇數' % num)


2. 
PI=3.14159
radius=eval(input('請輸入圓半徑'))
area=PI*radius**2
if radius < 0:
    print('圓半徑不能是負數')
else:
    print('圓半徑=' , radius , '，圓面積=' , area)
    
    
if~elif 練習
    
1.
a , b , c = eval(input('請輸入a,b,c'))
d=b*b - 4*a*c
if d>0:
    print('一元二次方程式有兩個不同的解')
elif d==0:
    print('一元二次方程式只有一個解')
else:
    print('一元二次方程式無解')
print('結束')

2.
score=int(input('請輸入分數：'))
if score >89:
    print('優等')
elif score > 79:
    print('甲等')
elif score > 69:
    print('乙等')
elif score > 59:
    print('丙等')
else:
    print('不及格')
    
3.
num=int(input('請輸入：'))
if num ==1:
    print('one')
elif num ==2:
    print('two')
elif num==3:
    print('three')
elif num==4:
    print('four')
elif num==5:
    print('five')
else:
    print('輸入超出範圍')


巢狀 if 練習
    
1.

score=eval(input('請輸入分數(0~100)：'))
if score >=90:
    print('優等')
else:
    if score >=80:
        print('甲等')
    else:
        if score >=70:
            print('乙等')
        else:
                if score >=60:
                    print('丙等')
                else:
                        print('不及格')



＊迴圈：重複執行的敘述
    ＠for:定數迴圈
        -> for 變數 in iterator:
            敘述式

            iterator 使用函式 range( 起始值 , 終止值 , 間隔值)
  
            起始值 ：預設值0 , 可不指定
            終止值 ：迴圈執行時，不包含終止值
            間隔值 ： 預設值1 , 可不指定

    ＠while：不定數迴圈    
        -> while 條件式：
                 敘述式
                 
                 當條件成立，則執行敘述



#Exercise=====================================================

迴圈訓練

for 練習:
    
1.印出0~10的整數
for i in range(11):
    print(i ,end = ' ')
    
    
2. 計算1+2+3+......+100
sum=0
for a in range(1,101):
    sum += a
print('sum=',sum)


3.計算1+2+3+......+n
n=eval(input('請輸入整數:'))
sum=0
for a in range(1,n+1):
    sum+=a
print('sum=',sum)

4. 計算 4+9+13+18+22+......+85+90+94+99
option.a
sum=0
for a in range(4,95,9):
    sum+=a
for a in range(9,100,9):
    sum+=a
print('sum=',sum)

option.b
sum=0
for a in range(4,95,9):
    sum=sum+a+(a+5)
print('sum=',sum)

5.請輸入正整數：連續相乘 ＃6 , 6!=720
option.a
num=eval(input('請輸入正整數：'))
sum=1
for a in range(1,num+1):
    sum*=a
print('sum=',sum)

option.b
num=eval(input('請輸入正整數：'))
sum=1
for a in range(num,0,-1):
    sum*=a
print('sum=',sum)


while 練習

1. 
i=0
while i<11:
    print(i)
    i=i+1
    
2.請輸入第0位學生成績(輸入-1結束)：
本班總成績：00分 , 平均：00分(小數兩位)

total = person = score = 0
while(score !=-1):
    person +=1
    total += score
    score = int(input('請輸入第 %d 位學生的成績（輸入-1 結束):' % person))
average = total / (person - 1)
print('本班總成績：%d 分，平均成績：%5.2f 分' % (total , average))


3.請輸入電腦的英文

ans=input('請輸入電腦的英文：')
while ans.upper() !='COMPUTER':
    ans=input('答錯了，請重新輸入')
else:
    print('恭喜答對')
    


4. 輸入年齡計算票價
票價100元：
若 <=6歲 或 >=70歲則打2折。
若 7~12 歲或是 60~69 歲 則打 5折。

age = int(eval(input('Please enter your age:')))
if (age <= 6 or age >=70):
    print('80% off')

elif (age >= 7 and age <=12):
    print('50% off')

elif (age >= 60 and age <=69):
    print('50% off')
       
else:
    print('No discount')
    





＊ 巢狀迴圈：
    ＠迴圈中的敘述式為另一個迴圈結構
    ＠巢狀層數不限
    ＠for , while 皆可構成巢式結構


  
1. 九九乘法表
第一種寫法

for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2d' % (i,j,i*j),'\t',sep=' ',end='')
    print()
    
第二種寫法

for i in range(1,10):
    for j in range(1,10):
        print(i,'*',j,'=',i*j,'\t',sep='',end='')
    print()

第三種寫法

for i in range(1,10):
    for j in range(1,10):
        s=i*j
        if s<10:
            s='0'+str(s)
        print(i,'*',j,'=',s,'\t',sep='',end='')
    print()

 PS : str(s):字串函式, 轉換為字串
      ＼t:是tab的意思




＊ 中斷迴圈
    ＠break:中斷後直接離開迴圈
    ＠continue:中斷後回到迴圈開頭繼續執行


# break 練習====================================================================

ans=input('請輸入電腦的英文（輸入QUIT結束)：')
while ans.upper() !='COMPUTER':
    if ans.upper() == 'QUIT':
        print('不玩了！')
        break
    ans=input('答錯了，請重新輸入')
else:
    print('恭喜答對')
    
# continue 練習
Ex : 輸入大樓的樓層數，並印出樓層數，請排除四樓

n=int(input('請輸入大樓的樓層數'))
print('本大樓具有的樓層數為：')
if(n>3):
    n +=1
for i in range(1, n+1):
    if(i==4):
        continue
    print(i,end='-')
print()



# 迴圈練習========================================================================
Ex : 數入層數，以*列印出該層數的直角三角形。
如：3
*
**
***

n=eval(input('請輸入層數：'))
for a in range(1, n+1):
    for b in range(0, a):
        print('*',end='')
    print()
    
Ex : 沿上，變成倒三角形  
n=eval(input('請輸入層數：'))
for a in range(n,0,-1):
    for b in range(0, a):
        print('*',end='')
    print()

Ex : 輸入三位整數，判斷此三位數是否為迴文數。
迴文數：又稱對稱數，將數字正向反向相同，如16861

number=eval(input('PLease enter a three-digit integer：'))
reversedNumber = (number % 10)*100+(number // 10 % 10)*10 + (number // 100)
if number == reversedNumber:
    print(number , 'is a palindrome number.')
else:
    print(number , 'is not a palindrome number.')
    
EX : 輸入3個數字，並依序由小到大輸出
    
num1 , num2 , num3 = eval(input('Enter three integers:'))
if num1 > num2:
    num1 , num2 = num2 , num1
    
if num2 > num3:
    num2 , num3 = num3 , num2
    
if num1 > num2:
   num1 , num2 = num2 , num1 
   
print('The sorted number are' , num1 , num2 , num3)




＊亂數產生器

Example:
    
import random
for i in range(1, 11):
    randnum=random.randint(1, 100)
    print('%4d' % randnum , end='')
  
    
    
樂透號碼產生器＋排序
lst=[]
import random
for i in range(6):
    randnum=random.randint(1,49)
    lst.append(randnum)

lst.sort()
print(lst)

    


Example:
import random
even = 0
odd = 0
for i in range(1, 11):
    randNum = random.randint(1, 100)
    print('%4d' % randNum , end='')
    if randNum % 2 ==0:
        even += 1
    else:
        odd+=1
print('\n奇數 = %d 個 , 偶數 = %d 個' % (even , odd))




*函式：
    ＠定義：
    將一組具有特定程式功能的程式碼，以獨立的程式架構建立為一個單元，並賦予一個名稱，
    供後續程式呼叫使用。
    優點：
    1. 重複性：使用時以呼叫名稱方式執行，不需重複撰寫程式碼。
    2. 精簡：無需重複相同的程式碼
    3. 可讀性：程式不複雜，可讀性提高。
    
    ＠宣告函式：
    
    def 函式名稱（參數^多個參數以透號隔開，若無參數，需保留小括號^）：
        敘述式
        .
        .
        .
        return 傳回值^無傳回值可省略，若有則傳回呼叫函式處^


    ＠呼叫
    函式必須呼叫方可被執行
        -呼叫格式：
        無傳回值 -> 函式名稱(參數)
        有傳回值 -> 變數=函式名稱(參數)
        
        
    @函式預設參數值：
        -函數宣告時，可指定參數的預設值。
        -當呼叫函數時，若無指定參數值，則會採用預設參數值。
        -呼叫函式時，全不指定參數，則全部以預設參數值帶入。
        -預設參數值有設定，不可寫在無預設參數值的前面。
         ^錯誤語法 def total(a=1 , b)^
        

Example:
1.不用函式
for i in range(1, 21):
    print('*',end='')
print()
for i in range(1, 31):
    print('*',end='')
print()
for i in range(1, 51):
    print('*',end='')

2.用函式
def printStar(n):
    for i in range(1, n+1):
        print('*',end='')
    print()

printStar(20)
printStar(30)
printStar(50)

3. 函式中呼叫函式
def main():
    printStar(20)
    printStar(30)
    printStar(50)
main()

Ex:建立函式，求出1~100總和(無參數，無傳回值)
def total():
    sum=0
    for i in range(1, 101):
        sum +=i
    print(sum)

total()

Ex:建立函式，求出1~100總和(無參數，有傳回值)
def total():
    sum=0
    for i in range(1, 101):
        sum +=i
    return sum

t=total()
print(t)

Ex:建立函式，求出1~100總和(有參數，有傳回值)
def total(a,b):
    sum=0
    for i in range(a, b+1):
        sum +=i
    return sum

a,b=eval(input('Enter integers'))
t=total(a,b)
print(t)

From teacher:

def total(a,b):
    sum=0
    for i in range(a, b+1):
        sum +=i
    return sum
    
def main():
    x=eval(input('請輸入起始數字：'))
    y=eval(input('請輸入終止數字：'))
    t=total(x,y)
    print('%d 到 %d 的總和為：%d' % (x,y,t))

main()
    
Ex:求總和與平均值，傳回多個值。
    
def SumandAverage(n1,n2):
    total=0
    average=0.0
    for i in range(n1, n2+1):
        total +=i
    average = total / (n2-n1+1)
    return total , average
    
def main():
    s,a =SumandAverage(1, 100)
    print('Sum=%d , average=%.2f' % (s,a))
    
main()
  
  
Ex:沿上題，預設參數值練習   

  
def SumandAverage(n1,n2=100):
    total=0
    average=0.0
    for i in range(n1, n2+1):
        total +=i
    average = total / (n2-n1+1)
    return total , average
    
def main():
    s,a =SumandAverage(1)
    print('Sum=%d , average=%.2f' % (s,a))   
    s,a =SumandAverage(100)
    print('Sum=%d , average=%.2f' % (s,a))  

main()


Ex:請輸入攝氏溫度:36
攝氏36度=華氏96.8度 , 公式：華氏=(9/5)x攝氏+32

1. 請以無傳回值方式撰寫
def Tem(n):
    m=(9/5)*n+32
    print(m)
    
Tem(36)


From teacher
def CtoF(degC):
    degF=degC*1.8+32
    print('攝氏' , degC , '度＝華氏' , degF,'度')
tempC=eval(input('請輸入攝氏溫度：'))
CtoF(tempC)

2. 請以有傳回值方式撰寫
def Tem(n):
    n=(9/5)*n+32
    return n

t=Tem(36)
print(t)

From teacher
print()
def CtoF(degC):
    degF=degC*1.8+32
    return degF
tempC=eval(input('請輸入攝氏溫度：'))
tempF=CtoF(tempC)
print('攝氏' , tempC , '度=華氏' , tempF , '度')











＊資料結構
    ＠串列：list(資料容器)
    ＠一維串列
    1. 一連串資料組成(等同於陣列)
    2. 可存放 "不同型態" 的資料
    3. 以[中括號]前後括住資料，資料之間以逗號隔開
    4. 可建構為多維串列(一維 , 二維....)
    5. len()函式：求串列長度(元素個數)
    6. append()函式：加入元素
        append(value): 將 value 加入到串列尾端
    7. insert()函式：加入元素在指定索引處
        insert(index,value)
    8. pop()函式：移除串列最後一個元素
        pop(索引)：移除串列指定索引元素
    9. remove()函式：移除指定值(若多個相同數值，僅移除第一個)
        remove(value)
    10. count():求串列指定值出現的次數
        count(value)
    11. index():求串列值所在的索引
        index(value)
    12. sort():串列排序(由小到大)
        
    13. reverse():串列元素反轉
    
    14. in / not in 判斷元素是否在/不在串列中
    15. sum():求串列元素總和
        max():求串列元素最大值
        min():求串列元素最小值
        
    16. +：連結串列
        *：複製串列
    
    

 

＠一維串列
   
list1 = []
list2 = [1,2,3,4,5]
list3 = ['apple' , 'banana' , 'orange']
list4 = [1,35,16.78,'pineapple']   
    
 
list2 #輸出 list2
list3[0] #輸出 list3 的第一個 串列名稱[索引值]從0開始
list2[1:3] #輸出 list2的第 2 個到 3 個 串列名稱[起始：終止] 起始到終止-1的元素
len(list2) #求 list2 元素個數
list1.append(10) #加入元素10
list1
list1.append(20) #加入元素20
list1
list1.insert(1, 30) #在1的位置加入30
list1
list2.pop() #移除list2 最後一個元素
list2
list2.pop(1) #移除list2 位置1的元素
list2
list2.remove(3) #移除list2 的3數值
list2
list3.append('apple') #加入元素 apple
list3
list3.count('apple') #求apple出現的次數
list3.index('banana') #求banana 所在的位置
list3.index('orange') #求orange 所在的位置
list3.index('apple') #求apple 所在的位置
list1.append(40)
list1
list1.sort() #排序由小到大
list1
list1.reverse() #排序由大到小
list1

30 in list1
50 not in list1
'apple' in list3

sum(list1)
max(list1)
min(list1)

list1+list2 # 執行輸出 list1連結list2
list1+list3 # 執行輸出 list1連結list3


2*list2 # 複製list2兩次
list1[-1] #輸出list1 -1位置
list1[-3:-1] #輸出 list1 -3到-1 位置
list1[-4:4]


# Exercise＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

1. 練習迴圈輸出
list3 = ['apple','banana','orange','kiwi']

for i in range(len(list3)):
    print('list3[%d]=%s' % (i , list3[i]))
  
    
 2. 樂透號碼輸出(號碼會重複)
import random
lotto = []
for i in range(1,7):
    randNum = random.randint(1,49)
    lotto.append(randNum)
print('樂透號碼是：')
for i in lotto:
    print('%4d' % i , end = '')
    
    
    
3. 樂透號碼輸出(號碼不重複)(輔助串列 checkNum)
import random
lotto = []
checkNum = []

for i in range(0 , 50):
    checkNum.append(0)
    
count = 1
while count <= 6:
    randNum = random.randint(1 , 49)
    if checkNum[randNum] == 0:
        lotto.append(randNum)
        count += 1
    checkNum[randNum] = 1
    
print("樂透號碼是：\n" , end = '')
for i in lotto:
    print(i , end = ' ')
print()


# Explain===================================================
checkNum[]串列：元素全部以0加入
    checkNum[0,0,0,0,0,0,0,0.....0,0]
while 迴圈重複執行6次
 a.取亂數 1~49 
 b.以取得的亂數做為索引帶入到 checkNum[]串列，判斷該元素是否為0
    0:加入該索引值到 lotto[],並設定該索引之 checkNum 元素為1
    1:該亂數(索引)已加入 lotto[], count 不計數(加1)
 c.若為0, 則將該索引值加入到 lotto[]串列
 d. 將 checkNum[] 串列中該索引值位置之元素設定為1
重複執行abcd
#===========================================================
    


4. 樂透號碼輸出(號碼不重複)(not in)
import random
lotto = []
n = 1
while n <= 6:
    randNum = random.randint(1 , 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n += 1

print('樂透號碼是：\n' , end = '')
for i in lotto:
    print('%4d' % i , end = '')
print()


5. 樂透號碼輸出(號碼不重複 + 排序)
import random
lotto = []
n = 1
while n <= 6:
    randNum = random.randint(1 , 49)
    if randNum not in lotto:
        lotto.append(randNum)
        n += 1
print('樂透號碼是: \n' , end = '')
for i in lotto:
    print('%4d' % i , end = ' ')
print()

lotto.sort()
print('號碼排序後：')
for i in lotto:
    print('%4d' % i , end = ' ')
print()


'''

＊資料結構
    ＠二維串列：視為多個一維串列組成，如 5 位學生，每位學生的 3 科成績。
    st = [[85,68,34],[45,67,98].[87,98,88],[68,44,96],[98,74,69]]
    st[3][0] = 68
    st[3][3] = 44
    st[3][2] = 96
    
'''

＠二維串列

list5 = [[1,2,3],[4,5,6]]
list5[0] #print(list5[0])
len(list5) #print(len(list5))
len(list5[1]) #print(len(list[1]))


#Exercise================================================

1. 請輸入二維元素數量後，隨機產生該數量的 1~50 數值
import random
rows = eval(input('請輸入列數：'))
columns = eval(input('請輸入欄數：'))
lst = []
for i in range(rows):
    lst.append([]) #將lst 建立為二維串列
    for j in range(columns):
        lst[i].append(random.randint(1 , 50))
print(lst)

2. 請輸入二維元素數量後，隨機產生該數量的 1~50 數值，並列出二維串例裡的數字
import random
rows = eval(input('請輸入列數：'))
columns = eval(input('請輸入欄數：'))
lst = []
for i in range(rows):
    lst.append([]) #將lst 建立為二維串列
    for j in range(columns):
        lst[i].append(random.randint(1 , 50))
print(lst)
print()
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print('lst[%d][%d] = %5d' % (i , j , lst[i][j]))
    print()

3. 請輸入二維元素數量後，隨機產生該數量的 1~50 數值，並計算總和
import random
rows = eval(input('請輸入列數：'))
columns = eval(input('請輸入欄數：'))
lst = []
for i in range(rows):
    lst.append([]) #將lst 建立為二維串列
    for j in range(columns):
        lst[i].append(random.randint(1 , 50))
print(lst)
print()
for column in range(len(lst[0])):
    total = 0
    for row in range(len(lst)):
        total += lst[row][column]
    print('第 %d 行的總和 = %d' % (column , total))
    

#===========================================================
    
    
'''
*資料結構

    ＠元組(數組)：tuple
    1. 與串列(list)類似，不同如下：
        - tuple 內的元素值不可以改變
        - 無法刪除個別元素
        - 無法取代個別元素
        - 可以刪除整個數組
        - 以(小括號)建立tuple

'''

tu1 = (1,2,3,4,5)
tu1
tu2 = ()
tu2
tu3 = tuple([x for x in range(1,6)])
tu3
tu4 = tuple('python')
tu4

tu1 += (6,7)
tu1

tu1[2] #輸出索引值元素

tu1[3:6] #輸出索引值元素


tu3 = 2*tu3
tu3

for i in tu1:
    print(i , end = ' ')


del tu1
tu1


'''

＊資料結構
    ＠集合：set
    1. 以{大括號}建立
    2. 集合不包含重複的資料
    3. add(x):將 x 加入集合
    4. remove(x): 將 x 從集合移除，可移除全部的 x。(串列僅能移除第一個 X)(Tuple 沒有 remove() 函式)
    5. 聯集：union(集合) (符號是 |)
    6. 交集：intersection(集合) (符號是 &)
    7. 差集：difference(集合) (符號是 -)
    8. ==:比較兩集合是否相等
      ！=:比較兩集合是否不相等
    

'''



s1 = {1,2,3}
s1
s2 = set()
s3 = set([x for x in range(1,6)])
s3

s4 = set((1,2,3)) #等同 s4 = {1,2,3}
s4

s5 = set((1,1,2,2,3)) 
s5 #集合不包含重複的資料

s10 = {1,3,6}
s10.add(20)
s10

s10.remove(3)
s10


set10 = {1,3,6}
set10.add(20)
set10

asd10 = {1,3,6}
asd10.add(20)
asd10

set20 = {1,6,8,10,20}
set25 = {1,3,8,10}
set20.union(set25) # or set20|set25



'''
＊資料結構
    ＠詞典：dict
    1. 以{大括號}建立
    2. 資料以鍵值(key)及值(value)組成
    3. 格式 key:value
    4. keys():列出key值
    5. values():列出values值
    6. items(): 列出項目值
    7. copy()：複製詞典
    8. update():合併詞典(若有重複，不顯示)（若有衝突，取後者）
    9. 詞典排序：針對key排序
        -> sorted(a,b,c)
        a:排序資料
        b:排序依據
        c:排序方式遞增or遞減


'''

dict1 = {'Taipei':'101','Paris':'Tour Eiffel','London':'Big Ben'}
dict1
dict1['Berlion']='Wall'
dict1
dict1['Taipei']

for key in dict1:
    print('%s:%s' % (key , dict1[key]))

dict1.keys()
dict1.values()
dict1.items()
tuple(dict1.items())

del dict1['Taipei'] #移除Taipei
dict1

dict2 = {1:'red' , 2:'yellow' , 3:'green'}
dict3 = {4:'blue' , 1:'purple'}
dict4 = dict2.copy()
dict4
dict4.update(dict3)
dict4


#Exercise_0521=====================================================

宣告一個整數串列(大小為5)
傳遞給 output(aList)函式
函式由輸入初始化後
回傳給主程式並且輸出該串列
再由主程式將該串列傳給 max(aList) 及 min(aList) 函式
輸出 aList 之最大值及最小值
(不可使用系統函式)




#==============================================================


'''
*資料結構整理

    ＠串列：list
        建立 -> 串列名稱 = [元素1 , 元素2 , .....]
        元素建立後即有索引值，索引值從 0 起算。
    
        語法
        1. append:加入元素，元素可為資料或串列。
        2. extend:加入元素，元素為串列。
    
    
    ＠數組(元祖):tuple
        建立 -> 數組名稱 = (元素1 , 元素2 , .....)
        元素個數，元素值皆不可改變，其餘與串列相同。
        不可使用 append , inseert。
    
        串列功能比數組大。
        數組優點：
        1. 安全，因為元素不可更改。
        2. 執行速度快。因為元素不可更改，所以資料簡單，因為簡單所以執行速度快。
        
        應用：串列與數組互相轉換
        轉換方式：
        1. 數組轉串列
            tuple1=(1,2,3)
            list1=list(tuple1)
            
            2. 串列轉數組
            list2=[4,5,6]
            tuple2=tuple(list2)


    @字典(詞典):dict
        建立 -> 字典名稱 = {元素1 , 元素2 , .....}
            -> 字典名稱 = dict([[key1,value1] , [key2,value2] , ....])
            -> 字典名稱 = dict(key1=value1 , key2=value2 , .......)
            ps:第三種建立方式，key不可為數值。        
            每一個元素都是 key(必須唯一):value(可以重複)
            若重複，則將 key 覆蓋，只有最後的 key 會存在。
        
        字典元素(在記憶體內的存放方式)無一定的順序排列，字串元素則為依序排列。
        
        字典取值的方式 -> 字典名稱[key]
            以 key 做為索引取得 value
            
        當 key 不存在，會產生錯誤。
        
        使用 get() 取得 value。若 key 不存在，則得到 none。
            -> 字典名稱.get(key)
                fruit = {'apple':15 , 'banana':10 , 'tomoto':12} 
                print(fruit.get('apple'))
                
        #Exercise 查詢血型，若無資料則顯示無此血型。
            
            dict1 = {'a':'內向穩重' , 'b':'外向樂觀' , 'o':'堅強自信' , 'ab':'聰明自然'}
            name = input('輸入血型：')
            blood = dict1.get(name)
            if blood == None:
                print('沒有'+ name + '血型！')
            else:
                print(name + ' 血型個性為：' + str(dict1[name]))
                
        字典修改：
            -> 字典名稱[key]=value
                fruit[apple] = 10
                
        字典刪除：
            刪除特定元素 -> del 字典名稱[key]
            刪除所有元素 -> 字典名稱.clear()
            刪除字典 -> del 字典名稱

        #Exercise 學生成績查詢系統，若查無資料則輸入成績。
            
            dict1 = {'Kelly':85 , 'Tom':89 , 'Marry':55}
            name = input('Please enter your name :')
            if name in dict1:
                print(name + 's score = ' + str(dict1[name]) )
            else:
                score = input('Please input your score :')
                dict1[name]=score
                print('字典內容:' + str(dict1))
            
   
'''


'''
*字串(str)
    Python並無特別區分字元及字串，均以單雙引號千後括住。
    
    @建立空字串：
        s1 = str()
        s2 = ''
    @建立字串：
        s3 = str('這是Python程式設計')
        s4 = 'Today is rainy day'
        
    @字串函式：
        -> len(字串名)：字串長度(字元數)
        -> max(字串名)：字串最大值
        -> min(字串名)：字串最小值
        -> 字串名[索引值]：取得字串特定字元
        max(s4)
        min(s4)
        len(s4)
        s4[1] , s4[-2]
        
        -> 字串名[起始值：終止值]：取得從起始值到終止值-1的字串
        s4[3:8]
        
        -> 字串名 + 字串名：串接
        -> 字串名 * 字串名：複製
        s5 = 'Simon'
        s6 = 'Lee'
        s5+s6
        s5*2
        
    @字串測試：字串名.函式()
        函式():傳回值為布林值
        -> 字串名.isalnum():字串是否為字元及數值
        s5.isalnum()
        -> 字串名.isalpha():字串是否為字元
        s5.isalpha()
        -> 字串名.isdigit():字串是否為數值
        s5.isdigit()
        -> 字串名.islower():字串是否皆為英文小寫
        -> 字串名.isupper():字串是否皆為英文大寫
        -> 字串名.isspace():字串是否皆為空白字元

    @子字串：字串名.函式('子字串')
        -> 字串名.endswith('子字串')：字串結尾是否為子字串
        -> 字串名.startswith('子字串')：字串開頭是否為子字串
        s5.endswith('on')
        s5.startswith('Si')
        -> 字串名.find('子字串'):字串中子字串的最小位置數值
        -> 字串名.rfind('子字串'):字串中子字串的最大位置數值
        -> 字串名.count('子字串'):字串中子字串的個數
        s7 = 'abcdeabcde'
        s7.find('e')
        s7.rfind('e')
        s7.count('e')
    
    @字串轉換
        -> 字串名.capitalize():將字串中第一個字元轉換為大寫，其餘小寫。
        -> 字串名.lower():將字串中所有字元轉換為小寫。
        -> 字串名.upper():將字串中所有字元轉換為大寫。
        -> 字串名.swapcase():將字串中的字元，大小寫互相轉換。
        -> 字串名.replace(str1,str2):str2 取代 str1。
        -> 字串名.title():將字串中每一個單字第一個字元轉換為大寫，其餘為小寫。
        s8 = 'Welcome to Taipei'
        s8.replace('Taipei','Tainan')
        print(s8)
    
    
    @空白處理
        -> 字串名.lstrip():刪除字串左側空白。
        -> 字串名.rstrip():刪除字串右側空白。
        -> 字串名.strip():刪除字串兩側空白。
        s9 = '     Welcome to my home    '
        s9.lstrip()
        s9.rstrip()
        s9.strip()

    @對齊
        -> 字串名.center(寬度值):將字串以寬度值置中對齊。
        -> 字串名.ljhust(寬度值):將字串以寬度值靠左對齊。
        -> 字串名.rjust(寬度值):將字串以寬度值靠右對齊。 
        s10 = 'Taipei City'
        s10.center(20)
        s10.ljust(20)
        s10.rjust(20)
        
        -> 字串名.split():字串分割。
        s11 = 'apple banana kiwi orange'
        lst = s11.split() #以空白字元做為分割字元
        lst

        s12 = '05-22-2020'
        lst1 = s12.split('-') #以減號做為分割字元
        lst1
    
    
'''



#Exercise========================================================

1. 讓使用者輸入10個數字不重複的數字至串列，並將該串列傳遞給名為 compute()的函式。
此函式接收一個串列 lst 和一個數字 a(預設3)，並回傳 lst 中 a 個最大的數字。
最後再將回傳結果輸出。


def compute(lst,a=3):
    lst.sort()
    ans = []
    for i in range(-1 , -1*a-1 , -1):
        ans.append(lst[i])
    return ans

def main():
    lst = []
    for i in range(10):
        num = eval(input('Please enter 10 numerals:'))
        lst.append(num)
    print(lst)
    print(compute(lst))
    
main()



2. 撰寫一成是，以 lotto() 函式產生大
號碼，並以 main() 函式呼叫 5 次 lotto()函式，
即產生五組大樂透號碼。請將大樂透號碼由小至大排序。

import random
def lotto():
    lottoLst = []
    count = 0
    while count <= 6:
        lottoNum = random.randint(1,49)
        if lottoNum not in lottoLst:
            lottoLst.append(lottoNum)
            count +=1
    lottoLst.sort()
    print(lottoLst)
    
def main():
    for i in range(1,6):
        lotto()
        
main()

3. 撰寫一程式，以隨機亂的方式產生100個介於1~1000的亂數，將他至放於 randLst 串列中。
然後印出第二小的數與第二大的數。數值可重複。

import random
randLst = []
for i in range(100):
    randNum = random.randint(1,1000)
    randLst.append(randNum)
    
randLst.sort()
for j in range(1,101):
    if j % 10 == 0:
        print('%4d' % (randLst[j-1]))
    else:
        print('%4d' % (randLst[j-1]) , end = ' ')
        
print()
print(randLst[1])
print(randLst[len(randLst)-2])


3. 撰寫一程式，以隨機亂的方式產生100個介於1~1000的亂數，將他至放於 randLst 串列中。
然後印出第二小的數與第二大的數。數值不可重複。

import random
randLst = []
count = 1
while count <=100:
    randNum = random.randint(1,1000)
    if randNum not in randLst:
        randLst.append(randNum)
        count += 1
        
randLst.sort()
for j in range(1,101):
    if j % 10 == 0:
        print('%4d' % (randLst[j-1]))
    else:
        print('%4d' % (randLst[j-1]) , end = '')
        
print()
print(randLst[1])
print(randLst[len(randLst) - 2])




'''

*檔案存取及例外處理
    ＠檔案運作的流程
        1. 使用open函式開啟檔案及設定模式。
        2. 使用寫入函式寫入檔案或讀取函式讀取檔案。
        3. 使用close函式關閉檔案。
        
    ＠開啟檔案
        1. open函式
            -> open (開啟的檔案,開啟模式)
                開啟的檔案：檔案的路徑及檔案全名
                開啟模式：W -> 寫入
                            檔案指標指向檔案開頭
                            並清除原檔案內容
                            檔案若不存在，則建立檔案
                        r -> 讀取
                            檔案指標指向檔案開頭
                            檔案若不存在，則生錯誤
                        a -> 附加
                            檔案指標指向檔案結尾
                            寫入的資料附加在原檔案後方
                            檔案若不存在，則建立檔案
                若存取的是二進位檔案，則將開啟模式參數後加b(rb,wb,ab)

    ＠讀取及寫入
        1. 寫入 -> 變數.write(寫入的資料)
        2. 讀取 -> 變數.read() -> 讀取所有內容
               -> 變數.read(n) -> 讀取 n 個字元
               -> 變數.readlines() -> 讀取所有內容
               -> 變數.readline() -> 讀取一行內容
               -> 變數.close() -> 關閉檔案
               
              
    
    ＠讀寫及開啟檔案的路徑
        1. 讀取路徑若未指定，則依系統預設路徑做為存取依據。(未給路徑，只給檔名)
        2. 自定路徑，程式碼撰寫時，路徑分隔符號以\\為主。
        
    ＠讀寫及開啟檔案的方式
        1. repr 函式：印出轉義字元
                        即字元資料若包含轉義字元(如\n)
                        則不執行轉義字元的功能，直接將其印出。
        2. w,r,a 參數後可加入'+'符號。即 w+,r+,a+，以讀寫模式開啟檔案。
        3. seek函式：移動指標
            -> 變數.seek(offset,where)
            offset:移動byte數
            where:從哪裡開始位移
                0:檔案頭
                1:目前位置
                2:檔案尾

'''

#Exercise========================================================

1. 透過 open 建立檔案(檔案不存在)
def main():
    outfile = open('\\Users\\martychen\\Desktop\\Python\\fruits.txt','w')
    outfile.write('banana\n')
    outfile.write('Grape\n')
    outfile.write('Orange\n')
    outfile.write('蘋果\n')
    outfile.write('芒果\n')
    outfile.close()
main()
    
    
 2. 
infile = open('\\Users\\martychen\\Desktop\\Python\\fruits.txt','r')
print('使用 readline()方法：')
line1 = infile.readline()
line2 = infile.readline()   
line3 = infile.readline()   
line4 = infile.readline()    

print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))     
    
print()
print(line1)
print(line2)
print(line3)
print(line4)
infile.close()


3. 
infile = open('\\Users\\martychen\\Desktop\\Python\\fruits.txt','r')
infile = infile.read()
print('使用 read()方法：')
print(repr(line1))
print(line1)
infile.close()

infile = open('\\Users\\martychen\\Desktop\\Python\\fruits.txt','r')
print('\n使用 readlines()方法：')
line1 = infile.readlines()
print(line1)
infile.close()

4. 
def main():
    infile = open('\\Users\\martychen\\Desktop\\Python\\fruits.txt','r')
    print('使用 read(3)方法：')
    line1 = infile.read(3)
    print(repr(line1))

    print('使用 read(8)方法：')
    line2 = infile.read(8)
    print(repr(line2))
    infile.close()
main()



5. 用迴圈讀取檔案內容
def main():
    infile = open('\\Users\\martychen\\Desktop\\Python\\fruits.txt','r')
    line = infile.readline()
    while line != '':
        print(line)
        line = infile.readline()
    infile.close()
main()

6. 
def main():
    outfile = open('\\Users\\martychen\\Desktop\\Python\\cities.txt','w')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    outfile.close()
    
    infile = open('\\Users\\martychen\\Desktop\\Python\\cities.txt','r')
    data = infile.read()
    print(data)
    infile.close()
main()

7. 
def main():
    outfile = open('\\Users\\martychen\\Desktop\\Python\\cities.txt','w+')
    outfile.write('Taipei\n')
    outfile.write('London\n')
    outfile.write('Coventry\n')
    outfile.seek(0,0)
    data = outfile.read()
    print(data)
    outfile.close()
    
main()   




'''

*檔案存取及例外處理
    ＠二進位檔案存取
        1. 載入 pickle模組 -> import pickle
        2. 使用 dump 函式寫入二進位資料
            -> pickle.dump(寫入的資料,寫入的檔案)
        3. 使用 load 函式讀取二進位資料
            -> pickle.load(讀取的檔案)
        
        數值以二進位模式操作可加快其效率。
        
        
    ＠例外(異常)處理，當程式出現異常運作時的處理機制。
     -> try:
            程式執行主體
        except 異常型態1:
            處理方式1
                .
                .
                .
        except 異常型態n:
            處理方式n   
        except: #空白：當以上異常總類都未發生(但還是有異常)
            處理方式n+1   
        else: #空白：當沒有異常發生
            處理方式n+2
        finally: #空白：最後一定會執行
            處理方式n+3   
            
        1. 異常型態
            EOFError : End Of File Error (檔案結尾錯誤)
            ZeroDivisionError(除法分母為0錯誤)
            SyntaxError(符號錯誤)
        

      
      
'''    
     

#Exercise========================================================

1. 二進位寫入/讀取
import pickle
def main():
    outbinfile = open('\\Users\\martychen\\Desktop\\Python\\binaryFile.dat','wb')
    pickle.dump(123, outbinfile)
    pickle.dump(77.7, outbinfile)
    pickle.dump('Python is good programming' , outbinfile)
    pickle.dump([11,22,33] , outbinfile)
    outbinfile.close()
    
    inbinfile = open('\\Users\\martychen\\Desktop\\Python\\binaryFile.dat','rb')
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    print(pickle.load(inbinfile))
    inbinfile.close()
main()
    
2. 二進位輸入
import pickle
def main():
    outfile = open('\\Users\\martychen\\Desktop\\Python\\score.txt','wb')
    data = eval(input('請輸入整數，輸入0結束輸入：'))
    while data != 0:
        pickle.dump(data, outfile)
        data = eval(input('請輸入整數，輸入0結束輸入：'))
    outfile.close()
    
    infile = open('\\Users\\martychen\\Desktop\\Python\\score.txt','rb')
    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile) , end =' ')
        except EOFError:
            end_of_file = True
    infile.close()
    print('\n所有資料已讀取')
main()        
  
3. 異常處理

def main():
    try:
        n1 ,n2 = eval(input('請輸入兩個數值，以逗號分隔：'))
        ans = n1/n2
        print('%d / %d = %d' , (n1,n2,ans))
    except ZeroDivisionError:
        print('除法分母不可為0!')
    except SyntaxError:
        print('輸入資料必須以逗號分隔!')
    except:
        print('輸入時發生錯誤')
    else:
        print('沒有異常錯誤！')
    finally:
        print('finally 子句被執行')
main()     
        


3. 撰寫一程式，以不定數迴圈輸入學生姓名，微積分與會計成績。
當輸入學生姓名為none時，則結束輸入的動作，並將上述輸入資料寫入名為students.dat的檔案中。

score = open('\\Users\\martychen\\Desktop\\Python\\students.txt','w')
while True:
    name = input('請輸入學生姓名：')
    calculus = input('請輸入微積分成績：')
    accounting = input('請輸入會計成績：')
    if name == 'none':
        break
    else:
        score.write(name)
        score.write(' ')
        score.write(calculus)
        score.write(' ')
        score.write(accounting)
        score.write(' ')
        score.write('\n')
score.close()       

4. 乘上題，讀取以建立的students的文字檔。

score = open('\\Users\\martychen\\Desktop\\Python\\students.txt','r')
line = score.readline()
while line != '':
    print(line)
    line = score.readline()
score.close()


5. 乘上題，讀取已建立的文字檔students.txt，並計算每位學生的平均成績。
微積分的比重是60%，會計比重是40%。

score = open('\\Users\\martychen\\Desktop\\Python\\students.txt','r')
info = score.readline()
while info != '': # 只要有讀到資料
    lst = info.split(' ') # 分割資料
    calculus = eval(lst[1]) # 放入串列
    accounting = eval(lst[2]) #放入串列
    average = calculus * 0.6 + accounting * 0.4 
    print('%10s:%.2f' % (lst[0] , average))
    info = score.readline()
score.close()

6. 乘上題，讀取已建立的文字檔students.txt，並顯示那位學生的微積分數最高。

score = open('\\Users\\martychen\\Desktop\\Python\\students.txt','r')
max = -1 # max 變數值設定 初始值
info = score.readline() 
while info != '':
    lst = info.split(' ')
    calculus = eval(lst[1])
    if calculus > max: #比較calculus 與 max的大小 , 若calculus >max,則將calculus值設定給max.
        max = calculus
        name = lst[0]
    info = score.readline()

print('微積分最高是 \n %10s: %3d。' % (name , max))
score.close()    
    
    
7. 乘上題， 讀取已建立的文字檔students.txt，並顯示那位學生的會計分數最低。

score = open('\\Users\\martychen\\Desktop\\Python\\students.txt','r')
min = 999 # max 變數值設定 初始值
info = score.readline() 
while info != '':
    lst = info.split(' ')
    accounting = eval(lst[2])
    if accounting < min: #比較calculus 與 max的大小 , 若calculus >max,則將calculus值設定給max.
        min = accounting
        name = lst[0]
    info = score.readline()

print('微積分最高是 \n %10s: %3d。' % (name , min))
score.close()    

8. 撰寫一程式，以不定數迴圈要求使用者輸入字串，檢視若字串是以B字元開頭，則加入lst串列中。
最後將其印出，當使用者輸入end時結束入動作。

lst =[]
while True:
    str = input('請輸入字串：')
    if str != 'end':
        if str.startswith('B'):
            lst.append(str)
    else:
        break
print(lst)
   


9. 撰寫一程式，輸入一個名為 str 的字串與欲尋找的字串，將找到的字串以'Bright'字串取代之。
若沒找到，則印出'is not found'訊息。

str = input('請輸入字串：')
fstr = input('請輸入找尋字串：')
if str.find(fstr) != -1:
    endStr = str.replace(fstr , 'Bright')
    print(endStr)

else:
    print(fstr + ' is not found')








'''

補充

*print:輸出單一項目如，變數，字串(字元)..等。多個項目以逗號隔開。
        輸出資料如需設定格式，則以 、格式字串1 格式字串2 % (資料1 , 資料2) 設定。
        

*排序
    ＠sort()：直接排序，直接在list中排序。改變原始排序。
    ＠sorted():排序後有結果，須以變數承接該結果，但不會影響元資料。
        sorted()預設是遞增。reverse = Fales。
                若要遞減，須下指令 reverse = True。
        
'''        
 
# Exercise==================================================================

       
a1=[5,4,6,95,25]
print(a1)
print(sorted(a1))
print(a1)
a1.sort(reverse = True) #遞減指令。
print(a1)    





members = [['Simom' ,'A' , 95],['Amy' , 'B' , 80],['Ruby' , 'C', 78],['Kelly' , 'B', 82]]
m_sort1 = sorted(members)
print(m_sort1)
print(members)
print(members[2][1]) #取出第2組第1個元素。

m_sort2 = sorted(members , key = lambda s1:s1[2]) 
#參數s1設定其值為s1的索引值2，即為members串列的第一層元素中的2者。
print(m_sort2)

m_sort2 = sorted(members , key = lambda s1:s1[2],reverse = True) # 遞減。
print(m_sort2)

# =============================================================================
# lambda(指令)：
#     僅一行
#     為簡化程式敘述使用
#     -> lambda 參數1,2.... : 運算,敘述A,B......
# =============================================================================
    
    
s = [20,30,10,40,90]
sort_s = sorted(range(len(s)), key = lambda a:s[a])
print(sort_s)


