import os
import cv2
from rich.console import Console
console = Console()
for t in range(0,1001,20):
    width, height = os.get_terminal_size().columns, os.get_terminal_size().lines
    imagess = cv2.imread(f'{t}.jpg',-1)
    resized_image = cv2.resize(imagess, (width,height))
    os.system("cls")
    for i in resized_image:
        for j in i:
            console.print("█", style=f"rgb({j[2]},{j[1]},{j[0]})", end="")
        console.print("")