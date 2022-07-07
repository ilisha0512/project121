import numpy as np
import cv2
video = cv2.VideoCapture(0)
image = cv2.imread("me.jpg")

while True:
    ret, frame = video.read()
    image = cv2.resize(image, (640, 480))
    frame = cv2.resize(frame, (640, 480))
    l_black = np.array([30, 30, 0])
    u_black = np.array([104, 153, 70])
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    f = frame - res
    f = np.where(f == 0, image, f)
    cv2.imshow("original video", frame)
    cv2.imshow("masked video", f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()