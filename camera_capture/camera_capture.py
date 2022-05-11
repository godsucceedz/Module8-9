import cv2 
import numpy as np 
import time

cam = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # set new dimensionns to cam object (not cap)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

i = 1
name = ''

while 1:
    print("part name")
    name = input()
    break

print("\ncamera activate...")
print("""Program start 
        #press 'd' to capture
        #press 'q' to exit""")

while 1:

    check, frame = cam.read()
    cv2.imshow('frame1', frame)
    
    c = cv2.waitKey(1)
    if c == 32: #press 'd' to capture 100
        cv2.imwrite(name + "No." + str(i) + '.jpg', frame)
        print("save" + name + str(i))
        i+=1
        
    
    elif c == 114:
        i = 1
        print("reset number")
        
    elif c == 113: #press 'q' to exit
        break
    
        
cam.release()
cv2.destroyAllWindows()
