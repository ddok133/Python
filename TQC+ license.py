TQC+ Python 3 程式語言認證

    ＠認證有效期 5 年
    ＠成績 滿分 100 分 / 及格 70 分
    ＠考試時間 100 分鐘
    ＠考題共九大題，除第四堤外，每題 20 分，其實各類每題 10 分。
    ＠考題類型 實作題 / 上機編寫
    ＠需前往TQC+網站註冊考生身分

Important questions:
102 / 104 / 109 / 110
202 / 204
308 / 
406 / 408 / 410
502 / 504 / 506 / 508 / 510
602 / 604 / 606

'''
TQC+ 程式語言Python 101 整數格式化輸出
'''
1. 題目說明:
請開啟PYD101.py檔案，依下列題意進行作答，輸入整數及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA101.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個整數

輸出說明
格式化輸出

輸入輸出範例
範例輸入
85
4
299
478
範例輸出
|   85     4|
|  299   478|
|85    4    |
|299   478  |



#PYA101

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
#靠右
print('|%5d %5d|' % (num1 , num2))
print('|%5d %5d|' % (num3 , num4))

#靠左
print('|%-5d %-5d|' % (num1 , num2))
print('|%-5d %-5d|' % (num3 , num4))


@@@!!!'''
* TQC+ 程式語言Python 102 浮點數格式化輸出
'''


1. 題目說明:
請開啟PYD102.py檔案，依下列題意進行作答，輸入浮點數及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA102.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
四個浮點數

輸出說明
格式化輸出

輸入輸出範例
範例輸入
23.12
395.3
100.4617
564.329
範例輸出
|  23.12  395.30|
| 100.46  564.33|
|23.12   395.30 |
|100.46  564.33 |


#PYA102

num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
#靠右
print('|%7.2f %7.2f|' % (num1 , num2))
print('|%7.2f %7.2f|' % (num3 , num4))

#靠左
print('|%-7.2f %-7.2f|' % (num1 , num2))
print('|%-7.2f %-7.2f|' % (num3 , num4))


'''
TQC+ 程式語言Python 103 字串格式化輸出
'''

1. 題目說明:
請開啟PYD103.py檔案，依下列題意進行作答，輸入單字及進行格式化輸出，使輸出值符合題意要求。作答完成請另存新檔為PYA103.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

3. 輸入輸出：
輸入說明
四個單字

輸出說明
格式化輸出

輸入輸出範例
範例輸入
I
enjoy
learning
Python
範例輸出
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
4. 評分項目：


#PYA103

word1 = input()
word2 = input()
word3 = input()
word4 = input()
#靠右
print('|%10s %10s|' % (word1 , word2))
print('|%10s %10s|' % (word3 , word4))

#靠左
print('|%-10s %-10s|' % (word1 , word2))
print('|%-10s %-10s|' % (word3 , word4))



@@@!!!'''
* TQC+ 程式語言Python 104 圓形面積計算
'''


1. 題目說明:
請開啟PYD104.py檔案，依下列題意進行作答，計算圓形之面積和周長，使輸出值符合題意要求。作答完成請另存新檔為PYA104.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。

提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
半徑

輸出說明
半徑
周長
面積

輸入輸出範例
範例輸入1
10
範例輸出1
Radius = 10.00
Perimeter = 62.83
Area = 314.16
範例輸入2
2.5
範例輸出2
Radius = 2.50
Perimeter = 15.71
Area = 19.63



#PYA104

import math
PI = math.pi #指定圓周率給PI
radius = eval(input())
print('Radius = %.2f' % radius)
print('Perimeter = %.2f' % (2*PI*radius))
print('Area = %.2f' % (pow(radius,2)*PI)) 

#pow(a,b)=a的b次方,是 math 函式裡的語法





import math
radius = eval(input())
print('Radius = %.2f' % radius)
print('Perimeter = %.2f' % (2*math.pi*radius))
print('Area = %.2f' % (pow(radius,2)*math.pi)) 



'''
TQC+ 程式語言Python 105 矩形面積計算
'''

1. 題目說明:
請開啟PYD105.py檔案，依下列題意進行作答，計算矩形之面積和周長，使輸出值符合題意要求。作答完成請另存新檔為PYA105.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
高、寬

輸出說明
高
寬
周長
面積

輸入輸出範例
範例輸入
23.5
19
範例輸出
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50


#PYA105

h = eval(input())
w = eval(input())
peri = (h+w)*2
area = h*w
print('Height = %.2f' % h)
print('Width = %.2f' % w)
print('Perimeter = %.2f' % peri)
print('Area = %.2f' % area)



'''
TQC+ 程式語言Python 106 公里英哩換算
'''

1. 題目說明:
請開啟PYD106.py檔案，依下列題意進行作答，計算選手賽跑每小時平均速度，使輸出值符合題意要求。作答完成請另存新檔為PYA106.py再進行評分。

2. 設計說明：
假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。

提示：輸出浮點數到小數點後第一位。

3. 輸入輸出：
輸入說明
x（min）、y（sec）、z（km）數值

輸出說明
速度

輸入輸出範例
範例輸入
10
25
3
範例輸出
Speed = 10.8


#PYA106

x = eval(input())
y = eval(input())
z = eval(input())
avgspeed = (z/1.6)/(60*x+y)*60*60
print('Speed = %.1f' % avgspeed)



'''
TQC+ 程式語言Python 107 數值計算
'''

1. 題目說明:
請開啟PYD107.py檔案，依下列題意進行作答，計算五個數字之數值、總和及平均數，使輸出值符合題意要求。作答完成請另存新檔為PYA107.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。

提示：總和與平均數皆輸出到小數點後第1位。

3. 輸入輸出：
輸入說明
五個數字

輸出說明
輸出五個數字
總和
平均數

輸入輸出範例
範例輸入1
20
40
60
80
100
範例輸出1
20 40 60 80 100
Sum = 300.0
Average = 60.0
範例輸入2
88.7
12
56
132.55
3
範例輸出2
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5


#PYA107
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
num5 = eval(input())

total_sum = num1+num2+num3+num4+num5
avg = total_sum/5
print(num1 , num2 , num3 , num4 , num5)
print('Sum = %.1f' % total_sum)
print('Average = %.1f' % avg)


'''
TQC+ 程式語言Python 108 座標距離計算
'''

1. 題目說明:
請開啟PYD108.py檔案，依下列題意進行作答，計算兩點座標及其距離，使輸出值符合題意要求。作答完成請另存新檔為PYA108.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。

提示1：歐式距離  
=
√
(
(
x
1
−
x
2
)
2
+
(
y
1
−
y
2
)
2
)
 
提示2：兩座標的歐式距離，輸出到小數點後第4位

3. 輸入輸出：
輸入說明
四個數字x1、y1、x2、y2

輸出說明
座標1
座標2
兩座標的歐式距離

輸入輸出範例
範例輸入
2
1
5.5
8
範例輸出
( 2 , 1 )
( 5.5 , 8 )
Distance = 7.8262


#PYA108


x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

dist = ((x2-x1)**2+(y2-y1)**2)**0.5
print('(' , x1 , ',' , y1 , ')')
print('(' , x2 , ',' , y2 , ')')
print('Distance = %.4f' % dist)



@@@!!!'''
TQC+ 程式語言Python 109 正五邊形面積計算
'''

1. 題目說明:
請開啟PYD109.py檔案，依下列題意進行作答，計算正五邊形之面積，使輸出值符合題意要求。作答完成請另存新檔為PYA109.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正五邊形面積的公式：  
A
r
e
a
=
(
5
∗
s
2
)
/
(
4
∗
t
a
n
(
p
i
/
5
)
)
 
提示3：輸出浮點數到小數點後第四位。

3. 輸入輸出：
輸入說明
正數s

輸出說明
正五邊形面積

輸入輸出範例
範例輸入
5
範例輸出
Area = 43.0119


#PYA109

import math

s = eval(input())
area = (5*pow(s,2))/(4*math.tan(math.pi/5))
print('Area = %.4f' % area)



@@@!!!'''
*TQC+ 程式語言Python 110 正n邊形面積計算
'''

1. 題目說明:
請開啟PYD110.py檔案，依下列題意進行作答，計算正n邊形面積，使輸出值符合題意要求。作答完成請另存新檔為PYA110.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。

提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下： 
A
r
e
a
=
(
n
∗
s
2
)
/
(
4
∗
t
a
n
(
p
i
/
n
)
)
 
提示3：輸出浮點數到小數點後第四位

