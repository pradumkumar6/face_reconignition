import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret is False:
        continue
    
    cv2.imshow("Actual Video Frame", frame)
    cv2.imshow("Gray video Frame", gray_frame)
        
    # Wait for user input -q
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
