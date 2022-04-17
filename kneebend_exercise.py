import cv2
import mediapipe as mp
import time
from find_angle import get_angle

cap = cv2.VideoCapture('KneeBendVideo.mp4')
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

mp_draw = mp.solutions.drawing_utils

pre_angle = 190
dir = 0
count = 0

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = pose.process(img_rgb)
    # print(result.pose_landmarks)

    if result.pose_landmarks:
        lm_list = []
        for id, lm in enumerate(result.pose_landmarks.landmark):
            # print(id, lm)
            img_height, img_width, channel = img.shape
            x, y = int(lm.x * img_width), int(lm.y * img_height)
            # print(id, x, y)
            lm_list.append([id, x, y])
            # print(lm_list)

            angle = get_angle(lm_list, 23, 25, 27, img)

            if angle is not None:
                angle = angle
                pre_angle = angle
            else:
                angle = pre_angle
            # print(angle)

            # Count
            if angle < 150:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if angle > 150:
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)


        # Draw Landmarks
        # mp_draw.draw_landmarks(img, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break