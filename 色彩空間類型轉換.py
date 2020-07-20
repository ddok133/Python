'''
# =============================================================================
#                              DATE : 20200717
# =============================================================================
'''


＊色彩空間類型轉換
    ＠RGB色彩空間：RGB三者重要性相等，但忽略亮度資訊。
      為硬體角度的色彩模型，以人眼觀看，存在一定差異程度。

    ＠HSV色彩空間：視覺感知的色彩模型，以心理學及視覺角度，指出人類視覺感知包含三部分。
        1. 色調(色相) Hue : 光的顏色
            設定值範圍 0~360 (0紅 , 60黃 , 120綠 , 180青 , 240藍 , 300品紅)
        2. 飽和度 Saturation : 色彩深淺程度
            唯一比例值，範圍 0~1，是色彩純度值與最大純度值之比值。飽和度=0,即為灰階。
        3. 明暗 Value : 光的明暗程度
            範圍 0~1
            
    ＠函數：cvtColor()色彩空間轉換
        -> cvtColor(src'原始影像' , mode'色彩空間轉換') 

        openCV色彩模型為BGR,與RGB不同。
        RGB/BGR 轉換到灰階GRAY
        GRAY = 0.299*R + 0.587*G + 0.114*B

1.
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rst = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print('img = \n',img)
print('rst = \n',rst)
print('像素點（1,0）直接算得到的值＝',img[1,0,0]*0.114+img[1,0,1]*0.587+img[1,0,2]*0.299)
print('像素點（1,0）使用公式 cv.cvtColor() 轉換值=' , rst[1,0])




'''
# =============================================================================
#                              DATE : 20200720
# =============================================================================
'''


＊灰階 轉換 BGR
    ＠當影像由GRAY色彩空間轉換到BGR色彩空間時，最後所有通道值是相同的。


1.
import cv2  as cv
import numpy as np
img = np.random.randint(0,256,size=[2,4],dtype=np.uint8)
rst = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
print('img=\n',img)
print('rst=\n',rst)

＊BGR 轉換 RGB
    ＠RGB 與 BGR 互相轉換，R 通道值與 B 通道互換。
    
1.
import cv2  as cv
import numpy as np
img = np.random.randint(0,256,size=[2,4,3],dtype=np.uint8)
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
bgr = cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
print('img=\n',img)
print('rgb=\n',rgb)
print('bgr=\n',bgr)

2.
import cv2  as cv
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('img', img)
cv.imshow('rgb', rgb)
cv.waitKey()




    ＠BGR 轉換為 GRAY 時，即為灰階影像。再將該影像轉換為 BGR 時，BGR 值均相同，顯示結果還是灰階。

2.
import cv2  as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)

print('img.shape=\n',img.shape) # shape 影像的結構
print('gray.shape=\n',gray.shape)
print('bgr.shape=\n',bgr.shape)

cv.imshow('img', img)
cv.imshow('gray', gray)
cv.imshow('bgr', bgr)
print('bgr = \n',bgr)
cv.waitKey()


    ＠色調 H 值設定範圍為 0~360,8 位元影像每個像素點能表示的灰階等極為 2^8=256 個。
      故 8 位元影像要以 HSV 表示時，必須將 H 值調整為 0~255。
      處理方式 ： 將 H 值 / 2 , 得到 0~180 之間的值。(適應8位元二進位儲存及表示)
      0:紅 30:黃 60:綠 90:青 120:藍 150:品紅
      
      

    ＠飽和度 S 值設定範圍為 0~1
      因灰階影像之R,G,B值皆相等，相當於一種極度不飽和的色彩，故灰階影像其飽和度=0.
      灰階影像顯示時，較亮區域對應之色彩具有較高飽和度。若極低飽和度，所得之色調值不可靠。


    ＠亮度 V 值設定範圍為 0~1
      對應到 0~255

1.
import cv2  as cv
import numpy as np 

imgblue = np.zeros([1,1,3],dtype=np.uint8) # 測試藍色的HSV值
imgblue[0,0,0] = 255 # 像素點的第0個通道(第一個值)設為255 ,變成[255,255,255]
Blue = imgblue
BlueHSV = cv.cvtColor(Blue,cv.COLOR_BGR2HSV)
print('Blue = \n',Blue)
print('BlueHSV = \n',BlueHSV)

imggreen = np.zeros([1,1,3],dtype=np.uint8)
imggreen[0,0,1] = 255
Green = imggreen
GreenHSV = cv.cvtColor(Green,cv.COLOR_BGR2HSV)
print('Green = \n',Green)
print('GreenHSV = \n',GreenHSV)

