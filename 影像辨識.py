'''
# =============================================================================
#                              DATE : 20200610
# =============================================================================
'''





＊影像辨識
    ＠opencv
        pip install opencv-python
        
    ＠讀取影像
        -> cv2.imread(檔案名稱 , flag)  # flag：檔案類型
            讀取的資料會儲存成一個numpy的陣列(串列)
            陣列的前 2 個維度為圖片的高度與寬度
            第三維是圖片色彩channel
                RGB圖片：channel=3
                灰階：channel=1
            


    ＠檔案類型 -> IMREAD_COLOR(1) # 彩色 3頻
             -> IMREAD_GRAYSCALE(0）# 灰階 2頻
             -> IMREAD_UNCHANGED(-1) #所有影像頻道(包含透明度)
    
    ＠視窗命名
        -> cv2.namedWindow(視窗名稱)
        
    ＠調整視窗大小
        -> cv2.namedWindow(視窗名稱 , cv2.WINDOW_NORMAL)
    
    ＠顯示影像
        -> cv2.imshow(視窗名稱 , 顯示影像)
        
    ＠關閉視窗
        -> cv2.destoryWindow(視窗名稱)
        -> cv2.destoryAllWindows() #關閉所有視窗
        

    ＠按鍵等待
        -> cv2.waitKey(delay) # 視窗等待按鍵去關閉
    
    ＠寫入影像
        -> cv2.imwrite(寫入的檔案名稱 , 要寫入的檔案)
        

        
        

1.

import cv2 as cv
img = cv.imread(r'/Users/martychen/Desktop/Python/lena_01.jpg')
cv.namedWindow('image')
cv.imshow('image',img)
cv.waitKey()


2. 用灰階讀取照片,並另存新檔。

import cv2 as cv
img = cv.imread(r'/Users/martychen/Desktop/Python/tpe101.jpg',0)
cv.namedWindow('imag')
cv.imshow('image',img)
x = cv.waitKey()
if x == 27: # 27 就是鍵盤'esc'按鍵
    cv.destroyAllWindows()
elif x == ord('s'):
    cv.imwrite(r'/Users/martychen/Desktop/Python/tpe101gray.jpg',img)
    cv.destroyAllWindows()







