3. 輸入輸出：
輸入說明
正數n、s

輸出說明
正n邊形面積

輸入輸出範例
範例輸入
8
6
範例輸出
Area = 173.8234


#PYA110

import math

n = eval(input())
s = eval(input())
area = (n*pow(s,2))/(4*math.tan(math.pi/n))
print('Area = %.4f' % area)





'''
TQC+ 程式語言Python 201 偶數判斷
'''

1. 題目說明:
請開啟PYD201.py檔案，依下列題意進行作答，判斷輸入值是否為偶數，使輸出值符合題意要求。作答完成請另存新檔為PYA201.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為偶數

輸入輸出範例
範例輸入1
56
範例輸出1
56 is an even number.
範例輸入2
21
範例輸出2
21 is not an even number.



#PYA201


num = int(input())
if num % 2 == 0:
    print('%d is an even number.' % num)

else:
    print('%d is not an even number.' % num)




@@@!!!'''
*TQC+ 程式語言Python 202 倍數判斷
'''

1. 題目說明:
請開啟PYD202.py檔案，依下列題意進行作答，判斷輸入值是否為3或5的倍數，使輸出值符合題意要求。作答完成請另存新檔為PYA202.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，顯示【x is a multiple of 3.】或【x is a multiple of 5.】；若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入x。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為3或者是5的倍數

輸入輸出範例
範例輸入1
55
範例輸出1
55 is a multiple of 5.
範例輸入2
36
範例輸出2
36 is a multiple of 3.
範例輸入3
92
範例輸出3
92 is not a multiple of 3 or 5.
範例輸入4
15
範例輸出4
15 is a multiple of 3 and 5.



#PYA202

num = int(input())
if (num %3 == 0) and (num %5 == 0):
    print('%d is a multiple of 3 and 5.' % num)
    
elif (num %3 == 0):
    print('%d is a multiple of 3.' % num)

elif (num %5 == 0):
    print('%d is a multiple of 5.' % num)
    
elif (num %3 == 0):
    print('%d is a multiple of 3.' % num)
    
else:
    print('%d is not a multiple of 3 or 5.' % num)
    



XX'''
TQC+ 程式語言Python 203 閏年判斷
'''

1. 題目說明:
請開啟PYD203.py檔案，依下列題意進行作答，判斷輸入值是否為閏年，使輸出值符合題意要求。作答完成請另存新檔為PYA203.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
判斷是否為閏年或平年

輸入輸出範例
範例輸入1
1992
範例輸出1
1992 is a leap year.
範例輸入2
2010
範例輸出2
2010 is not a leap year.




#PYA203

year = eval(input())   
if year %400 ==0 or (year %4 ==0 and year%100 !=0):
    print(year , 'is a leap year.')
else:
    print(year , 'is not a leap year.')




@@@!!!'''

*TQC+ 程式語言Python 204 算術運算
'''

1. 題目說明:
請開啟PYD204.py檔案，依下列題意進行作答，依輸入值進行算術運算，使輸出值符合題意要求。作答完成請另存新檔為PYA204.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果。

