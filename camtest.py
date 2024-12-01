import cv2

# Check to see if camera is accessible

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not accessible.")
else:
    print("Camera works!")
cap.release()