import cv2

acp= cv2.VideoCapture(0);
print(acp.isOpened())
while(acp.isOpened()):
    ret,frame =cap.read()

    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
     if cv2.waitkey(1) & 0xFF ==ord('Q'):
         break

acp.release()
cv2.destroyAllWindows()
