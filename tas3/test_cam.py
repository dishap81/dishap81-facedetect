import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opening")
else:
    print("Camera opened successfully")

ret, frame = cap.read()

if ret:
    cv2.imshow("Test", frame)
    cv2.waitKey(0)
else:
    print("Frame not captured")

cap.release()
cv2.destroyAllWindows()