3. 輸入輸出：
輸入說明
兩個整數a、b，及一個算術運算子 (+、-、*、/、//、%）

輸出說明
運算結果 (無須做格式化)

輸入輸出範例
範例輸入
30
20
*
範例輸出1
600


#PYA204

a = eval(input())
b = eval(input())
opr = input()
ans = 0
if opr == '+' : ans = a+b
elif opr == '-' : ans = a-b
elif opr == '*' : ans = a*b
elif opr == '/' : ans = a/b
elif opr == '//' : ans = a//b
elif opr == '%' : ans = a%b

print(ans)


'''
TQC+ 程式語言Python 205 字元判斷
'''
1. 題目說明:
請開啟PYD205.py檔案，依下列題意進行作答，判斷輸入值的字元，使輸出值符合題意要求。作答完成請另存新檔為PYA205.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。例如：a為英文字母、9為數字、$為其它字元。

3. 輸入輸出：
輸入說明
一個字元

輸出說明
判斷是英文字母（包括大、小寫）、數字、或者其它字元

輸入輸出範例
範例輸入1
P
範例輸出1
P is an alphabet.
範例輸入2
@
範例輸出2
@ is a symbol.
範例輸入3
7
範例輸出3
7 is a number.


#PYA205

c = input()
if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
    print(c , 'is an alphabet.')   
elif ('0' <= c <= '9'):
    print(c , 'is a number.')
else:
    print(c , 'is a symbol.')    
    
    
'''

TQC+ 程式語言Python 206 等級判斷
'''

1. 題目說明:
請開啟PYD206.py檔案，依下列題意進行作答，判斷輸入值所對應的等級，使輸出值符合題意要求。作答完成請另存新檔為PYA206.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：

分　數	等級
80 ~ 100	A
70 ~ 79	B
60 ~ 69	C
<= 59	F
3. 輸入輸出：
輸入說明
一個整數

輸出說明
判斷輸入值所對應的等級

輸入輸出範例
範例輸入
79
範例輸出
B


    
    
#PYA206   
    
score = eval(input())
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif score <= 59:
    grade = 'F'
print(grade)
 
  
    
    
'''

TQC+ 程式語言Python 207 折扣方案
'''

1. 題目說明:
請開啟PYD207.py檔案，依下列題意進行作答，判斷輸入值之折扣並計算實付金額，使輸出值符合題意要求。作答完成請另存新檔為PYA207.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：

金　　額	折　扣
8,000（含）以上	9.5折
18,000（含）以上	9折
28,000（含）以上	8折
38,000（含）以上	7折
3. 輸入輸出：
輸入說明
一個數值，需大於8,000（含）以上

輸出說明
顯示折扣優惠後的實付金額（輸出不需指定小數點位數）

輸入輸出範例
範例輸入
12000
範例輸出
11400.0



#PYA207

cost = eval(input())
if cost >= 38000:
    pay = cost*0.7
elif cost >= 28000:
    pay = cost*0.8
elif cost >= 18000:
    pay = cost*0.9
elif cost >= 8000:
    pay = cost*0.95
print(pay)


'''
TQC+ 程式語言Python 208 十進位換算
'''
1. 題目說明:
請開啟PYD208.py檔案，依下列題意進行作答，依輸入值進行進位轉換，使輸出值符合題意要求。作答完成請另存新檔為PYA208.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。

提示：轉換規則 = 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F。

3. 輸入輸出：
輸入說明
一個數值

輸出說明
將此數值轉換成十六進位值

輸入輸出範例
範例輸入1
13
範例輸出1
D
範例輸入2
8
範例輸出2
8


#PYA208

num = eval(input())
if 0 <= num <= 9 : hex_num = num
elif num == 10 : hex_num = 'A'
elif num == 11 : hex_num = 'B'
elif num == 12 : hex_num = 'C'
elif num == 13 : hex_num = 'D'
elif num == 14 : hex_num = 'E'
elif num == 15 : hex_num = 'F'

print(hex_num)


'''
TQC+ 程式語言Python 209 距離判斷
'''

1. 題目說明:
請開啟PYD209.py檔案，依下列題意進行作答，計算輸入值之座標，使輸出值符合題意要求。作答完成請另存新檔為PYA209.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，判斷此點是否與點(5, 6)的距離小於或等於15，如距離小於或等於15顯示【Inside】，反之顯示【Outside】。

提示：計算平面上兩點距離的公式： 
√
(
x
1
−
x
2
)
2
+
(
y
1
−
y
2
)
2
 
3. 輸入輸出：
輸入說明
兩個數值x、y

輸出說明
小於或等於15輸出Inside；大於15輸出Outside

輸入輸出範例
範例輸入1
7
20
範例輸出1
Inside
範例輸入2
30
35
範例輸出2
Outside


#PYA209

x = eval(input())
y = eval(input())
dist = ((x-5)**2 + (y-6)**2)**0.5
if dist <= 15:
    print('Inside')
else:
    print('Outside')


'''
TQC+ 程式語言Python 210 三角形判斷
'''

1. 題目說明:
請開啟PYD210.py檔案，依下列題意進行作答，檢查輸入值是否可組成三角形，使輸出值符合題意要求。作答完成請另存新檔為PYA210.py再進行評分。

2. 設計說明：
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。若可以，則輸出該三角形之周長；否則顯示【Invalid】。

提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。

3. 輸入輸出：
輸入說明
三個正整數

輸出說明
可以組成三角形則輸出周長；否則顯示Invalid

輸入輸出範例
範例輸入1
5
6
13
範例輸出1
Invalid
範例輸入2
1
1
1
範例輸出2
3


#PYA210

side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

if side1 + side2 > side3 \
    and side1 + side3 > side2 \
    and side2 + side3 > side1:
    print(side1+side2+side3)
else:
    print('Invalid')
    
    
    
'''
TQC+ 程式語言Python 301 迴圈整數連加
'''
1. 題目說明:
請開啟PYD301.py檔案，依下列題意進行作答，依輸入值計算總和，使輸出值符合題意要求。作答完成請另存新檔為PYA301.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），利用迴圈計算從a開始連加到b的總和。例如：輸入a=1、b=100，則輸出結果為5050（1 + 2 + … + 100 = 5050）。

3. 輸入輸出：
輸入說明
兩個正整數（a、b，且a < b）

輸出說明
計算從a開始連加到b的總和

輸入輸出範例
範例輸入
66
666
範例輸出
219966


#PYA301

a = int(input())
b = int(input())
ans = 0

for i in range(a,b+1):
    ans += i
print(ans)


'''
TQC+ 程式語言Python 302 迴圈偶數連加
'''

1. 題目說明:
請開啟PYD302.py檔案，依下列題意進行作答，依輸入值計算偶數的總和，使輸出值符合題意要求。作答完成請另存新檔為PYA302.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），利用迴圈計算從a開始的偶數連加到b的總和。例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。

3. 輸入輸出：
輸入說明
兩個正整數（a、b，且a < b）

輸出說明
計算從a開始的偶數連加到b的總和

輸入輸出範例
範例輸入
14
1144
範例輸出
327714



#PYA302

a = int(input())
b = int(input())
ans = 0

for i in range(a,b+1):
    if i%2 == 0:
        ans += i
print(ans)

'''
TQC+ 程式語言Python 303 迴圈數值相乘
'''

1. 題目說明:
請開啟PYD303.py檔案，依下列題意進行作答，依輸入值以三角形的方式輸出此數相乘結果，使輸出值符合題意要求。作答完成請另存新檔為PYA303.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數（<100），然後以三角形的方式依序輸出此數的相乘結果。

提示：輸出欄寬為4，且需靠右對齊。

3. 輸入輸出：
輸入說明
一個正整數（<100）

輸出說明
輸入輸出範例
以三角形的方式依序輸出此數的階乘結果

範例輸入1
5
範例輸出1
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
範例輸入2
12
範例輸出2
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   6  12  18  24  30  36
   7  14  21  28  35  42  49
   8  16  24  32  40  48  56  64
   9  18  27  36  45  54  63  72  81
  10  20  30  40  50  60  70  80  90 100
  11  22  33  44  55  66  77  88  99 110 121
  12  24  36  48  60  72  84  96 108 120 132 144


#PYA303
  
num = int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print('%4d' % (i*j) , end = '')
    print()



'''
TQC+ 程式語言Python 304 迴圈倍數總和
'''

1. 題目說明:
請開啟PYD304.py檔案，依下列題意進行作答，依輸入值計算所有5之倍數總和，使輸出值符合題意要求。作答完成請另存新檔為PYA304.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
所有5之倍數數字總和

輸入輸出範例
範例輸入
21
範例輸出
50


#PYA304

a = int(input())
ans = 0
for i in range(1,a+1):
    if i%5 ==0:
        ans += i
print(ans)


'''
TQC+ 程式語言Python 305 數字反轉
'''

1. 題目說明:
請開啟PYD305.py檔案，依下列題意進行作答，將輸入值進行反轉，使輸出值符合題意要求。作答完成請另存新檔為PYA305.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一個正整數，將此數值以反轉的順序輸出。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
將此數值以反轉的順序輸出

輸入輸出範例
範例輸入1
31283
範例輸出1
38213
範例輸入2
1003120
範例輸出2
0213001




#PAY305

a = eval(input())
while a != 0:
    print(a%10 , end = '')
    a //= 10


'''
TQC+ 程式語言Python 306 迴圈階乘計算
'''

1. 題目說明:
請開啟PYD306.py檔案，依下列題意進行作答，依輸入值計算n!的值，使輸出值符合題意要求。作答完成請另存新檔為PYA306.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
計算n!的值

輸入輸出範例
範例輸入
15
範例輸出
1307674368000


#PYA306

n = eval(input())
result = 1
for i in range(1,n+1):
    result *=i
print(result)




XX'''
TQC+ 程式語言Python 307 乘法表
'''

1. 題目說明:
請開啟PYD307.py檔案，依下列題意進行作答，依輸入值計算n*n乘法表，使輸出值符合題意要求。作答完成請另存新檔為PYA307.py再進行評分。

2. 設計說明：
(1) 請使用迴圈敘述撰寫一程式，要求使用者輸入一個正整數n（n<10），顯示n*n乘法表。

(2) 每項運算式需進行格式化排列整齊，每個運算子及運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊不跳行。

3. 輸入輸出：
輸入說明
一個正整數n（n<10）

輸出說明
輸出格式化的n*n乘法表

輸入輸出範例
範例輸入1
3
範例輸出1
1 * 1 = 1   2 * 1 = 2   3 * 1 = 3   
1 * 2 = 2   2 * 2 = 4   3 * 2 = 6   
1 * 3 = 3   2 * 3 = 6   3 * 3 = 9   
範例輸入2
5
範例輸出2
1 * 1 = 1   2 * 1 = 2   3 * 1 = 3   4 * 1 = 4   5 * 1 = 5   
1 * 2 = 2   2 * 2 = 4   3 * 2 = 6   4 * 2 = 8   5 * 2 = 10  
1 * 3 = 3   2 * 3 = 6   3 * 3 = 9   4 * 3 = 12  5 * 3 = 15  
1 * 4 = 4   2 * 4 = 8   3 * 4 = 12  4 * 4 = 16  5 * 4 = 20  
1 * 5 = 5   2 * 5 = 10  3 * 5 = 15  4 * 5 = 20  5 * 5 = 25  


#PYA307

n = eval(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print('%-2d* %-2d= %-4d' % (j,i,(j*i)),end='')
    print()

???@@@!!!'''
TQC+ 程式語言Python 308 迴圈位數加總
'''

1. 題目說明:
請開啟PYD308.py檔案，依下列題意進行作答，將輸入值之每位數全部加總，使輸出值符合題意要求。作答完成請另存新檔為PYA308.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，要求使用者輸入一個數字，此數字代表後面測試資料的數量。每一筆測試資料是一個正整數（由使用者輸入），將此正整數的每位數全部加總起來。

3. 輸入輸出：
輸入說明
先輸入一個正整數代表後面測試資料的數量
依測試資料的數量，再輸入正整數的測試資料

輸出說明
將測試資料的每位數全部加總

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示 1
1
98765
Sum of all digits of 98765 is 35

輸入與輸出會交雜如下，輸出的部份以粗體字表示 2
3
32412
Sum of all digits of 32412 is 12
0
Sum of all digits of 0 is 0
769
Sum of all digits of 769 is 22


#PYA308

total = eval(input())
for i in range(total):
    num = eval(input())
    tem = num
    sum_digit = 0
    while tem != 0:
        sum_digit += tem%10
        tem //= 10
    print('Sum of all digits of %d is %d' % (num , sum_digit))


???'''
TQC+ 程式語言Python 309 存款總額
'''

1. 題目說明:
請開啟PYD309.py檔案，依下列題意進行作答，計算每個月的存款總額，使輸出值符合題意要求。作答完成請另存新檔為PYA309.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，提示使用者輸入金額（如10,000）、年收益率（如5.75），以及經過的月份數（如5），接著顯示每個月的存款總額。

提示：四捨五入，輸出浮點數到小數點後第二位。

舉例：
假設您存款$10,000，年收益為5.75%。
過了一個月，存款會是：10000 + 10000 * 5.75 / 1200 = 10047.92
過了兩個月，存款會是：10047.92 + 10047.92 * 5.75 / 1200 = 10096.06
過了三個月，存款將是：10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
以此類推。

3. 輸入輸出：
輸入說明
一個正整數（金額）、一個正數（收益率）及一個正整數（月份）

輸出說明
格式化輸出每個月的存款總額

輸入輸出範例
範例輸入
50000
1.3
5
範例輸出
Month 	  Amount
  1 	 50054.17
  2 	 50108.39
  3 	 50162.68
  4 	 50217.02
  5 	 50271.42



#PAY309

amount = eval(input())
rate = eval(input())
months = eval(input())
total = amount
print('%s \t  %s' % ('Month', 'Amount'))#此為格式化輸出之標頭
for i in range(1,months+1):
    total += total * rate/1200
    print('%3d \t %.2f' % (i, total))#此為格式化輸出之內容，需置於置於迴圈中
  
  
???'''
TQC+ 程式語言Python 310 迴圈公式計算
'''

1. 題目說明:
請開啟PYD310.py檔案，依下列題意進行作答，依公式計算總和，使輸出值符合題意要求。作答完成請另存新檔為PYA310.py再進行評分。

2. 設計說明：
請使用迴圈敘述撰寫一程式，讓使用者輸入正整數n (1 < n)，計算以下公式的總和並顯示結果：
1
1
+
√
2
+
1
√
2
+
√
3
+
1
√
3
+
√
4
+
.
.
.
+
1
√
n
−
1
+
√
n
 
提示：輸出結果至小數點後四位。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
代入公式計算結果

輸入輸出範例
範例輸入
8
範例輸出
1.8284
  
#PYA310

n = eval(input())
sum = 0
for i in range(2,n+1):
    sum += 1/((i-1)**0.5 + i**0.5)
print('%.4f' % sum)



'''
TQC+ 程式語言Python 401 最小值
'''

1. 題目說明:
請開啟PYD401.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA401.py再進行評分。

2. 設計說明：
請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值。

3. 輸入輸出：
輸入說明
十個數值

輸出說明
十個數值中的最小值

輸入輸出範例
範例輸入
23
57
48
2
99
70
9
65
35
88
範例輸出
2


#PYA401

total = 10
min_num = eval(input())
for i in range(total-1):
    num = eval(input())
    if  num < min_num:
        min_num = num
print(min_num)


'''
TQC+ 程式語言Python 402 不定數迴圈-最小值
'''

1. 題目說明:
請開啟PYD402.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA402.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。

3. 輸入輸出：
輸入說明
n個數值，直至9999結束輸入

輸出說明
n個數值中的最小值

輸入輸出範例
範例輸入
29
100
948
377
-28
0
-388
9999
範例輸出
-388


#PYA402

num = eval(input())
min_num = num
while num != 9999:
    num = eval(input())
    if  num < min_num:
        min_num = num
print(min_num)


XXX'''
TQC+ 程式語言Python 403 倍數總和計算
'''

403. 倍數總和計算
1. 題目說明:
請開啟PYD403.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA403.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數a、b（a<=b），輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和。

3. 輸入輸出：
輸入說明
兩個正整數a、b（a<=b）

輸出說明
格式化輸出兩個正整數之間4或9之倍數（包含a和b）
倍數個數
倍數總合

輸入輸出範例
範例輸入1
5
55
範例輸出1
8   9   12  16  18  20  24  27  28  32  
36  40  44  45  48  52  54  
17
513
範例輸入2
4
9
範例輸出2
4   8   9   
3
21


#PYA403

a = int(input())
b = int(input())
count = total_sum = 0 #下面迴圈會用到
time = 10 # 每行印10個

for i in range(a,b+1):
    if i %4 == 0 or i %9 == 0:
        print('%-4d' % i , end ='')
        total_sum += i # 把i加到總和
        count += 1 # 計算個數
        
        if count % time ==0:
            print() #換行

if count > 0 and count %10 != 0:
    print()
    
print('%d' % count)
print(total_sum)
    
    
    
'''
TQC+ 程式語言Python 404 數字反轉判斷
'''

1. 題目說明:
請開啟PYD404.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA404.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一個正整數，將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0。

3. 輸入輸出：
輸入說明
一個正整數或0

輸出說明
正整數反轉輸出。如輸入數值為0，輸出為0

輸入輸出範例
範例輸入1
31283
範例輸出1
38213
範例輸入2
0
範例輸出2
0
範例輸入3
135790
範例輸出3
097531


#PYA404 compare to PYA305

num = eval(input())

if num == 0:
    print(num)
else:
    while num != 0:
        print(num % 10 , end = '')
        num //=10

    
    
    
'''
TQC+ 程式語言Python 405 不定數迴圈-分數等級
'''

1. 題目說明:
請開啟PYD405.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA405.py再進行評分。

2. 設計說明：
請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），之後根據以下分數與GPA的對照表，印出其所對應的GPA。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：

分　數	GPA
90 ~ 100	A
80 ~ 89	B
70 ~ 79	C
60 ~ 69	D
0 ~ 59	E
3. 輸入輸出：
輸入說明
一個正整數，直至-9999結束輸入

輸出說明
依輸入值，輸出對應的GPA

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
75
C
39
E
100
A
85
B
65
D
-9999

    
#PYA405



@@@!!!'''
TQC+ 程式語言Python 406 不定數迴圈-BMI計算
'''

1. 題目說明:
請開啟PYD406.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA406.py再進行評分。

2. 設計說明：
請撰寫一程式，以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，印出BMI及相對應的BMI代表意義（State）。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：

BMI值	代表意義
BMI < 18.5	under weight
18.5 <= BMI < 25	normal
25.0 <= BMI < 30	over weight
30 <= BMI	fat
提示： 
B
M
I
=
體
重
(
k
g
)
/
身
高
2
(
m
)
 ，輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。

3. 輸入輸出：
輸入說明
兩個正數（身高cm、體重kg），直至-9999結束輸入

輸出說明
輸出BMI值
BMI值代表意義

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
176
80
BMI: 25.83
State: over weight
170
100
BMI: 34.60
State: fat
-9999


#PYA406

state = ''
height = eval(input())
while height != -9999:
    weight = eval(input())
    bmi = weight / (height / 100 * height / 100)
    if weight == -9999:
        break
    elif bmi >= 30:
        state = 'fat'
    elif bmi >= 25 and bmi < 29.9:
        state = 'over weight'
    elif bmi >= 18.5 and bmi <= 24.9:
        state = 'normal'
    elif bmi < 18.5:
        state = 'under weight'
    print('BMI: %.2F' % bmi)
    print('State: %s' % state) # print('State:' , state)
    
    height = eval(input())



#or 
    
height = eval(input())
while height != -9999:
    weight = eval(input())
    bmi = weight / (height / 100 * height / 100)
    if weight == -9999:
        break
    elif bmi >= 30:
        state = 'fat'
    elif bmi >= 25 and bmi < 29.9:
        state = 'over weight'
    elif bmi >= 18.5 and bmi <= 24.9:
        state = 'normal'
    elif bmi < 18.5:
        state = 'under weight'
    print('BMI: %.2F' % bmi)
    print('State:' , state)
    
    height = eval(input())

'''
TQC+ 程式語言Python 407 不定數迴圈-閏年判斷
'''

1. 題目說明:
請開啟PYD407.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA407.py再進行評分。

2. 設計說明：
(1) 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
(2) 假設此不定數迴圈輸入-9999則會結束此迴圈。

3. 輸入輸出：
輸入說明
一個正整數，直至-9999結束輸入

輸出說明
判斷是否為閏年或平年

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
2017
2017 is not a leap year.
2000
2000 is a leap year.
2016
2016 is a leap year.
2009
2009 is not a leap year.
2018
2018 is not a leap year.
-9999




#PYA407




@@@!!!'''
TQC+ 程式語言Python 408 奇偶數個數計算
'''

1. 題目說明:
請開啟PYD408.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA408.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

3. 輸入輸出：
輸入說明
十個整數

輸出說明
偶數的個數
奇數的個數

輸入輸出範例
範例輸入
69
48
19
91
83
22
18
37
82
40
範例輸出
Even numbers: 5
Odd numbers: 5


#PYA408


even = odd = 0 
for i in range(10): #迴圈執行10次
    a = int(input())
    if a%2 == 0: # 判斷除以2是否為0
        even += 1
    else:
        odd += 1
        
print('Even numbers:' , even)
print('Odd numbers:' , odd)



'''
TQC+ 程式語言Python 409 得票數計算
'''

1. 題目說明:
請開啟PYD409.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA409.py再進行評分。

2. 設計說明：
某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one won the election.】。

3. 輸入輸出：
輸入說明
五個正整數（1、2或其他）

輸出說明
每次投完後需印出目前每位候選人的得票數
五張選票投票完成，最後印出最高票者為當選人

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
2
Total votes of No.1: Nami =  0
Total votes of No.2: Chopper =  1
Total null votes =  0
1
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  0
8
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  1
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  2
Total null votes =  1
2
Total votes of No.1: Nami =  1
Total votes of No.2: Chopper =  3
Total null votes =  1
=> No.2 Chopper won the election.

程式執行狀況擷圖
下圖中的 粉紅色點 為 空格



#PYA409



@@@!!!'''
TQC+ 程式語言Python 410 繪製等腰三角形
'''
1. 題目說明:
請開啟PYD410.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA410.py再進行評分。

2. 設計說明：
請撰寫一程式，依照使用者輸入的n，畫出對應的等腰三角形。

3. 輸入輸出：
輸入說明
一個正整數

輸出說明
以 * 畫出等腰三角形
（每列最後一個 * 的右方無空白）

輸入輸出範例
範例輸入
7
範例輸出
      *
     ***
    *****
   *******
  *********
 ***********
*************


#PYA410

n = eval(input())
for i in range(0,n): #換行繼續
    for j in range(n-i,1,-1): #印空白
        print(' ', end='')
    for k in range(0,i*2+1,1): #印*
        print('*',end='')
    print() #換行



# or


n = eval(input())
for i in range(0,n): #換行
    for j in range(0,n-1-i): #印空白
        print(' ', end='')
    for k in range(0,i*2+1,1): #印＊
        print('*',end='')
    print()



@@@!!!'''
TQC+ 程式語言Python 502 乘積
'''

1. 題目說明:
請開啟PYD502.py檔案，依下列題意進行作答，依使用者輸入的數字作為參數傳遞並計算乘積，使輸出值符合題意要求。作答完成請另存新檔為PYA502.py再進行評分。

2. 設計說明：
請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。

3. 輸入輸出：
輸入說明
兩個整數

輸出說明
兩個整數相乘之乘積

輸入輸出範例
範例輸入
56
11
範例輸出
616


# PYA502


def compute(a, b):
    return a * b
num1 = eval(input())
num2 = eval(input())

print(compute(num1,num2))    
    
    
    


@@@!!!'''
TQC+ 程式語言Python 504 次方計算
'''

1. 題目說明:
請開啟PYD504.py檔案，依下列題意進行作答，依使用者輸入的整數作為參數傳遞進行公式計算，使輸出值符合題意要求。作答完成請另存新檔為PYA504.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳 
a
b
 的值。

3. 輸入輸出：
輸入說明
兩個整數

輸出說明
a
b
 的值

輸入輸出範例
範例輸入
14
3
範例輸出
2744

# PYA504

def compute(a, b):
    return a ** b
a = eval(input())
b = eval(input())

print(compute(a,b))




???@@@!!!'''
TQC+ 程式語言Python 506 一元二次方程式
'''

1. 題目說明:
請開啟PYD506.py檔案，依下列題意進行作答，依使用者輸入的數字作為參數傳遞進行公式計算，使輸出值符合題意要求。作答完成請另存新檔為PYA506.py再進行評分。

2. 設計說明：
請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式  
a
x
2
+
b
x
+
c
=
0
  的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】

提示：輸出有順序性

3. 輸入輸出：
輸入說明
三個整數，分別為a、b、c

輸出說明
代入一元二次方程式，回傳方程式解；如無解則輸出【Your equation has no root.】

輸入輸出範例
範例輸入1
2
-3
1
範例輸出1
1.0, 0.5
範例輸入2
9
9
8
範例輸出2
Your equation has no root.

# PYA506
# 定義解一元二次方程式的函式compute
# 回傳 -> return

def compute(a,b,c):
    delta = b**2 - 4 * a * c
    
    if delta <0:
        return None
    elif delta == 0:
        return -b / (2 * a)
    else:
        res1 = (-b + delta**0.5) / (2*a)
        res2 = (-b - delta**0.5) / (2*a)
        return str(res1) + ',' + str(res2)

a = eval(input())   
b = eval(input())   
c = eval(input())    
result = compute(a,b,c)
if result == None:
    print('Your equation has no root.')
else:
    print(result)
    


@@@!!!'''
TQC+ 程式語言Python 508 最大公因數
'''

1. 題目說明:
請開啟PYD05.py檔案，依下列題意進行作答，計算兩個正整數的最大公因數，使輸出值符合題意要求。作答完成請另存新檔為PYA508.py再進行評分。。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。

3. 輸入輸出：
輸入說明
兩個正整數（以半形逗號分隔）

x,y

輸出說明
最大公因數

輸入輸出範例
範例輸入1
12,8
範例輸出1
4
範例輸入2
4,6
範例輸出2
2
    
# PYA508
# =============================================================================
# 最大公因數(輾轉相除法)
# =============================================================================

def compute(a,b):
    gcd = 1 #最大公因數
    k =1 #公因數
    if a > 0 and b > 0: #正整數
        while k <= a and k <= b:
            if a % k == 0 and b % k == 0:
                gcd = k
            k += 1
        return gcd


x,y = eval(input())
gcd = compute(x,y) 
print(gcd)   




@@@!!!'''
TQC+ 程式語言Python 510 費氏數列
'''

1. 題目說明:
請開啟PYD05.py檔案，依下列題意進行作答，計算費氏數列，並依輸入的正整數回傳費氏數列前n個數值，使輸出值符合題意要求。作答完成請另存新檔為PYA510.py再進行評分。

2. 設計說明：
請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。

提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
F
0
=
0
 
F
1
=
1
 
F
n
=
F
n
−
1
+
F
n
−
2
 
3. 輸入輸出：
輸入說明
一個正整數num (num>=2)

輸出說明
依輸入值num，輸出費氏數列前num個的數值（每個數值後方為一個半形空格）

輸入輸出範例
範例輸入1
10
範例輸出1
0 1 1 2 3 5 8 13 21 34 
範例輸入2
20
範例輸出2
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 



# PYA510
# =============================================================================
# 費式數列：
#     由0,1開始
#     而後的每一個數值為其前二個數值的和
#     0,1,1,2,3,5,8,13,21,34.....
# =============================================================================
    
    
def compute(n):
    n1 = 0
    n2 = 1
    print('%d %d' % (n1 , n2) , end=' ')
    for i in range(3,n+1):
        n3 = n1+n2
        print('%d' % (n3) , end=' ')
        n1 = n2
        n2 = n3
        
num = int(input())
compute(num)
    

@@@!!!'''
TQC+ 程式語言Python 602 撲克牌總和
'''

1. 題目說明:
請開啟PYD602.py檔案，依下列題意進行作答，輸出並計算五張牌總和，使輸出值符合題意要求。作答完成請另存新檔為PYA602.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。

提示：J、Q、K以及A分別代表11、12、13以及1。

3. 輸入輸出：
輸入說明
5張牌數

輸出說明
5張牌的數值總和

輸入輸出範例
範例輸入
5
10
K
3
A
範例輸出
32



#PYA602
# =============================================================================
# 以迴圈方式執行5次加入輸入的數值到串列(使用append)
# 將A,J,Q,K,10 定義為一般數值
# 宣告串列cards[]儲存5個值
# 宣告變數esult儲存5個值的總和
# =============================================================================
cards = []
result = 0

for i in range(5):
    cards.append(input()) # 以迴圈方式執行5次加入輸入的數值到串列(使用append)
    
for i in range(5):
    if cards[i] == 'A' : result += 1
    elif cards[i] == 'J' : result += 11
    elif cards[i] == 'Q' : result += 12
    elif cards[i] == 'K' : result += 13 # 將A,J,Q,K定義為一般數值
    else:
        result += eval(cards[i]) # input()輸入值為字串，加總時需轉為數值(使用eval)

print(result)    
    
 

   
@@@!!!'''
TQC+ 程式語言Python 604 眾數
'''

1. 題目說明:
請開啟PYD604.py檔案，依下列題意進行作答，計算眾數及其出現的次數，使輸出值符合題意要求。作答完成請另存新檔為PYA604.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。

提示：假設樣本中只有一個眾數。

3. 輸入輸出：
輸入說明
十個整數

輸出說明
眾數
眾數出現的次數

輸入輸出範例
範例輸入
34
18
22
32
18
29
30
38
42
18
範例輸出
18
3
    
    
#PYA604


size = 10 # 設定樣本數=10
sample =[] # 設定儲存樣本數的串列(sample)
count = [0]*size #設定計算的次數的串列 count ＝「0,0,0,0,0,0,0,0,0,0] (儲存出現次數最多的數值次數)

for i in range(size):  
    num = int(input()) # 以迴圈輸入10個數值，加入到串列  
    
    sample.append(num)
    count[sample.index(num)] += 1 # 傳回參數指定之元素在串列中第一次出現的索引
    
num_occu = max(count)

print(sample[count.index(num_occu)]) # count 串列中元素最大值，數值出現最多的次數。
print(num_occu)




???@@@!!!'''
TQC+ 程式語言Python 606 二維串列行列數
'''

1. 題目說明:
請開啟PYD606.py檔案，依下列題意進行作答，印出串列的值，使輸出值符合題意要求。作答完成請另存新檔為PYA606.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入兩個正整數rows、cols，分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。
串列元素[row][col]所儲存的數字，其規則為：row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。
接著以該串列作為參數呼叫函式compute()輸出串列。

提示：欄寬為4。

3. 輸入輸出：
輸入說明
兩個正整數（rows、cols）

輸出說明
格式化輸出row、col的交點值

輸入輸出範例
範例輸入
5
10
範例輸出
   0   1   2   3   4   5   6   7   8   9
  -1   0   1   2   3   4   5   6   7   8
  -2  -1   0   1   2   3   4   5   6   7
  -3  -2  -1   0   1   2   3   4   5   6
  -4  -3  -2  -1   0   1   2   3   4   5



# PYA606
  
def compute(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])): # 以迴圈產生二維串列
            print('%4d' % lst[i][j] , end ='')
        print()
        
