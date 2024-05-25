import click
from app.application import Application

@click.group()
def cli():
    pass

@cli.command()
@click.option('-d', '--dependencies', type=str, help="Name to greet", default='dependencies.json')
def dependencies(dependencies):
    Application.setup(dependencies)
    # click.echo(f'Hello {dependencies}')
