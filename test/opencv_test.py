import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# set height and width
cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
    ret, frame = cap.read()
    
    # check if return value is correct
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    blackAndWhite = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Show original video and black and white
    cv.imshow('Original', frame)
    cv.imshow('B/W', blackAndWhite)

    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