row = eval(input()) #代表第一維 (列)
column = eval(input()) #代表第二維 (欄)
lst = []

for i in range(row):
    lst.append([])
    for j in range(column):
        lst[i].append(j-i)

compute(lst)



@@@!!!'''
TQC+ 程式語言Python 608 最大最小值索引
'''

1. 題目說明:
請開啟PYD608.py檔案，依下列題意進行作答，建立3*3矩陣並輸出矩陣最大值與最小值的索引，使輸出值符合題意要求。作答完成請另存新檔為PYA608.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

3. 輸入輸出：
輸入說明
九個整數

輸出說明
矩陣最大值及其索引
矩陣最小值及其索引

輸入輸出範例
範例輸入
6
4
8
39
12
3
-3
49
33
範例輸出
Index of the largest number 49 is: (2, 1)
Index of the smallest number -3 is: (2, 0)



# PYA608
# =============================================================================
# 以條件式以較最大最小值
# 比較大小的原則
# 先設定一個比較值，如最大值max(通常為0)。
# 若 a1 > max , 則將 a1 指定給max(max=a1)。
# 否則維持原max值不變。
# =============================================================================

size = 3
mat = []

for i in range(size):
    mat.append([]) # 先給空字串
    for j in range(size):
        mat[i].append(eval(input())) # 輸入3次3個數值。9個不重複的數值到串列mat[]
        
