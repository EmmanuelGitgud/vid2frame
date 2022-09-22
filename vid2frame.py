import cv2
import os 

directory = 'Twice'
cap= cv2.VideoCapture('TW.webm')
path = directory
i=0


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(os.path.join(path,'pic'+str(i)+'.jpg'),frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

