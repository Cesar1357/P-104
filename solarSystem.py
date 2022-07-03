import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sol",(50,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(0,0,255))
cv2.putText(img,"Mercurio",(120,190),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Venus",(200,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Tierra",(290,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Marte",(370,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Jupiter",(450,100),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Saturno",(750,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Urano",(960,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))
cv2.putText(img,"Neptuno",(1100,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(0,0,255))


cv2.imshow("Poster",img)
cv2.waitKey(0)