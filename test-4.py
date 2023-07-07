from rich.console import Console
from rich.table import Table

console = Console()
import os
table = Table(show_header=True, header_style="red")
table.add_column("column")
table.add_column("line")
table.add_row(
   str( os.get_terminal_size().columns),str(os.get_terminal_size().lines)
)
console.print(table)