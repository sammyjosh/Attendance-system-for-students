
import os.path

import cv2
cam=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Id=input('Enetr your id')
sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        sampleNum=sampleNum+1
        cv2.imwritten("dataset/User."+Id+'.'+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.imshow('frame',img)
    if cv2.waitKey(100)&0xFF == ord('q'):
     break
    elif sampleNum>100:
         break
cam.release()
cv2.destroyAllWindows()

for imagepath in imagePaths:
          pilImage=Image.open(imagePath) .convert('L')
          imageNp=np.array(pilImage,'unint8')
          Id=int(os.path.split(imagePath)[-1] .split(".") [1])
          faces.append(Id)
          print(Id)
          Ids.append(Id)
          cv2.imshow("training",imageNp)
          cv2.waitKey(100)
          return (faces,Ids)



faces,Ids =getImagesandLabels(path)
regonizer.train(faces, np.array(Ids))
regonizer.save('tainer/trainer .yml')
import cv2 ,os
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
cascadePath="Classifiers/face.xml"
faceCascade=cv2.CascadeClassifier(cascadePath)
path='dataSet'

def getImagesAndLabels(path):
    ImagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]