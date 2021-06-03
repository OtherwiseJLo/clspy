import logging
import sys

import typer

from .server import CLSPY_Server

app = typer.Typer()

logging.basicConfig(filename="clspy.log", level=logging.DEBUG, filemode="w")


@app.command()
def main(
    tcp: bool = typer.Option(False, help="Use tcp instead of stdio"),
    stdio: bool = typer.Option(False, help="Use stdio for server"),
    host: str = typer.Option("127.0.0.1"),
    port: int = typer.Option(9008),
):
    if not (tcp or stdio):
        typer.echo(
            "No option selected; please launch with one of the following options:"
        )
        typer.echo("\nUsing stdio:")
        typer.echo("\tclspy --stdio")
        typer.echo("\nUsing tcp:")
        typer.echo("\tclspy --tcp [--host=(127.0.0.1)] [--port=(9008)]")
    if tcp and stdio:
        typer.echo("Please select only one option")
        sys.exit()
    if stdio and not tcp:
        typer.echo("Launching with stdio...")
    if tcp and not stdio:
        typer.echo("Launching with tcp...")
