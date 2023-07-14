from random import randint
from rich.text import Text
from rich.console import Console
import os
c = Console()
t = Text()
stli = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm-=+_[]{}|\\\"':;<>,./?`~"
#print(len(stli))
for i in range(1,os.get_terminal_size().columns * os.get_terminal_size().lines):
    r,g,b = randint(0,255),randint(0,255),randint(0,255)
    #t.append(stli[randint(0,83)],f"rgb({r},{g},{b})")
    c.print(stli[randint(0,83)],style=f"bold rgb({r},{g},{b}) on rgb(99,99,99)",end="")
#c.clear()
#c.print(t)