max_num = min_num = mat[0][0] # 設定數值＝0
max_index = min_index = [0 , 0] # 設定索引=0

for i in range(size): # 判斷最大值與最小值
    for j in range(size):
        if mat[i][j] > max_num:
            max_num = mat[i][j]
            max_index = [i , j]
        elif mat[i][j] < min_num:
            min_num = mat[i][j]
            min_index = [i , j]
            
print('Index of the largest number %d is: (%d, %d)' % \
      (max_num , max_index[0] , max_index[1]))
print('Index of the smallest number %d is: (%d, %d)' % \
      (min_num , min_index[0] , min_index[1]))

        
    
# or
    
lst = []
for i in range(9):
    n = int(input())
    lst.append(n)
    
maxr = lst.index(max(lst))//3
maxc = lst.index(max(lst))%3
minr = lst.index(min(lst))//3
minc = lst.index(min(lst))%3
        
print('Index of the largest number' , max(lst) , 'is:' , (maxr , maxc))       
print('Index of the smallest number' , min(lst) , 'is:' , (minr , minc))        
        
        
@@@!!!'''
TQC+ 程式語言Python 610 平均溫度
'''

1. 題目說明:
請開啟PYD610.py檔案，依下列題意進行作答，依輸入值計算四週的平均溫度及最高、最低溫度，使輸出值符合題意要求。作答完成請另存新檔為PYA610.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。

