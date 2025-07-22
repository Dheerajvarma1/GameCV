import cv2
import mediapipe as mp
import pyautogui
import math

# Setup pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Distance helper
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Flags to avoid repeat press
punched = False
kicked = False
ducked = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    if result.pose_landmarks:
        lm = result.pose_landmarks.landmark
        h, w, _ = frame.shape

        def to_px(point):
            return int(point.x * w), int(point.y * h)

        # Landmarks
        r_sh = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]
        l_sh = lm[mp_pose.PoseLandmark.LEFT_SHOULDER]
        r_wr = lm[mp_pose.PoseLandmark.RIGHT_WRIST]
        l_wr = lm[mp_pose.PoseLandmark.LEFT_WRIST]
        r_hip = lm[mp_pose.PoseLandmark.RIGHT_HIP]
        l_hip = lm[mp_pose.PoseLandmark.LEFT_HIP]
        r_knee = lm[mp_pose.PoseLandmark.RIGHT_KNEE]
        l_knee = lm[mp_pose.PoseLandmark.LEFT_KNEE]
        r_ankle = lm[mp_pose.PoseLandmark.RIGHT_ANKLE]
        l_ankle = lm[mp_pose.PoseLandmark.LEFT_ANKLE]

        # Convert to pixel coordinates
        r_sh_px, l_sh_px = to_px(r_sh), to_px(l_sh)
        r_wr_px, l_wr_px = to_px(r_wr), to_px(l_wr)
        r_hip_px, l_hip_px = to_px(r_hip), to_px(l_hip)
        r_knee_px, l_knee_px = to_px(r_knee), to_px(l_knee)
        r_ankle_px, l_ankle_px = to_px(r_ankle), to_px(l_ankle)

        # Draw landmarks
        mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # === Punch (X) ===
        d_r = distance(*r_sh_px, *r_wr_px)
        d_l = distance(*l_sh_px, *l_wr_px)

        if (d_r > 150 or d_l > 150) and not punched:
            print("👊 Punch!")
            pyautogui.press("x")
            punched = True
        elif d_r < 120 and d_l < 120:
            punched = False

        # === Kick (Z) ===
        if (r_ankle_px[1] < r_hip_px[1] or l_ankle_px[1] < l_hip_px[1]) and not kicked:
            print("🦵 Kick!")
            pyautogui.press("z")
            kicked = True
        elif r_ankle_px[1] > r_hip_px[1] + 40 and l_ankle_px[1] > l_hip_px[1] + 40:
            kicked = False

        # === Duck (Shift) ===
                # === Duck (wrists near knees) ===
        d_rk = distance(*r_wr_px, *r_knee_px)
        d_lk = distance(*l_wr_px, *l_knee_px)

        if d_rk < 60 and d_lk < 60 and not ducked:
            print("🧎 Duck detected (hands near knees)!")
            pyautogui.press("shift")
            ducked = True
        elif d_rk > 80 and d_lk > 80:
            ducked = False


    cv2.imshow("Game Control Tracker", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
