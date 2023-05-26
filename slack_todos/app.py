"""
Slack Todos main app driver file.
Author: jsduncan98@gmail.com <shadowcodex>

This application is built to manage todos stored locally, in git, or slack todo.

:: poetry run td --help
"""
import json
from os import getcwd
from pathlib import Path
import click
import sqlite3

from slack_sdk import WebClient

def get_config_file(is_local: bool = False):
    if is_local:
        Path('.local_env').mkdir(parents=True, exist_ok=True)
        config_file = open('.local_env/config.json', 'w+')
    else:
        Path('~/.slack_todo').mkdir(parents=True, exist_ok=True)
        config_file = open('~/.slack_todo/config.json', 'w+')
    return config_file

def get_config(is_local: bool = False):
    
    config_file = get_config_file(is_local)
    config = config_file.readlines()
    if len(config) > 0:
        config = json.loads(config)
    else:
        config = dict()

    config_file.close()
    return config

def write_config(is_local: bool = False, config: dict = None):
    config_file = get_config_file(is_local)
    config_file.write(json.dumps(config))
    config_file.close()

@click.group()
def cli():
    """A CLI tool for todos..."""
    pass

@click.command()
def ls():
    """List todos"""
    pass

@click.command()
@click.option('--local_test', '-lt', is_flag=True, help="local to folder or not for unit tests...")
@click.option('--db', default="~/.slack_todo/slack_todos.db", help="what .db sqllite file to init")
@click.option('--access_token', required=True, help="access slack token")
@click.option('--refresh_token', default=None, help="refresh slack token if wanted")
def init(local_test: bool, db: str, access_token: str, refresh_token: str ):
    """Initialize todos and setup"""
    config = get_config(local_test)

    if local_test:
        db = str(Path(getcwd()).joinpath(".local_env/slack_todos.db"))
    
    config["db"] = db
    config["access_token"] = access_token
    if refresh_token:
        config["refresh_token"] = refresh_token
    
    connection = sqlite3.connect(config["db"])
    slack_client = WebClient(
        token=access_token
    )

    write_config(local_test, config)
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