提示1：平均溫度輸出到小數點後第二位。
提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

3. 輸入輸出：
輸入說明
四週各三天的溫度

輸出說明
平均溫度
最高溫度
最低溫度

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
下圖中的 粉紅色點 為 空格

# PYA610

week = 4
day = 3
temp =[]

for i in range(week):
    temp.append([])
    print('Week %d:' % (i+1))
    for j in range(day):
        temp[i].append(eval(input('Day %d:' % (j+1))))
        
comb = []
for i in range(week):
    comb.extend(temp[i]) # 將串列 temp 中所有的元素加入到串列 comb 串列, 執行運算。
     
avg = sum(comb) / (week * day)
print('Average: %.2f' % avg)
print('Highest:' , max(comb))
print('Lowest:' , min(comb))



@@@!!!'''
TQC+ 程式語言Python 702 數組合併排序
'''


1. 題目說明:
請開啟PYD702.py檔案，依下列題意進行作答，將兩數組合併並進行排序，使輸出值符合題意要求。作答完成請另存新檔為PYA702.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

3. 輸入輸出：
輸入說明
兩個數組，直至-9999結束輸入

輸出說明
排序前的數組
排序後的串列

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create tuple1:
9
0
-1
3
8
-9999
Create tuple2:
28
16
39
56
78
88
-9999
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]


#PYA702

tup1 = ()
tup2 = ()

print('Create tuple1:')
while True: # 使用 while 迴圈可設定條件始終成立，一直執行一直執行（While Ture)。
    num = eval(input())
    if num == -9999: #輸入-9999結束重複執行。 ＃將結束以條件式宣告。
        break 
    tup1 += (num,) # 類似append , 語法就是這樣下 (num ,) or (7,6) or (8,)
    
print('Create tuple2:')
while True:
    num = eval(input())
    if num == -9999: #輸入-9999結束重複執行
        break
    tup2 += (num,)
    
tup_comb = tup1 + tup2 # 兩數組相加可使用 ＋ 符號。(數組沒有 append 函式)

print('Combined tuple before sorting:' , tup_comb)

lst_comb = list(tup_comb) #將數組轉為串列。
print('Combined list after sorting:' , sorted(lst_comb))        

# 數組內容不可變動，通常轉換為串列後再進行運算或執行處理。如排序：函式 sorted。




@@@!!!'''
TQC+ 程式語言Python 704 集合條件判斷
'''


1. 題目說明:
請開啟PYD704.py檔案，依下列題意進行作答，將整數儲存至集合（set）中並進行條件判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA704.py再進行評分。

2. 設計說明：
請撰寫一程式，輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。

3. 輸入輸出：
輸入說明
輸入n個整數至集合，直至-9999結束輸入

輸出說明
集合的長度
集合中的最大值
集合中的最小值
集合內的整數總和

輸入輸出範例
範例輸入
34
-23
29
7
0
-1
-9999
範例輸出
Length: 6
Max: 34
Min: -23
Sum: 46


# PYA704

num = set() # 設定 num 為空集合

while True:
    inp = eval(input())
    if inp == -9999:
        break
    num.add(inp) #集合加資料用add函式： 集合名稱.add(資料)
    
print('Length:' , len(num)) #len(x) 求x之長度(個數)
print('Max:' , max(num)) #max(x) 求x之最大值
print('Min:' , min(num)) #min(x) 求x之最小值
print('Sum:' , sum(num)) #sum(x) 求x之總和




???@@@!!!'''
TQC+ 程式語言Python 706 全字母句
'''

Python 3
1. 題目說明:
請開啟PYD706.py檔案，依下列題意進行作答，進行全字母句之判斷，使輸出值符合題意要求。作答完成請另存新檔為PYA706.py再進行評分。

2. 設計說明：
全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子。請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）。

提示：不區分大小寫字母

3. 輸入輸出：
輸入說明
先輸入一個正整數表示測試資料筆數，再輸入測試資料

輸出說明
輸入的資料是否為全字母句

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示 第1組
3
The quick brown fox jumps over the lazy dog
True
Learning Python is funny
False
Pack my box with five dozen liquor jugs
True

輸入與輸出會交雜如下，輸出的部份以粗體字表示 第2組
2
Quick fox jumps nightly above wizard
True
These can be weapons of terror
False



# PYA707

num_alph = 26 # 英文字母26個
k = eval(input())

