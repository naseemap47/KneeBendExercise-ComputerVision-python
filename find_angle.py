import math
import cv2


def get_angle(list_lm, p1, p2, p3, image, draw=True):
    if len(list_lm) > 30:
        x1, y1 = list_lm[p1][1:]
        x2, y2 = list_lm[p2][1:]
        x3, y3 = list_lm[p3][1:]

        # Angle
        angle = math.degrees(
            math.atan2(y3 - y2, x3 - x2) -
            math.atan2(y1 - y2, x1 - x2)
        )

        # Draw
        if draw:
            # Circle
            cv2.circle(
                image, (x1, y1), 7,
                (0, 255, 0), 2
            )
            cv2.circle(
                image, (x1, y1), 3,
                (0, 255, 0), cv2.FILLED
            )
            cv2.circle(
                image, (x2, y2), 7,
                (0, 255, 0), 2
            )
            cv2.circle(
                image, (x2, y2), 3,
                (0, 255, 0), cv2.FILLED
            )
            cv2.circle(
                image, (x3, y3), 7,
                (0, 255, 0), 2
            )
            cv2.circle(
                image, (x3, y3), 3,
                (0, 255, 0), cv2.FILLED
            )

            # Line
            cv2.line(
                image, (x1, y1), (x2, y2),
                (255, 255, 255), 2
            )
            cv2.line(
                image, (x3, y3), (x2, y2),
                (255, 255, 255), 2
            )

        return abs(angle)


