import cv2
import numpy as np

cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

name=raw_input('enter name')
Id=raw_input('enter your id')
sampleNum=0

while(True):
    ret, img=cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sampleNum = sampleNum+1
        cv2.imwrite("dataSet1/"+Id +str(sampleNum) + ".jpg",gray[y:y+h,x:x+w])
        print
        cv2.imshow('frame',img)
        cv2.waitKey(100)

    cv2.imshow('frame',img)
            
    cv2.waitKey(100)
    if(sampleNum > 100):
        break
    
        
    
cam.release()
cv2.destroyAllWindows()
