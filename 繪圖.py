'''
# =============================================================================
#                              DATE : 20200610
# =============================================================================
'''





* 繪圖
    ＠共同參數
        img：要繪製圖形的影像
        coloe：色彩，使用 BGR 模型。以數組型態儲存，如(255,0,0)
        thickness：線條租細，預設1
        linetype：線條類型
    ＠畫線
        -> cv2.line(檔案名稱 , 起點座標 , 終點座標 , color , thinkness , linetype)
        

    ＠畫矩形
        -> cv2.rectangle(檔案名稱 , 頂點1 , 頂點2 , color , thinkness , linetype)
        
        

    ＠畫圓
        -> cv2.circle(檔案名稱 , 圓心 , 半徑 , color , thinkness , linetype)
        
    ＠畫橢圓
        -> cv2.ellipse(檔案名稱 , 圓心 , (軸1 , 軸2) , 旋轉角度 , 圓弧起始角度 , 圓弧結束角度 , \
            color ,  thinkness , linetype)
        
            

    ＠畫多邊形
        -> cv2.polylines(檔案名稱 , 頂點座標 , isClosed , color ,  thinkness , linetype)
            頂點座標必須是一個陣列(串列)
            其資料型態必須為 numpy.int32
            繪圖前必須以 reshape 重新計算調整(頂點)
            x.reshape(頂點數量,1,2)  # x 設為-1, 由其他參數計算得出
        建立頂點座標
            -> numpy.array([[a,b],[c,d],....], numpy.int32)
            
    ＠寫文字
        -> cv2.putText(檔案名稱 , 文字 , 座標 , 字型 , 大小 , color ,  \
            thinkness , linetype , bottomLeftOrigin # 文字映射 True/False )
    
    ＠使用自定字型
        載入 PIL 模組下的：
            1. ImageFont -> ImageFint.Truetype(載入字體路徑 , 字體大小)
            2. image -> Image.fromarray：將 numpy 陣列轉為 PIL 影像
            3. ImageDraw -> ImageDraw.Draw:在 PIL 影像上寫文字
            4. 使用 text 方法以設定的字型及大小寫入文字
            
            


1.  畫線練習

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8) #np.uint8  可刪除
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.imshow('apple',img)
cv.waitKey()


# =============================================================================
# numpy.zeros()
#     建立一個所有元素都是0的數組
# numpy.zeros(512.512.3)
#     建立 512x512 大小的影像圖片。
#     每一格中有3個元素都是0(BGR)的彩色圖片。 #3個0即是黑色。
#     由imshow()讀入
# np.uint8
#     無號(不會是負號)的8位數整數
# =============================================================================




2. 畫三條線

import cv2 as cv
import numpy as np

n = 300

img = np.zeros((n+1,n+1,3),np.uint8)
img = cv.line(img,(0,0),(n,n),(255,0,0),3)
img = cv.line(img,(0,100),(n,100),(0,255,0),1)
img = cv.line(img,(100,0),(100,n),(0,0,255),6)
cv.imshow('apple',img)
cv.waitKey()


3. 畫矩形

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
cv.rectangle(img,(384,0),(510,128),(0,255,0),5)
cv.imshow('apple',img)
cv.waitKey()

4. 畫矩形填滿色彩

import cv2 as cv
import numpy as np
n = 300
img = np.ones((n,n,3),np.uint8)*255 # ones 即帶入3 個1 , *255 即變成3個255 , 即產生白色圖片。
img = cv.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1,1) # -1 代表 thickness的填滿
cv.imshow('banana',img)
cv.waitKey()



5. 畫圓並填滿色彩

import cv2 as cv
import numpy as np
img = np.zeros((512,512, 3),np.uint8)
cv.circle(img,(447,63),63,(0,0,255),-1)
cv.imshow('King',img)
cv.waitKey()



