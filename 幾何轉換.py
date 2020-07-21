'''
# =============================================================================
#                              DATE : 20200720
# =============================================================================
'''


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



'''
# =============================================================================
#                              DATE : 20200721
# =============================================================================
'''


＊仿射轉換
    ＠透過幾何轉換執行平移，旋轉。此轉換可保持影像的平行性(平行線)及平直性(直線)。
    ＠warpAffine():仿射函數
        -> cv2.warpAffine(src , M , dsize , flags , borderMode , borderValue)
            M 轉換矩陣 , dsize 輸出影像尺寸大小 , flags 內插方法，預設INTER_LINEAR
            borderMode 框線模式 BORDER_CONSTANT
            borderValue 框線值 預設 0



1.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
height,width = img.shape[:2]
x = 100
y = 200
M = np.float32([[1,0,x],[0,1,y]])
move = cv.warpAffine(img, M, (width,height))
cv.imshow('img', img)
cv.imshow('move', move)
cv.waitKey()

a.平移:透過 3x3(或2x2) M矩陣執行轉換。
M -> | 1 0 tx | : 將每一個像點移到 x+t , y+t
     | 0 1 ty | 
     
M(11) = 1     M(21) = 0         |  src(x*1 + y*0 + 100, x*0 + y*1 + 200)
M(12) = 0     M(22) = 1         |
M(13) = 100   M(23) = 200       |


    ＠getRotationMatrix2D() 函數：產生以 warpAffine() 進行旋轉轉換時的轉換矩陣。
        -> cv2.getRotationMatrix2D(center , angle , scale)
            center 旋轉中心點 , angle 旋轉角度(逆時針為正) , scale 縮放比例

1.
import cv2 as cv
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
height,width = img.shape[:2]
M = cv.getRotationMatrix2D((width/2 , height/2), 45, 0.7)
rotate = cv.warpAffine(img, M, (width,height))
cv.imshow('img', img)
cv.imshow('rotate', rotate)
cv.waitKey()




    ＠getAffineTransform() 函數：產生以waprAffine() 進行仿射轉換時的轉換矩陣(以三個點進行轉換)
        -> cv2.getAffineTransform(src , dst)
            src 原影像的三個點座標   ｜ -> 二維陣列
            dst 轉換影像的三個點座標 ｜



1.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols , ch = img.shape
p1 = np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2 = np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
M = cv.getAffineTransform(p1,p2)
dst = cv.warpAffine(img, M, (cols,rows))
cv.imshow('img', img)
cv.imshow('result', dst)
cv.waitKey()



＊透視轉換
    ＠將矩形轉換為任意四邊形(無需維持平行性及平直性)
    ＠waprPerspective()函數
        -> warpPerspective(src , M , dsize , flags , borderMode , borderValue)
            M 轉換矩陣 , dsize 輸出影像尺寸大小 , flags 內插方法，預設INTER_LINEAR
            borderMode 框線模式 BORDER_CONSTANT
            borderValue 框線值 預設 0

    ＠getPerspectiveTransform()函數：產生 warpPerspective()執行時的轉換矩陣 M.
        -> cv2.getPerspectiveTransform(src , dst)
            src 原影像的四個點座標
            dst 轉換影像的四個點座標 (任意四邊形，無需平行性，平直性)
            
1.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols = img.shape[:2]
print(rows,cols)
pts1 = np.float32([[150,50],[300,50],[60,450],[210,450]])
pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img,M,(cols,rows))
cv.imshow('img', img)
cv.imshow('dst', dst)
cv.waitKey()


2.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/opencv-logo.png')
rows , cols = img.shape[:2]
print(rows,cols)
pts1 = np.float32([[300,290],[500,290],[300,400],[500,400]])
pts2 = np.float32([[50,50],[rows-170,100],[50,cols+100],[rows-240,cols-200]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (cols,rows))
cv.imshow('img', img)
cv.imshow('dst', dst)
cv.waitKey()




＊重對映：將影像中的像素點放到另一位置。
    ＠remap()函數
        -> cv2.remap(src , x , y , interpolation , borderMaod , bordervalue)
            x 對映的 x 座標 , y 對映的 y 座標
            interpolation 內插方式
            borderMode 框線模式 BORDER_CONSTANT
            borderValue 框線值 預設 0
      
1.
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.ones(img.shape,np.float32)*3
mapy = np.ones(img.shape,np.float32)*0
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img=\n',img)
print('mapx=\n',mapx)
print('mapy=\n',mapy)
print('rst=\n',rst)


rst : 目標陣列中的所有像素點均對映到原影像(img)中之第 0 行第 3 列之像素點。


2.
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.ones(img.shape,np.float32)
mapy = np.ones(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img=\n',img)
print('mapx=\n',mapx)
print('mapy=\n',mapy)
print('rst=\n',rst)

3.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


    ＠繞 x 軸翻轉：
        對映過程中
            x 軸座標不變
            y 軸座標值以 x 軸做為對稱軸進行交換
        對稱關係為
            目前行號 ＋ 對稱行號 ＝ 總行數 -1
        反映於 x , y 上：(mapx , mapy)
            mapx 值保持不變，mapy = 總行數 -1 -目前行號

4.
import cv2 as cv
import numpy as np
img = np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols = img.shape
mapx = np.ones(img.shape,np.float32)
mapy = np.ones(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
print('img=\n',img)
print('mapx=\n',mapx)
print('mapy=\n',mapy)
print('rst=\n',rst)

5. 繞 x 軸翻轉
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()

6. 繞 y 軸翻轉
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey() 
    

7. 繞 x,y 軸翻轉
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),cols-1-j)
        mapy.itemset((i,j),rows-1-i)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey() 



8. x,y 軸互換：
mapx調整為所在行的行號
mapy調整成所在列的列號

import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/Lena512.jpg')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),i)
        mapy.itemset((i,j),j)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()


9. 若行列數量不相同，則無法完成對映的值會設成0.
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/opencv-logo.png')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),i)
        mapy.itemset((i,j),j)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()





10.縮放
import cv2 as cv
import numpy as np
img = cv.imread(r'/Users/martychen/Documents/Python/Python practice/lena_01.jpg')
rows , cols = img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols<i<0.75*cols and 0.25*rows<j<0.75*rows:
            mapx.itemset((i,j),2*(j-cols*0.25)+0.5)
            mapy.itemset((i,j),2*(i-cols*0.25)+0.5)
        else:
            mapx.itemset((i,j),0)
            mapy.itemset((i,j),0)
rst = cv.remap(img,mapx,mapy,cv.INTER_LINEAR)
cv.imshow('img',img)
cv.imshow('rst',rst)
cv.waitKey()
