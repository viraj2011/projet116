import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           1,  
           color=(225,225,255)
           )

cv2.putText(img,  
           "MERCURY",
           (50, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(225,225,255)
           )

cv2.putText(img,  
           "VENUS",
           (70, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(75,105,205)
           )

cv2.putText(img,  
           "EARTH",
           (90, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(15,115,10)
           )

cv2.putText(img,  
           "MARS",
           (110, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(265,26,125)
           )

cv2.putText(img,  
           "JUPITER",
           (130, 600),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(235,22,55)
           )

cv2.putText(img,  
           "SATURN",
           (150, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(325,25,45)
           )


cv2.putText(img,  
           "URANUS",
           (170, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(205,22,145)
           )


cv2.putText(img,  
           "NEPTUNE",
           (200, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           color=(225,225,5)
           )




cv2.imshow("Solar_systemwithname",img)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.waitKey(0)

