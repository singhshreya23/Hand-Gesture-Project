import cv2
import mediapipe as mp
import serial
import time

# Arduino connection
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)  # Arduino ko settle hone do
    print("Arduino connected!")
except:
    print("Arduino nahi mila, bina Arduino chalega")
    arduino = None

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
) as hands:
    while True:
        success, img = cap.read()
        if not success:
            break

        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    img, handLms,
                    mp_hands.HAND_CONNECTIONS
                )
            cv2.putText(img, "Hand Detected!",
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

            # Arduino ko signal bhejo
            if arduino:
                arduino.write(b'1')
        else:
            cv2.putText(img, "No Hand",
                (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)

            if arduino:
                arduino.write(b'0')

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) == 27:
            break

cap.release()
if arduino:
    arduino.close()
cv2.destroyAllWindows()