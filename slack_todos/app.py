"""
Slack Todos main app driver file.
Author: jsduncan98@gmail.com <shadowcodex>

This application is built to manage todos stored locally, in git, or slack todo.

:: poetry run td --help
"""
import click

@click.group()
def cli():
    """A CLI tool for todos..."""
    pass

@click.command()
def ls():
    """List todos"""
    pass

@click.command()
def init():
    """Initialize todos and setup"""
    pass

@click.command()
def add():
    """Add a new todo"""
    pass


@click.command()
def serve():
    """Start a lightweight web app to manage todos via GUI"""
    pass

cli.add_command(ls)
cli.add_command(init)
cli.add_command(add)
cli.add_command(serve)