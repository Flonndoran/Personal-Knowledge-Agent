import typer
from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def version():
    console.print('[blue]Personal Knowledge Agent v0.1.0[/blue]')

if __name__ == "__main__":
    app()
    