for i in range(k): # 以迴圈輸入測試英文句子(次數)
    sentence = input() # 設定一變數sentence 儲存輸入的英文句子
    alphabet = set(sentence.lower()) # 將英文句子轉換為全部小寫，並設定給集合。
    alphabet.remove(' ') # 移除空白字元。(使用集合的 remove()函式)
    print(len(alphabet) == num_alph)
    # 以比較運算子 == 判斷集合中的元素長度是否等於26。集合中的元素是不會重複的，若重複只取第一個。
    


???@@@!!!'''
TQC+ 程式語言Python 708 詞典合併
'''

1. 題目說明:
請開啟PYD708.py檔案，依下列題意進行作答，進行兩詞典合併，使輸出值符合題意要求。作答完成請另存新檔為PYA708.py再進行評分。

2. 設計說明：
請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。

3. 輸入輸出：
輸入說明
輸入兩個詞典，直至end結束輸入

輸出說明
合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Create dict1:
Key: a
Value: apple
Key: b
Value: banana
Key: d
Value: durian
Key: end
Create dict2:
Key: c
Value: cat
Key: e
Value: elephant
Key: end
a: apple
b: banana
c: cat
d: durian
e: elephant

程式執行狀況擷圖
下圖中的 粉紅色點 為 空格


# PYA708
# =============================================================================
# 定義函式，輸入詞典的 key and value
# 呼叫函式2次建立2個詞典
# 複製詞典：copy函式 -> 詞典名.copy()
# 更新詞典：update函式 -> 詞典1.update(詞典2) 以詞典2更新詞典1，即兩詞典合併。
# 詞典排序：使用sorted 函式
# =============================================================================

def compute():
    dic = {}
    while True:
        key = input('Key: ')
        if key == 'end':
            return dic
        
        value = input('Value: ')
        dic[key] = value

print('Create dict1:')
dict1 = compute()

print('Create dict2:')
dict2 = compute()

merge_dict = dict1.copy()
merge_dict.update(dict2)
sortedDict = sorted(merge_dict)

for i in sortedDict: # (0 , sortedDict元素個數 -1, 12)
    print('%s: %s' % (i , merge_dict[i]))




???@@@!!!'''
TQC+ 程式語言Python 710 詞典搜尋
'''
1. 題目說明:
請開啟PYD710.py檔案，依下列題意進行作答，為一詞典輸入資料並進行搜尋，使輸出值符合題意要求。作答完成請另存新檔為PYA710.py再進行評分。

2. 設計說明：
請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），再輸入一鍵值並檢視此鍵值是否存在於該詞典中。

3. 輸入輸出：
輸入說明
先輸入一個詞典，直至end結束輸入，再輸入一個鍵值進行搜尋是否存在

輸出說明
鍵值是否存在詞典中

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
Key: 123-4567-89
Value: Jennifer
Key: 987-6543-21
Value: Tommy
Key: 246-8246-82
Value: Kay
Key: end
Search key: 246-8246-82
True



# PAY710

my_dict = {}

while True:
    key = input('Key: ')
    if key == 'end':
        break
    value = input('Value: ')
    my_dict[key] = value
    
search_key = input('Search key: ')
print(search_key in my_dict) #使用 in 運算子。a in b : a 是否在 b 內。



@@@!!!'''
TQC+ 程式語言Python 802 字元對應
'''
1. 題目說明:
請開啟PYD802.py檔案，依下列題意進行作答，顯示字串每個字元對應的ASCII碼及其總和，使輸出值符合題意要求。作答完成請另存新檔為PYA802.py再進行評分。

2. 設計說明：
請撰寫一程式，要求使用者輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
依序輸出字串中每個字元對應的ASCII碼
每個字元ASCII碼的總和

輸入輸出範例
範例輸入
Kingdom
範例輸出
ASCII code for 'K' is 75
ASCII code for 'i' is 105
ASCII code for 'n' is 110
ASCII code for 'g' is 103
ASCII code for 'd' is 100
ASCII code for 'o' is 111
ASCII code for 'm' is 109
713



# PAY802

# =============================================================================
# ord(c) : c 為字元參數。取得其 unicode 碼(10進位)
# ASCII碼 表示法為10進位數值(共0~127)，代表英文大小寫字母, 符號,數字及控制字串。
# unicode碼(萬國碼) 可表示到 2的16次方=65536個字元，涵蓋ASCII碼。
# =============================================================================



total = 0
string = input()

for i in range(0,len(string)): #以迴圈的方式取出輸入字串的每一個字元。
    num = ord(string[i]) #字串建立後即自動為每個字元賦予位置索引值(從0起算)。
    print("ASCII code for '%s' is %d" % (string[i] , num))
    total += num

print(total)
    



@@@!!!'''
TQC+ 程式語言Python 804 大寫轉換
'''
1. 題目說明:
請開啟PYD804.py檔案，依下列題意進行作答，將字串轉換成大寫及首字大寫，使輸出值符合題意要求。作答完成請另存新檔為PYA804.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一字串，分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。

3. 輸入輸出：
輸入說明
一個字串

輸出說明
全部大寫
每個字的第一個字母大寫

輸入輸出範例
範例輸入
learning python is funny
範例輸出
LEARNING PYTHON IS FUNNY
Learning Python Is Funny
    
    
    
# PAY804

st = input()

str1 = st.upper() 
print(str1) 

str2 = st.title()
print(str2)
    
    


@@@!!!'''
TQC+ 程式語言Python 806 字元次數計算
'''
1. 題目說明:
請開啟PYD806.py檔案，依下列題意進行作答，計算指定字元出現的次數，使輸出值符合題意要求。作答完成請另存新檔為PYA806.py再進行評分。

2. 設計說明：
請撰寫一程式，讓使用者輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()的函式，此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。

3. 輸入輸出：
輸入說明
一個字串和一個字元

輸出說明
字串中指定字元出現的次數

輸入輸出範例
範例輸入
Our country is beautiful
u
範例輸出
u occurs 4 time(s)



# PAY806

def compute(sentence , w): #宣告函式，帶入的參數為一字串，一字元。
    return sentence.count(w) #字串.count(字元)：求字元在字串中的個數。
sentence = input()
word = input()

print(word , 'occurs' , compute(sentence , word) , 'time(s)')


# =============================================================================
# if no use def
# =============================================================================


s = input()
w = input()
print(w , 'occurs' , s.count(w) , 'time(s)')
print(s.count(w))





???@@@!!!'''
TQC+ 程式語言Python 808 社會安全碼
'''

1. 題目說明:
請開啟PYD808.py檔案，依下列題意進行作答，進行社會安全碼格式檢查，使輸出值符合題意要求。作答完成請另存新檔為PYA808.py再進行評分。

2. 設計說明：
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。

3. 輸入輸出：
輸入說明
一個字串（格式為ddd-dd-dddd，d表示數字）

輸出說明
判斷是否符合SSN格式

輸入輸出範例
範例輸入1
329-48-4977
範例輸出1
Valid SSN
範例輸入2
837-a3-3000
範例輸出2
Invalid SSN




# PAY808

s = input()

isSSN = (len(s) == 11) # 安全碼共11位，判斷輸入的字串長度是否等於11，將結果設定給變數isSSN(True / False)。
if isSSN: # 將isSSN設為條件式，若為True。
    for i in range(len(s)): # 則以11位長度做為迴圈的執行次數。
        if i == 3 or i == 6: # 在字串的位置(索引)3及6處，判斷是否為減號。1. 以反向判斷，若符合條件，則將isSSN設為False並結束跳離。
            if s[i] != '-':
                isSSN = False
                break
        elif not s[i].isdigit(): # 以字串的isdifit()函式。2. 判斷字串中的某字元 s[i] 是否為數值，若符合條件，則將isSSN為false並結束跳離。    
            isSSN = False
            break
                                # 1,2:判斷輸入的字元是否為減號及非數字字元。
if isSSN:
    print('Valid SSN')
    
else:
    print('Invalid SSN')


???@@@!!!'''
TQC+ 程式語言Python 810 最大值與最小值之差
'''
1. 題目說明:
請開啟PYD810.py檔案，依下列題意進行作答，找出串列數字中最大值和最小值之間的差，使輸出值符合題意要求。作答完成請另存新檔為PYA810.py再進行評分。

2. 設計說明：
請撰寫一程式，首先要求使用者輸入正整數k（1 <= k <= 100），代表有k筆測試資料。每一筆測試資料是一串數字，每個數字之間以一空白區隔，請找出此串列數字中最大值和最小值之間的差。

提示：差值輸出到小數點後第二位。

3. 輸入輸出：
輸入說明
先輸入測試資料的筆數，再輸入每一筆測試資料（一串數字，每個數字之間以空白區隔）

