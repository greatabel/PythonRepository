import cv2

cam = cv2.VideoCapture("video/POI.mp4")
cam.set(cv2.CAP_PROP_POS_FRAMES, 18)

while (cam.isOpened()):

         ret, frame = cam.read()
         cv2.imshow('frame',frame)

         if cv2.waitKey(1) & 0xFF == ord('q'):
                  break

cam.release()
cv2.destroyAllWindows()