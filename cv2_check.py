import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    
    ret , frame = cap.read()
    
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    cv2.imshow('kinsukh', image)


    if cv2.waitKey(1) & 0xFF == ord('q'):   
        break
    
cap.release()
cv2.destroyAllWindows()