imgred = np.zeros([1,1,3],dtype=np.uint8)
imgred[0,0,2] = 255
Red = imgred
RedHSV = cv.cvtColor(Red,cv.COLOR_BGR2HSV)
print('Red = \n',Red)
print('RedHSV = \n',RedHSV)


    ＠HSV 色彩主要差異是在 H 通道，可對 H 通道進行篩選，以選出特定色彩。
        ＊inRange()函數：針對像素點之像素值判斷是否在某範圍內。
            -> cv2.inRange(src'影像' , lower'範圍下限' , upper'範圍上限')
        *若 src 值在範圍內，則傳回值中對應位置上之值為 255 , 否則為 0。


1.
import cv2  as cv
import numpy as np 

img = np.random.randint(0,256,size=[5,5],dtype=np.uint8)
min = 100
max = 200
mask = cv.inRange(img,min,max)
print('img=\n',img)
print('mask=\n',mask)

2.
import cv2  as cv
import numpy as np 

img = np.ones([5,5],dtype=np.uint8)*9
mask = np.zeros([5,5],dtype=np.uint8)
mask[0:3,0] = 1
mask[2:5,2:4] = 1
roi = cv.bitwise_and(img,img,mask=mask)
print('img=\n',img)
print('mask=\n',mask)
print('roi=\n',roi)



    ＠HSV 色彩空間分析色彩時，並非分析一特定值，而是分析一色彩區間。
      如藍色 H 值為 120，分析藍色時會以其附近值作為區間，通常附近值為半徑10。
      即 120+10 , 120-10 作為分析區間。
      S 通道及 V 通道分析區間在 100~255。
      因 S 飽和度 與 V 亮度 太低時，得到 H 值不可靠。

    HSV 色彩區間：
        [H-10,100,100] ~ [H+10,255,255]
    紅色 色彩區間：
        [0,100,100] ~ [10,255,255]
    綠色 色彩區間：
        [50,100,100] ~ [70,255,255]
    藍色 色彩區間：
        [110,100,100] ~ [130,255,255]
    

1.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/opencv-logo.png')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('img',img)

minBlue = np.array([110,50,50])
maxBlue = np.array([130,255,255])
mask = cv.inRange(hsv,minBlue,maxBlue)
blue = cv.bitwise_and(img,img,mask=mask)
cv.imshow('blue',blue)

minGreen = np.array([50,50,50])
maxGreen = np.array([70,255,255])
mask = cv.inRange(hsv,minGreen,maxGreen)
green = cv.bitwise_and(img,img,mask=mask)
cv.imshow('green',green)

minRed = np.array([0,50,50])
maxRed = np.array([10,255,255])
mask = cv.inRange(hsv,minRed,maxRed)
red = cv.bitwise_and(img,img,mask=mask)
cv.imshow('red',red)

cv.waitKey()



    ＠HSV 膚色分析
        一般可設定為
            色調值：5 ~ 170
            飽和度：25 ~ 166

    ＠處理並設定 HSV 值
      並將其設定為遮罩(mask),再將影像及遮罩做位元and運算，達到以遮罩控制影像顯示的目的。


1.
import cv2 as cv
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv)
minHue = 5
maxHue = 160
hueMask = cv.inRange(h,minHue,maxHue)
minSat = 25
maxSat = 160
satMask = cv.inRange(s,minSat,maxSat)
mask = hueMask & satMask
roi = cv.bitwise_and(img,img,mask=mask)
cv.imshow('img', img)
cv.imshow('ROI',roi)
cv.waitKey()



    ＠於 RGB / BGR 三通道後，再加一通道名為 alpha 透明度通道。
      4通道影像為 RGBA / BGRA , 設定值範圍：0~1 or 0~255(透明~不透明)

1.
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[2,2,3],dtype=np.uint8)
bgra = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
print('img=\n',img)
print('bgra=\n',bgra)
b,g,r,a = cv.split(bgra)
print('a=\n',a)
bgra = cv.merge([b,g,r,a])
print('bgra=\n',bgra)

2.
import cv2 as cv
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
bgra = cv.cvtColor(img,cv.COLOR_BGR2BGRA)
b,g,r,a = cv.split(bgra)
a[:,:]=25
bgra125 = cv.merge([b,g,r,a])
a[:,:]=0
bgra0 = cv.merge([b,g,r,a])
cv.imshow('img',img)
cv.imshow('ngra',bgra)
cv.imshow('bgra125',bgra125)
cv.imshow('bgra0',bgra0)
cv.waitKey()
cv.destroyAllWindows()
cv.imwrite(r'/Users/martychen/Documents/Python/Python practice/bgra.png',bgra )
cv.imwrite(r'/Users/martychen/Documents/Python/Python practice/bgra125.png',bgra125 )
cv.imwrite(r'/Users/martychen/Documents/Python/Python practice/bgra0.png', bgra0)




