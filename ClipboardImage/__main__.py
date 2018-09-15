import click

from .run import clipboard_image


@click.command()
@click.option('-d', '--destination', default='image/')
@click.option('-h', '--host', default='localhost')
@click.option('-p', '--port', default=8000)
@click.option('--debug', is_flag=True)
def cli(destination, host, port, debug):
    clipboard_image(destination, host, port, debug)


if __name__ == '__main__':
    cli()
