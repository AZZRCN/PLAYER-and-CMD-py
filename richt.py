from rich.console import Console
#^C之类:rgb(241,76,70)
#普通字:rgb(204,204,204)
#黄色:rgb(245,245,67)
c = Console()
c.print(open("LICENSE").read(),style="bold green on black",justify="left")