import logging

import typer

from .server import CLSPY_Server

logging.basicConfig(filename="clspy.log", level=logging.DEBUG, filemode="w")


def main(
    tcp: bool = typer.Option(False, help="Use tcp instead of stdio"),
    stdio: bool = typer.Option(False, help="Use stdio for server"),
    host: str = typer.Option("127.0.0.1"),
    port: int = typer.Option(9008),
):
    if not (tcp or stdio):
        typer.echo("No option selected; please select option to launch")


if __name__ == "__main__":
    typer.run(main)
