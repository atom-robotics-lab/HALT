import cv2
import numpy as np
def Trafficupdate(p,l):
    frame=cv2.imread(p)
    cv2.imshow('htui',frame)
    brg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(brg, 90, 255, cv2.THRESH_BINARY)
    inverted_image = cv2.bitwise_not(thresh)
    cropped_image1 = frame[100::, 0::]
    cropped_image3 = inverted_image[100::, 0::]
    contours, hierarchy = cv2.findContours(cropped_image3 , 1, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0 :
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] !=0 :
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            print("CX : "+str(cx)+"  CY : "+str(cy)+" Cords for {0} level traffic ".format(l))
            cv2.circle(cropped_image1, (cx,cy), 5, (0,0,255), -2)
            cv2.circle(cropped_image3, (cx,cy), 5, (0,255,0), -2)
            cv2.putText(cropped_image1, "centroid is {0} , {1}".format(cx,cy), (cx - 120, cy-200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.drawContours(cropped_image1, contours, -1, (0,255,0), 1)
    return cropped_image1
#MAIN
a=Trafficupdate('./images/r1.png',0)
b=Trafficupdate('./images/r2.png',1)
c=Trafficupdate('./images/r3.png',2)
d=Trafficupdate('./images/r4.png',3)
while True:
        cv2.imshow("Traffic level 0",a)
        cv2.imshow("Traffic level 1",b)
        cv2.imshow("Traffic level 2",c)
        cv2.imshow("Traffic level 3",d)
        if cv2.waitKey(10) & 0xff == ord('q'):   # 1 is the time in ms
            break
cap.release()
cv2.destroyAllWindows()