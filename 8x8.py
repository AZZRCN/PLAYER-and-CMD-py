import sys
import cv2
from rich.console import Console
from os import system
from time import sleep
from rich.text import Text
console = Console()
for i in range(0,4092):
    imagess = cv2.imread(f'{i}.jpg',1)
    resized_image = cv2.resize(imagess, (16,9))
    system("cls")
    t = Text()
    for i in resized_image:
        for j in i:
            t.append("██", style=f"rgb({j[2]},{j[1]},{j[0]})")
        t.append("\n")
    console.print(t)
    del t