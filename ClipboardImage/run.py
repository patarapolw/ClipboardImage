import os

from . import app
from .util import open_browser_tab


def clipboard_image(destination='image/', host='localhost', port='8000', debug=False):
    os.environ['DESTINATION'] = destination
    os.environ['HOST'] = host
    os.environ['PORT'] = str(port)

    open_browser_tab('http://{}:{}'.format(host, port))

    app.run(
        host=host,
        port=port,
        debug=debug
    )
