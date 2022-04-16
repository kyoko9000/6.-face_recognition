import cv2
import face_recognition

# tai anh len
image1 = cv2.imread('nhu quynh.jpg')
# chuyen anh thanh mau xam
image_1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# tim vi tri khuon mat
face_l = face_recognition.face_locations(image_1)
# ve hinh vuong len khuon mat (top, right, bottom, left)
# cv2.rectangle(image1,(face_l[1][1],face_l[1][0]),(face_l[1][3],face_l[1][2]),(0,255,0),3)
# cv2.rectangle(image1,(face_l[1],face_l[0]),(face_l[3],face_l[2]),(0,255,0),3)
for a in face_l:
    cv2.rectangle(image1,(a[1],a[0]),(a[3],a[2]),(0,255,0),3)

# show buc anh len
print(face_l)
cv2.imshow('hello',image1)
# duy tri khung hinh
cv2.waitKey(0)