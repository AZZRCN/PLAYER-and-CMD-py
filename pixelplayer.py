import os
import cv2
from rich.console import Console
from ffpyplayer.player import MediaPlayer
import time
console = Console()
ret = True
#video_path = "C:\\Users\\86156\\Documents\\GitHub\\PLAYER-and-CMD-py\\AM.ts"#"强风大背头.mp4"
video_path = input("路径:")
video=cv2.VideoCapture(video_path)
player = MediaPlayer(video_path)
T1 = time.time()
fpas = 1 / 30
cnt = 0
while ret:
    #time.sleep(0.026233)
    #console
    for i in range((int(int(time.time() - T1) / fpas)) - cnt):
        cnt += 1
        video.read()
    ret,frame = video.read()
    width, height = os.get_terminal_size().columns, os.get_terminal_size().lines
    resized_image = cv2.resize(frame, (width,height))
    os.system("cls")
    for i in resized_image:
        for j in i:
            console.print("█", style=f"rgb({j[2]},{j[1]},{j[0]})", end="")
        #console.print("")
    #for i in range(1,int(int(time.time()-T1) / 0.007) - cnt):
    #    video.read()
    #    cnt += 1
    #    print(f"pass!{cnt}")
    cnt += 1
    