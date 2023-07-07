#16/1
from math import floor
import cv2
from rich.console import Console
con = Console()
imagess = cv2.imread(r'7.jpg',-1)
column = len(imagess)#|
columnd = floor(column/ 16)
row = len(imagess[0])#-
rowd = floor(row / 16)
print(column)#row
print(row)#column
for i in range(0,16):
    for j in range(0,16):
        t = imagess[i * columnd][j * rowd]
        con.print("■",style=f"rgb({t[2]},{t[1]},{t[0]})",end="")
    print()