6. 畫同心圓

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),dtype='uint8') # dtype='uint8' 等於 np.uint8
# 取得中心點(img.shape[1] / 2,img.shape[0] / 2)
for r in range(0,175,25):
    cv.circle(img,(img.shape[1] // 2 , img.shape[0] // 2) , r ,(255,255,255))
    # img.shape[1] 是圖片的水平寬度 , img.shape[0] 是圖片的垂直高度 , img.shape[2] 是channel 數

cv.imshow('Man',img)
cv.waitKey()



7. 同心圓另一種寫法

import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype='uint8')*255 

(centerX , centerY) = (round(img.shape[1]/2),round(img.shape[0]/2))
red = (0,0,255)
for r in range(5,round(d/2),12):
    cv.circle(img,(centerX,centerY),r,red,3)
cv.imshow('woman',img)
cv.waitKey()


# =============================================================================
# round函數
#     -> round(數值 , 小數位數＃預設值為整數位，不寫即代表不取小數)
#         將數值取小數位數的四捨五入值
# =============================================================================


8. 畫橢圓



import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img.fill(200)

cv.ellipse(img,(180,200),(100,60),45,0,360,(128,0,255),2)
cv.ellipse(img,(180,200),(50,100),45,0,180,(255,0,128),-1)

cv.imshow('woman',img)
cv.waitKey()
cv.destroyAllWindows()





9.  畫橢圓

import cv2 as cv
import numpy as np

d = 400
img = np.ones((d,d,3),dtype='uint8')*255

center = (round(d/2),round(d/2))
size = (100,200)
for i in range(1,10):
    angle = np.random.randint(0,361)
    
    color = np.random.randint(0,high = 256,size = (3,)).tolist()
    thickness = np.random.randint(1,9)
    cv.ellipse(img , center , size , angle , 0 , 360 , color , thickness)
    
cv.imshow('friend',img)
cv.waitKey()




10. 畫多邊形


import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
pts = np.array([[10,5],[60,90],[130,80],[110,70]],np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.imshow('friend',img)
cv.waitKey()




11. 寫文字

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,350),font,4,(255,255,255),2,cv.LINE_AA)
# cv.LINE_AA 反鋸齒處理


cv.imshow('friend',img)
cv.waitKey()
cv.destroyAllWindows()






12. 寫文字, 列出 opencv 所有字型

import cv2 as cv
import numpy as np
img = np.zeros((512,512,3), np.uint8)
img.fill(64) # .fill : RGB填入數值 , 所以是(64,64,64)
text = 'OpenCV for Python'

cv.putText(img , text , (10,40), cv.FONT_HERSHEY_SIMPLEX,
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img , text , (10,80), cv.FONT_HERSHEY_PLAIN,
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img , text , (10,120), cv.FONT_HERSHEY_DUPLEX,
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img , text , (10,160), cv.FONT_HERSHEY_COMPLEX,
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img , text , (10,200), cv.FONT_HERSHEY_TRIPLEX,
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img , text , (10,240), cv.FONT_HERSHEY_COMPLEX_SMALL,
           1,(0,255,255),1,cv.LINE_AA)
cv.putText(img , text , (10,280), cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
           1,(0,255,255),1,cv.LINE_AA)

cv.putText(img , text , (10,320), cv.FONT_HERSHEY_SCRIPT_COMPLEX,
           1,(0,255,255),1,cv.LINE_AA)

cv.imshow('friend',img)
cv.waitKey()
cv.destroyAllWindows()



13. 文字描邊


import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (0,200), font, 3, (0,255,0),10)
cv.putText(img, 'OpenCV', (0,200), font, 3, (0,0,255),5)

cv.imshow('friend',img)
cv.waitKey()



14. 印射文字


import cv2 as cv
import numpy as np
d = 400
img = np.ones((d,d,3),dtype='uint8')*255
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (20,150), font, 3, (0,255,0),15,cv.LINE_AA)
cv.putText(img, 'OpenCV', (20,220), font, 3, (0,0,255),15,cv.FONT_HERSHEY_SCRIPT_SIMPLEX,True)

cv.imshow('friend',img)
cv.waitKey()


15. 使用自定字型

from PIL import ImageFont, ImageDraw,Image
import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)


img[:] = (0,0,192) # img 設定為(0,0,192)
text = '恭喜\n新囍'

fontPath = r'/Users/martychen/Downloads/TaipeiSansTCBeta-Bold.ttf'
font = ImageFont.truetype(fontPath,224) # fontPath 是字的檔案 , 224 是字的大小
imgPil = Image.fromarray(img)

draw = ImageDraw.Draw(imgPil)
draw.text((30,30),text,font=font,fill=(0,0,0,0))

img=np.array(imgPil)
cv.imshow('bigone',img)
cv.waitKey()
cv.destroyAllWindows()






