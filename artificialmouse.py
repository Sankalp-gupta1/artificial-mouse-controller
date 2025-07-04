import cv2
import numpy as np
import pyautogui

def detect_finger(frame): #it is needed for detect finger max limit is  (n-1)
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve accuracy
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use adaptive thresholding to handle varying lighting conditions
    _, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply morphological operations for further noise reduction
    kernel = np.ones((5, 5), np.uint8)
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (assumed to be the finger) with a minimum size
    min_contour_size = 100  # Adjust as needed
    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_size]

    if large_contours:
        max_contour = max(large_contours, key=cv2.contourArea)
        return max_contour
    else:
        return None

def artificial_mouse_with_finger():
    cap = cv2.VideoCapture(0)  # Open the default camera (change the argument for a different camera)

    # Set a higher camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        finger_contour = detect_finger(frame)

        if finger_contour is not None:
            # Get the centroid of the finger contour
            M = cv2.moments(finger_contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Simulate mouse movement based on finger position
            screen_width, screen_height = pyautogui.size()
            target_x = int(cx * (screen_width / frame.shape[1]))
            target_y = int(cy * (screen_height / frame.shape[0]))

            pyautogui.moveTo(target_x, target_y)

        # Display the frame
        cv2.imshow("Artificial Mouse", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Starting artificial mouse with finger tracking. Press 'q' to exit.")
    artificial_mouse_with_finger()
    print("Artificial mouse with finger tracking completed.")
