import cv2

cam = cv2.VideoCapture(0)
ret, frame = cam.read()

h, w = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video_write = cv2.VideoWriter('video/saved_out.avi', fourcc, 25.0, (w, h) )

while (cam.isOpened()):

         ret, frame = cam.read()
         video_write.write(frame)
         cv2.imshow('video',frame)

         if cv2.waitKey(1) & 0xFF == ord('q'):
                  break

cam.release()
video_write.release()
cv2.destroyAllWindows()

