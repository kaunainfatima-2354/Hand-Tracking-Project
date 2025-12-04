# Hand-Tracking-Project
This project is a simple real-time computer vision script built with OpenCV that detects hand movement within a Region of Interest (ROI) and classifies the position of the detected fingertip as SAFE, WARNING, or DANGER based on its distance from a predefined point.

📌 Features

1. Captures webcam video in real time
2. Detects skin-colored regions using HSV thresholding
3. Extracts the largest contour (assumed to be the hand)
4. Finds fingertip by choosing the topmost point on the convex hull
5. Calculates distance of fingertip from a fixed object location
6. Classifies the current hand position into:
🟢 SAFE
🟡 WARNING
🔴 DANGER
7. Displays contour, fingertip area, and status overlay

🚀 How It Works

1. Capture Webcam Feed using cv2.VideoCapture(0).
2. Flip the Frame horizontally to match mirror view.
3. Crop ROI (the lower part of the frame) for faster processing.
4. Convert ROI to HSV Color Space.
5. Apply skin color mask using HSV thresholds.
6. Extract contours from the mask.
7. Pick the largest contour (hand region).
8. Compute the convex hull around the hand.
9. Select the topmost point of the hull as the fingertip.
10. Measure distance between fingertip and a fixed point.
11. Display relevant warnings based on that distance.
