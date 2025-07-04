import cv2
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# MediaPipe Hand Detection Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Pycaw: System Volume Setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Distance Calculation Function
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Start Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)  # Mirror image
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            thumb_x, thumb_y = int(thumb.x * frame.shape[1]), int(thumb.y * frame.shape[0])
            index_x, index_y = int(index_finger.x * frame.shape[1]), int(index_finger.y * frame.shape[0])

            distance = calculate_distance(thumb_x, thumb_y, index_x, index_y)
            volume_level = max(0.0, min(distance / 300.0, 1.0))  # Normalize

            volume.SetMasterVolumeLevelScalar(volume_level, None)

            # Draw line for visual feedback
            cv2.line(frame, (thumb_x, thumb_y), (index_x, index_y), (0, 255, 0), 3)

    cv2.imshow('🎛️ Gesture Volume Control', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
