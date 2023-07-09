import cv2
import threading
import time

# 先播放一秒，如果当前时间对不上，视频就等一下，等音频跟上再继续播放
def video():
    cap = cv2.VideoCapture("视频.mp4")
    rate = cap.get(5)  # 读取视频帧率
    startTime = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            zhen = cap.get(1)   # 获取当前帧数
            frame = cv2.resize(frame, (1080, 640))
            cv2.imshow('frame', frame)
            cv2.waitKey(1)  # 等待1毫秒 （1秒=1000毫秒）
            sleepTime = zhen/rate - time.time() + startTime
            if sleepTime > 0:  # 播放时间快了就等一下
                time.sleep(sleepTime)



vd = threading.Thread(target=video)
vd.start()