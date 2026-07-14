import cv2
import numpy as np
import face_recognition as fr
import os
from datetime import datetime

path = "students"
student_images = []
student_names = []
myList = os.listdir(path)
# print(myList)
for child in myList:
    currImage = cv2.imread(f'{path}/{child}')
    student_images.append(currImage)
    student_names.append(os.path.splitext(child)[0])    

# print(student_names)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myData = f.readlines()
        nameList = []
        for line in myData:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            datestr = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{datestr}')

encodeListKnown = findEncodings(student_images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print("Couldn't find camera")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Can't read images")
        break
        
    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25)

    faceInCurrentFrame = fr.face_locations(imgSmall)
    encodeInCurrentFrame = fr.face_encodings(imgSmall,faceInCurrentFrame)

    for encodeFace, faceLoc in zip(encodeInCurrentFrame, faceInCurrentFrame):
        matches = fr.compare_faces(encodeListKnown, encodeFace)
        faceDis = fr.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = student_names[matchIndex].upper()
            # print(name)
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)

    cv2.imshow("frame", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        break


cap.release()
cv2.destroyAllWindows()