import numpy as np
import pandas as pd
import os
import cv2 
from matplotlib import pyplot as plt
import joblib 
#ml model imported as clf
clf = joblib.load('filename.pkl') 

rows=9
cols=9
arr = [[0 for i in range(cols)] for j in range(rows)]

image =cv2.imread(r"C:\Users\rajat vohra\Documents\python_2020\comp_vision\images\ab.png",1)


#cv2.imshow("a",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

blur=cv2.GaussianBlur(gray,(5,5),0)
#cv2.imshow("g",gray)
thresh=cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
#cv2.imshow("g",thresh)
dilated=cv2.dilate(thresh,(5,5),iterations=1)
#cv2.imshow("g",dilated)
eroded=cv2.erode(dilated,(5,5),iterations=1)
#cv2.imshow("g2",eroded)
contours, hierarchy = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
output=image.copy()


if len(contours) != 0:

    c = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(c)
    # draw the book contour (in green)
    
output=output[y:y+h,x:x+w]
#cv2.imshow("before", output)
gray=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)

blur=cv2.GaussianBlur(gray,(5,5),0)
#cv2.imshow("g",gray)
thresh=cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
#cv2.imshow("g",thresh)
thresh=cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, (3,3))
thresh=cv2.medianBlur(thresh, 3)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


output=cv2.resize(output,(360,360))
output=cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
try: 
    os.remove(r"C:\Users\rajat vohra\Documents\python_2020\comp_vision\images\new.jpg")
except: 
    pass
cv2.imwrite(r"C:\Users\rajat vohra\Documents\python_2020\comp_vision\images\new.jpg",output)
(thresh, out) = cv2.threshold(output, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
output=cv2.bitwise_not(out)
#cv2.imshow("output",output)
#a=np.float32(X.iloc[0])
#a=np.reshape(a,(28,28))

lines=[40*i for i in range(10)]
for line in lines:
    pt1 = (line,0)
    pt2 = (line,360)
    pt3=(0,line)
    pt4=(360,line)
    cv2.line(output, pt1, pt2, (0,0,0), 2)
    cv2.line(output, pt3, pt4, (0,0,0), 2)


for i in range(0,360,40):
    for j in range(0,360,40):
        a=output[i:i+40,j:j+40]
        a=cv2.resize(a,(28,28))
        count=0
        for l in range(28):
            for m in range(28):
                if(a[l,m]==0):
                    count=count+1
        
        if(count<700):
            a=a.reshape(1,-1)
            x=clf.predict(a)
            x=int(x)
            arr[int(i/40)][int(j/40)]=x


        
cv2.waitKey(0)



cv2.waitKey(0)
cv2.destroyAllWindows()