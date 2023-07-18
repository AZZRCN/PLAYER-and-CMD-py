from time import sleep
from rich.console import Console
from 基本宽高比 import pogcd
c = Console()
import os
list = os.listdir()
for i in list:
    if(i[-4:] == ".jpg"):
        c.clear()
        pogcd(i)