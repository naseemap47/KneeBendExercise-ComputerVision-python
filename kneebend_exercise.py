import cv2
import mediapipe as mp
import time
from find_angle import get_angle

cap = cv2.VideoCapture('KneeBendVideo.mp4')
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

pre_angle = 190
direction = 0
count = 0
p_time = 0
c_time = 0

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

            # Angle
            angle = get_angle(lm_list, 23, 25, 27, img)
            if angle is not None:
                angle = angle
                pre_angle = angle
            else:
                angle = pre_angle
            # print(angle)

            # Count
            if angle < 150:
                if direction == 0:
                    count += 0.5
                    direction = 1
            if angle > 150:
                if direction == 1:
                    count += 0.5
                    direction = 0
            # print(count)

            # Display Counts
            cv2.rectangle(
                img, (645, 10), (820, 50),
                (0, 0, 0), cv2.FILLED
            )
            cv2.putText(
                img, f'Counts: {str(int(count))}',
                (650, 40), cv2.FONT_HERSHEY_PLAIN,
                2, (255, 255, 255), 3
            )

            # Time
            if direction == 1:
                c_time = time.time()
            if direction == 0:
                p_time = time.time()
            hold_time = c_time - p_time
            # print(hold_time)

            # Warnings
            if hold_time > 0:
                if hold_time < 8:
                    cv2.rectangle(
                        img, (230, 40), (630, 80),
                        (255, 255, 255), cv2.FILLED
                    )
                    cv2.putText(
                        img, 'Keep your knee bent', (250, 70),
                        cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 0, 255), 2
                    )

        # Draw Landmarks
        # mp_draw.draw_landmarks(img, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
