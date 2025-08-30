import cv2
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# OpenCV webcam capture
cap = cv2.VideoCapture(0)

def get_finger_states(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    finger_states = []

    # Thumb: compare x with IP joint
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[2].x:
        finger_states.append(1)
    else:
        finger_states.append(0)

    # Other fingers: tip is higher (y less) than pip joint
    for i in range(1, 5):
        if hand_landmarks.landmark[tips_ids[i]].y < hand_landmarks.landmark[tips_ids[i] - 2].y:
            finger_states.append(1)
        else:
            finger_states.append(0)
    return finger_states

def detect_gesture(finger_states):
    gestures = {
        (0, 0, 0, 0, 0): "Rock ✊",
        (0, 1, 1, 0, 0): "Scissors ✌️",
        (0, 1, 0, 0, 0): "One Finger ☝️",
        (1, 0, 0, 0, 0): "Thumbs Up 👍",
        (1, 1, 1, 1, 1): "Open Palm ✋",
        (1, 1, 0, 0, 1): "Rock n Roll 🤘",
        (0, 1, 1, 1, 1): "OK 👌",
        (1, 0, 0, 0, 1): "Call Me 🤙",
    }
    return gestures.get(tuple(finger_states), "Unknown Gesture")

    
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_states = get_finger_states(hand_landmarks)
            gesture = detect_gesture(finger_states)

            cv2.putText(frame, gesture, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
