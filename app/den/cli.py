import click

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
 