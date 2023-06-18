import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console


main = typer.Typer(help="Beer Log Managment Application", add_completion=False)

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("\N{beer mug} beer added to database.")
    else:
        print("Error to add the beer in the database!")
        print("No beer today! \N{Weary Face}")


@main.command("list")
def list_beers(name: Optional[str] = None,
               style: Optional[str] = None,
               flavor: Optional[int] = None,
               image: Optional[int] = None,
               cost: Optional[int] = None):
    """Lists beers from the database."""
    beers = get_beers_from_database()
    table = Table(title="\N{beer mug} Beerlog \N{beer mug}")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d %H:%M:%S")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
