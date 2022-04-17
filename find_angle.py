import math


def get_angle(list_lm, p1, p2, p3):
    if len(list_lm) > 30:
        x1, y1 = list_lm[p1][1:]
        x2, y2 = list_lm[p2][1:]
        x3, y3 = list_lm[p3][1:]

        # Angle
        angle = math.degrees(
            math.atan2(y3 - y2, x3 - x2) -
            math.atan2(y1 - y2, x1 - x2)
        )

        return abs(angle)


