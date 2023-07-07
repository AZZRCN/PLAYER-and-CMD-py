from rich.progress import track
from time import sleep
from random import randint
for step in track(range(100), description="DOWNLOADING...",):
    sleep(randint(1,10)/100)