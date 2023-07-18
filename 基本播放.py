import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

video_path = input()
if(not video_path):exit(1)

def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while 1:
        END,frame = video.read()
        if not END:
            print("End of video")
            break
        if cv2.waitKey(28)== ord("q"):
            break
        cv2.imshow("Video", frame)
    video.release()
    cv2.destroyAllWindows()

PlayVideo(video_path)