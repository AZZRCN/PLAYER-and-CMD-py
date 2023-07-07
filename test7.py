import cv2
from rich.console import Console
con = Console()
imagess = cv2.imread(r'63.jpg',-1)
print(len(imagess))#row
print(len(imagess[0]))#column
保留行 = 7#例如2,行不是2的倍数就跳过
保留列 = 5#约等于同上
#最终显示从上面两个参数计算
#保留行 *= 2#因为比例问题
line = round(len(imagess)/保留行)#算出一共打印多少行
column = round(len(imagess[0])/保留列)#同上
for j in range(0,line):
        #con.print("■",style=f"rgb({i[2]},{i[1]},{i[0]})",end="")
    if(j%保留行 != 0):
        continue
    else:
        for i in range(0,column):
            if(i%保留列 != 0):
                continue
            else:
                t = imagess[j*保留行][i * 保留列]
                con.print("█",style=f"rgb({t[2]},{t[1]},{t[0]})",end="")
    con.print("")