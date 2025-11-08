import click
from app.settings import COMMANDS
from app.cli_utils import _JobrGroup

@click.group(cls=_JobrGroup,
             subcommands=COMMANDS)
@click.pass_context
def interactive_cli(ctx: click.Context) -> None:
    pass

    
entry_point = interactive_cli