import sys
import cv2
from rich.console import Console
from os import system
from time import sleep
from rich.text import Text
console = Console()
纵 = 2#纵向扩展
横 = 2#横向扩展
fps = 30
视频fps = 30
像素 = (16,16)#缩放到多少像素,(宽,高)
for i in range(0,622,int(视频fps/fps)):
    imagess = cv2.imread(f'{i}.jpg')
    resized_image = cv2.resize(imagess,像素)
    t = Text()
    for i in resized_image:
        for temp in range(0,纵):
            for j in i:
                t.append("██" * 横, style=f"rgb({j[2]},{j[1]},{j[0]})")
            t.append("\n")
    system("cls")
    console.print(t)
    del t
    sleep(1/fps)