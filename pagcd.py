#16/1
from time import sleep


def pogcd(path:str):
    from math import floor, gcd
    import cv2
    from rich.console import Console
    con = Console()
    imagess = cv2.imread(path,-1)
    column = len(imagess)#|
    row = len(imagess[0])#-
    gcdd = gcd(column, row)
    columnd = floor(column/ gcdd)
    rowd = floor(row / gcdd)
    #print(column)#row
    #print(row)#column
    for i in range(0,columnd):
        for j in range(0,rowd * 2):
            t = imagess[i * gcdd][int(j * gcdd / 2)]
            con.print("█",style=f"rgb({t[2]},{t[1]},{t[0]})",end="")
        con.print()
    sleep(0.1)
if __name__ == "__main__":
    pogcd("113.jpg")