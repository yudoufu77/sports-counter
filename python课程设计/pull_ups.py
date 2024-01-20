import cv2
import mediapipe as mp
import numpy as np
import math
import time
import os

@app.route('/api/pull-ups', methods=['GET'])
class PoseDetector:
    def __init__(self, mode=False, complexity=1, smooth_landmarks=True,
                 enable_segmentation=False, smooth_segmentation=True,
                 detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.complexity = complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.mode, self.complexity, self.smooth_landmarks,
                                      self.enable_segmentation, self.smooth_segmentation,
                                      self.detection_con, self.track_con)
        self.lm_list = []

    def find_pose(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)

        if self.results.pose_landmarks:
            if draw:
                self.mp_draw.draw_landmarks(img, self.results.pose_landmarks,
                                            self.mp_pose.POSE_CONNECTIONS)

        return img

    def find_position(self, img, draw=True):
        self.lm_list = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lm_list

    def find_angle(self, img, p1, p2, p3, draw=True):
        x1, y1 = self.lm_list[p1][1:]
        x2, y2 = self.lm_list[p2][1:]
        x3, y3 = self.lm_list[p3][1:]

        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        angle = angle + 360 if angle < 0 else angle
        angle = 360 - angle if angle > 180 else angle

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)

            for point in [p1, p2, p3]:
                x, y = self.lm_list[point][1:]
                cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
                cv2.circle(img, (x, y), 15, (0, 0, 255), 2)

            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle


def main():
    detector = PoseDetector()

    while True:
        video_path = input("请输入视频地址: ")

        if not os.path.exists(video_path):
            print("视频不存在，请重新输入。")
            continue
        else:
            break

    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_dir, 'out')
    output_file = '引体向上.avi'
    path = os.path.join(output_path, output_file)

    if os.path.exists(output_path):
        count = 1
        while True:
            new_output_file = f'引体向上 ({count}).avi'
            new_output_path = os.path.join(output_path, new_output_file)
            if not os.path.exists(new_output_path):
                path = new_output_path
                break
            count += 1

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    count = 0
    direction = 0
    form = 0
    feedback = "Fix Form"
    start_time = time.time()
    prev_count = 0
    prev_time = start_time
    avg_speed = 0  # 保留平均速度

    # 获取视频的原始尺寸
    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 设置显示窗口的大小，保持原始视频的长宽比
    window_width = 500
    window_height = int((original_height / original_width) * window_width)

    # 打开显示窗口
    cv2.namedWindow('Pullup counter(press key ''q'' to exit)', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Pullup counter(press key ''q'' to exit)', window_width, window_height)

    #输出视频设置
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path, fourcc, fps, (original_width, original_height))

    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            break

        img = detector.find_pose(img, False)
        detector.find_position(img, False)


        if len(detector.lm_list) != 0:
            lelbow = detector.find_angle(img, 11, 13, 15)
            lshoulder = detector.find_angle(img, 13, 11, 23)
            relbow = detector.find_angle(img, 12, 14, 16)
            rshoulder = detector.find_angle(img, 14, 12, 24)


            per = np.interp(lelbow, (50, 150), (0, 100))
            bar = np.interp(lelbow, (50, 150), (380, 50))

            if (lelbow > 150 and lshoulder > 150) or (relbow > 150 and rshoulder > 150):
                form = 1

            if form == 1:
                if per == 0:
                    if (lelbow < 70 and lshoulder < 70) or (relbow < 70 and rshoulder < 70):
                        feedback = "Up"
                        if direction == 0:
                            count += 0.5
                            direction = 1
                    else:
                        feedback = "Fix Form"

                if per == 100:
                    if (lelbow > 150 and lshoulder > 150) or (relbow > 150 and rshoulder > 150):
                        feedback = "Down"
                        if direction == 1:
                            count += 0.5
                            direction = 0
                    else:
                        feedback = "Fix Form"

            cv2.putText(img, f"Count: {int(count)}", (20, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

            current_time = time.time()
            elapsed_time = current_time - start_time
            avg_speed = avg_speed if count == prev_count else (count/ elapsed_time)*60

            cv2.putText(img, f"Time: {int(elapsed_time)}s", (20, 80), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)
            cv2.putText(img, f"Avg Speed: {avg_speed:.2f} pullups/min", (20, 120), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

            prev_count = count
            prev_time = current_time

            if form == 1:
                cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
                cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 255, 0), 2)
        out.write(img)

        cv2.imshow('Pullup counter(press key ''q'' to exit)', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    print("视频已保存到out目录,请查看")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()