3.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/lena_01.jpg')
cv.imshow('img',img)
hsv_low = np.array([0,0,0])
hsv_high = np.array([0,0,0])
def h_low(value):
    hsv_low[0] = value
def h_high(value):
    hsv_low[0] = value
def s_low(value):
    hsv_low[0] = value
def s_high(value):
    hsv_low[0] = value
def v_low(value):
    hsv_low[0] = value
def v_high(value):
    hsv_low[0] = value
cv.namedWindow('image')
cv.createTrackbar('H_low','image',0,255,h_low)
cv.createTrackbar('H_high','image',0,255,h_high)
cv.createTrackbar('S_low','image',0,255,s_low)
cv.createTrackbar('S_high','image',0,255,s_high)
cv.createTrackbar('V_low','image',0,255,v_low)
cv.createTrackbar('V_high','image',0,255,v_high)

while(1):
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hsv = cv.inRange(hsv,hsv_low,hsv_high)
    cv.imshow('hsv',hsv)
    if cv.waitKey(1) & 0xFF == 27:
        break
cv.destroyAllWindows()





＊幾何轉換
    ＠影像縮放：resize()函數
        -> cv2.resize(src , dsize , fx , fy , interpolation)
        src 原始影像
        dsize 輸出影像大小
        fx 水平縮放比例
        fy 垂直縮放比例
        interpolation 內插方式
    影像執行幾何處理時，若無法直接透過對映值獲得像素點新值時，則採用內插處理。(通常在放大影像使用)
    內插處理：
        ->INTER_AREA 區域內插(鄰近，最接近區域)
        ->INTER_NEAREST 最鄰近內插(鄰近，最接近區域)
        ->INTER_CUBIC 三次樣條內插(像點附近4x4區域)
        ->INTER_LINEAR 線性內插(預設)


1.
import cv2 as cv
import numpy as np
img = np.ones([2,4,3],dtype=np.uint8)
size = img.shape[:2]
rst = cv.resize(img,size)
print('img.shape=\n',img.shape)
print('img=\n',img)
print('rst.shape=\n',rst.shape)
print('rst=\n',rst)

原始影像大小：2行4列
resize後的大小：4行2列
＊結果的行數為原始的列數

shape屬性：
第一個值是'行'，第二個值是'列'
dsize屬性：
第一個值是'列'，第二個值是'行'


2.
import cv2 as cv
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows,cols = img.shape[:2]
size = (int(cols*0.9),int(rows*0.5))
rst = cv.resize(img , size)
print('img.shape=\n',img.shape)
print('rst.shape=\n',rst.shape)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()



3.
import cv2 as cv
img1 = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
img2 = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
img3 = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
res1 = cv.resize(img1,None,fx=1.5,fy=1.5,interpolation=cv.INTER_AREA)
res2 = cv.resize(img2,None,fx=1.5,fy=1.5,interpolation=cv.INTER_LINEAR)
res3 = cv.resize(img3,None,fx=1.5,fy=1.5,interpolation=cv.INTER_CUBIC)
cv.imshow('img1', img1)
cv.imshow('res1', res1)
cv.imshow('res2', res2)
cv.imshow('res3', res3)
cv.imwrite(r'/Users/martychen/Documents/Python/Python practice/Lena512_A.jpg', res1)
cv.imwrite(r'/Users/martychen/Documents/Python/Python practice/Lena512_L.jpg', res2)
cv.imwrite(r'/Users/martychen/Documents/Python/Python practice/Lena512_C.jpg', res3)

while True:
    if (cv.waitKey() & 0xFF) == ord('q'):
        break
    else:
        pass
cv.destroyAllWindows()


    ＠影像翻轉：flip()
        -> cv2.flip(src , flipcode)
        flipcode :0 繞 x 軸翻轉
                  正數 繞 y 軸翻轉
                  負數 繞 X,Y 軸翻轉


1.
import cv2 as cv
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
x = cv.flip(img,0)
y = cv.flip(img,1)
xy = cv.flip(img,-1)
cv.imshow('img',img)
cv.imshow('x',x)
cv.imshow('y',y)
cv.imshow('xy',xy)
cv.waitKey()


































  
    