輸出說明
每個串列數字中，最大值和最小值之間的差

輸入輸出範例
輸入與輸出會交雜如下，輸出的部份以粗體字表示
4
94 52.9 3.14 77 46
90.86
-2 0 1000.34 -14.4 89 50
1014.74
87.78 33333 29.3
33303.70
9998 9996 9999
3.00


# PAY810

k = eval(input())

for i in range(k): # 以迴圈帶入輸入次數執行
    str_num = input() # 設定給str_num 變數為串列中的元素(數值加空白)
    str_num_list = str_num.split(' ') # 將str_num中以空白做為分割，存入str_num_list變數中。
    str_num_list = [eval(x) for x in str_num_list]  # 以迴圈 for x in str_num_list，將str_num_list串列中每一個元素取出轉換為數值eval(x)。
    print('%.2f' % (max(str_num_list) - min(str_num_list))) # 以max() , min() 求得str_num_list 中的最大,最小值。



      
@@@!!!'''
TQC+ 程式語言Python 902 資料加總
'''
1. 題目說明:
請開啟PYD902.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA902.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。檔案讀取完成後要關閉。

3. 輸入輸出：
輸入說明
讀取read.txt的內容（內容為數字，以空白分隔）

輸出說明
總和

輸入輸出範例
範例輸入
無

範例輸出
660


# PAY902

f = open('read.txt' , 'r')
data = f.read() # 讀取的文字檔(txt)，為一串列格式(data)。
f.close()


num = data.split(' ') # 以空白分割每一個資料，存入num。
total = 0
for i in range(0,len(num)): # 以迴圈取出num串列中的每一個元素。轉換為數值後執行加總運算。
    total += eval(num[i])
    
print(total)





# =============================================================================
# 迴圈補充語法

 1.
 s = 'as','e','r','fs'
 for s1 in s:
     print(s1)

2.
odd_num = list(range(1,10,2))
print(odd_num)

odd_num = tuple(range(1,10,2))
print(odd_num)

# =============================================================================





???@@@!!!'''
TQC+ 程式語言Python 904 資料計算
'''
1. 題目說明:
請開啟PYD904.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA904.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、所有人的平均身高、平均體重以及最高者、最重者。

提示：輸出浮點數到小數點後第二位。

3. 輸入輸出：
輸入說明
讀取read.txt（每一行的格式為名字和身高、體重，以空白分隔）

輸出說明
輸出檔案中的內容
平均身高
平均體重
最高者
最重者

輸入輸出範例
範例輸入
無

範例輸出
Ben 175 65

Cathy 155 55

Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg



# PYA904

# =============================================================================
# with 運算式/敘述 as 變數:
#     將 with 後的 運算/敘述 得到的結果(參數)指定給變數。 
#     執行後會關閉變數代表的資料。
# =============================================================================


data = []

with open('read.txt' , 'r') as file : #將開啟的檔案設定給file。
    for line in file: # 將file帶入迴圈。
        print(line) # 印出每一個file元素。  
        
        tmp = line.strip('/n').split(' ') # 移除換行符號 "line.strip('/n')"，並用空白分割 line 串列的資料，分別存入tmp串列(姓名,身高,體重)。
        tmp = [tmp[0] , eval(tmp[1]) , eval(tmp[2])]
        data.append(tmp)
        
name = [data[x][0] for x in range(len(data))]
height = [data[x][1] for x in range(len(data))] 
weight = [data[x][2] for x in range(len(data))]    

print('Average height: %.2f' % (sum(height)/len(height)))
print('Average weight: %.2f' % (sum(weight)/len(weight)))

max_h = max(height)
max_w = max(weight)

print('The tallest is %s with %.2fcm' % (name[height.index(max_h)] , max_h))
print('The heaviest is %s with %.2fkg' % (name[weight.index(max_w)] , max_w))
    



@@@!!!'''
TQC+ 程式語言Python 906 字串資料取代
'''

1. 題目說明:
請開啟PYD906.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA906.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，data.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。

3. 輸入輸出：
輸入說明
輸入data.txt及兩個字串（分別為s1、s2，字串s1被s2取代）

輸出說明
輸出檔案中的內容
輸出取代指定字串後的檔案內容

輸入輸出範例
範例輸入
data.txt
pen
sneakers
範例輸出
=== Before the replacement
watch shoes skirt
pen trunks pants
=== After the replacement
watch shoes skirt
sneakers trunks pants

    
# PAY906

# =============================================================================
# 列印取代前的資料
# 檔案開啟後讀取再關閉
# 
# replace(字串1 , 字串2) : 以字串2取代字串1。取代後存入新檔案(new_data)
# 
# 將新檔案new_data 寫入輸出檔 outfile
# =============================================================================

f_name = input()
str_old = input()
str_new = input()

infile = open(f_name , 'r')
data = infile.read()

print('=== Before the replacement')
print(data)
infile.close()

print('=== After the replacement')
new_data = data.replace(str_old , str_new)
print(new_data)

outfile = open(f_name,'w')
outfile.write(new_data)
outfile.close()




???@@@!!!'''
TQC+ 程式語言Python 908 單字次數計算

1. 題目說明:
請開啟PYD908.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA908.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.txt檔案需為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）

3. 輸入輸出：
輸入說明
讀取read.txt的內容，以及檔案中某單字出現的次數

輸出說明
輸出符合次數的單字，並依單字的第一個字母大小排序

輸入輸出範例
範例輸入
read.txt
3
範例輸出
a
is
programming

'''

# PYA908

# =============================================================================
# 字典名.item():傳回字典中所有的 key and value
# =============================================================================

1.
f_name = input()
n = int(input())
word_dict = dict()

with open(f_name , 'r') as file: # 讀取檔案，並命名為file。
    for line in file: #以迴圈方式逐一讀取file內容，去除換行符號，以空格分割，設定為word。
        word = line.strip('\n').split(' ')
        
    for x in word:
        if x in word_dict:
            word_dict[x] +=1
        else:
            word_dict[x] = 1
            
word_list = word_dict.items() #取出字典中所有 key 及 value 值，設定給word_list。
wordQTY = [x for (x, y) in word_list if y == n]
# 利用迴圈以輸入的次數值做為終止值，取出word_list中的字詞wordQTY，以x帶入迴圈中，若符合存在於word，則將word_dict[x] 加1。
sortedword = sorted(wordQTY) #最後將 wordQTY(即取出符合出現次數) 排序(sorted)並印出。

for x in sortedword:
    print(x)



2.
fn = input()  # 輸入的檔案名稱 read.txt
n = int(input()) #輸入的次數
with open(fn , 'r' , encoding='UTF-8') as fp:
    data = sorted(fp.read().split()) # 讀取的檔案內容以空白分割後排序。
    
for i in sorted(set(data)):
    if data.count(i) == n:
        print(i)
    




















@@@!!!'''
TQC+ 程式語言Python 910 學生基本資料
'''
1. 題目說明:
請開啟PYD910.py檔案，依下列題意進行作答，使輸出值符合題意要求。作答完成請另存新檔為PYA910.py再進行評分。

請注意：資料夾或程式碼中所提供的檔案路徑，不可進行變動，read.dat檔案為UTF-8編碼格式。

2. 設計說明：
請撰寫一程式，要求使用者讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄。請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。

3. 輸入輸出：
輸入說明
讀取read.dat

輸出說明
讀取檔案內容，並格式化輸出男生人數和女生人數

輸入輸出範例
範例輸入
無

範例輸出
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文
Number of males: 3
Number of females: 2



    
#PYA910 


    
f_name = 'read.dat'
c_male = c_female = 0

with open(f_name , 'rb') as file: #將檔案以二進位方式開啟，並設定給file變數。
    for line in file: #以迴圈將檔案(file)資料以utf-8格式讀取，存入row變數(列資料)。
        row = line.decode('utf-8') # -> 資料.decode(編碼格式) : 以編碼格式讀取資料。
        print(row)
        row = row.strip('\n').split(' ') # 去除rpw資料中的換行符號，並以空白分割存回給row變數。
        
        if row[2] == '1':
            c_male += 1
        elif row[2] == '0':
            c_female += 1

print('Number of males:' , c_male)
print('Number of females:' , c_female)


# =============================================================================
# row變數即為列資料
# row[0]:學號
# row[1]:姓名
# row[2]:性別
# row[3]:科系
# 
# 以條件判斷row[2]資料若為字元1，則將男性變數c_male值加1。否則將女性變數c_female值加1。
# =============================================================================







































