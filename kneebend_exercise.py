import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('KneeBendVideo.mp4')
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)
    # print(result.pose_landmarks)

    if result.pose_landmarks:
        for id, lm in enumerate(result.pose_landmarks.landmark):
            print(id, lm)

    cv2.imshow('Video', img)
    cv2.waitKey(1)