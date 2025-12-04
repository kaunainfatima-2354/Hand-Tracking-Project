import cv2
import numpy as np


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break
    
    obj_x, obj_y = 150, 60
    boundary_radius = 70

    frame = cv2.resize(frame, (640, 280))
    roi = frame[140:280, :]

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)

        contour_frame = roi.copy()
        cv2.drawContours(contour_frame, [c], -1, (0, 255, 0), 2)
        cv2.circle(contour_frame, (obj_x, obj_y), 25, (255, 0, 0), 2)

        hull = cv2.convexHull(c, returnPoints=True)

        fingertip = min(hull[:, 0, :], key=lambda p: p[1])
        fx, fy = fingertip
        

        dist = ((fx - obj_x)**2 + (fy - obj_y)**2) ** 0.5

        if dist > boundary_radius + 50:
            state = "SAFE"
            color = (0, 255, 0)
        elif boundary_radius - 20 < dist <= boundary_radius +50:
            state = "WARNING"
            color = (0, 255, 255)
        else:
            state = "DANGER DANGER"
            color = (0, 0, 255)

        cv2.putText(contour_frame, state, (10, 40), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2)

        cv2.imshow("contours", contour_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

