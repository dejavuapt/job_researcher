import click
from app.database.backend import SQLiteDb
import os

@click.group()
@click.pass_context
def den(ctx: click.Context) -> None:
    click.echo("den")

@den.command()
def add() -> None:
    pass
    
@den.command()
def ls() -> None:
    pass
 
@den.command()
def delete() -> None:
    pass

@den.command()
def update() -> None:
    pass
 
# temporary
@den.command()
@click.option('-p', '--path', default=os.path.dirname(os.path.realpath(__file__)), help='path of init db')
def db(path: str) -> None:
    SQLiteDb(path)