import cv2

imag=cv2.imread('obrazy/barrack.jpg')
grey_img=cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)

kaskada=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
prostokat = kaskada.detectMultiScale(grey_img, scaleFactor=1.1, minNeighbors=5)

for (x,y,w,h) in prostokat:
    cv2.rectangle(imag,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('face',imag)
cv2.waitKey(0)