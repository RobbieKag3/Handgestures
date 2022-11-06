import cv2
import mediapipe as mp
camera=cv2.VideoCapture(0)
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
hands=mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5)
tipid=[8,12,16,20]
def   drawhandlandmarks(image,hand_landmarks):
    if hand_landmarks:
        for lm in hand_landmarks:
            mp_drawing.draw_landmarks(image,lm,mp_hands.HAND_CONNECTIONS)
while True:
    ret,image=camera.read()
    image=cv2.flip(image,1)
    results=hands.process(image)
    hand_landmarks=results.multi_hand_landmarks
    drawhandlandmarks(image,hand_landmarks)
    cv2.imshow("image", image)
    if cv2.waitKey(1)==32:
        break