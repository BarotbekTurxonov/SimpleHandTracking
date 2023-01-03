import cv2
from cvzone. HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8, maxHands=2)

While True:
        success, img = cap.read()
        hands,img =detector.findHands(img)
        
        cv2.imshow("Video", img)


        cv2.imshow("Image", img)        
#draw=False
         cv2.waitKey(1)
