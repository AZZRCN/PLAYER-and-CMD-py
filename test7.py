"""import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('强风大背头.mp4')

# Check if camera opened successfully
#if (cap.isOpened()== False): 
 # print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()"""

# 使用cv2读取显示视频
 
# 引入math
import math
# 引入opencv
import cv2
from ffpyplayer.player import MediaPlayer
# opencv获取本地视频
 
def play_video(video_path, audio_play=True):
    cap = cv2.VideoCapture(video_path)
    if audio_play:
        player = MediaPlayer(video_path)
    # 打开文件状态
    isopen = cap.isOpened()
    if not isopen:
        print("Err: Video is failure. Exiting ...")
 
    # 视频时长总帧数
    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # 获取视频宽度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 获取视频高度
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 播放帧间隔毫秒数
    wait = int(1000 / fps) if fps else 1
    # 帧数计数器
    read_frame = 0
 
    # 循环读取视频帧
    while (isopen):
        # 读取帧图像
        ret, frame = cap.read()
        # 读取错误处理
        if not ret:
 
            if read_frame < total_frame:
                # 读取错误
                print("Err: Can't receive frame. Exiting ...")
            else:
                # 正常结束
                print("Info: Stream is End")
            break
 
        # 帧数计数器+1
        read_frame = read_frame + 1
        cv2.putText(frame, "[{}/{}]".format(str(read_frame), str(int(total_frame))), (read_frame, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 9), 2)
        dst = cv2.resize(frame, (1920//2, 1080//2), interpolation=cv2.INTER_CUBIC)  # 窗口大小
        # 计算当前播放时码
        timecode_h = int(read_frame / fps / 60 / 60)
        timecode_m = int(read_frame / fps / 60)
        timecode_s = read_frame / fps % 60
        s = math.modf(timecode_s)
        timecode_s = int(timecode_s)
        timecode_f = int(s[0] * fps)
        print("{:0>2d}:{:0>2d}:{:0>2d}.{:0>2d}".format(timecode_h, timecode_m, timecode_s, timecode_f))
 
        # 显示帧图像
        cv2.imshow('image', dst)
 
        # 播放间隔
        wk = cv2.waitKey(wait)
 
        # 按键值  & 0xFF是一个二进制AND操作 返回一个不是单字节的代码
        keycode = wk & 0xff
 
        # 空格键暂停
        if keycode == ord(" "):
            cv2.waitKey(0)
 
        # q键退出
        if keycode == ord('q'):
            print("Info: By user Cancal ...")
            break
 
    # 释放实例
    cap.release()
 
    # 销毁窗口
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    play_video('强风大背头.mp4', audio_play=False)