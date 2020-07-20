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








  
    
    
    
    
    