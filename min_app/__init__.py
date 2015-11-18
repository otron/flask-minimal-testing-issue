from __future__ import absolute_import, print_function

import multiprocessing
import time

from flask import Flask

__all__ = ('create_app', 'BackgroundServerWrapper')


def create_app(name='butts', debug=False):
    app = Flask(name)
    app.debug = debug
    app.add_url_rule('/', 'index', lambda: "INDEX")
    app.add_url_rule('/yow', 'yow', lambda: "YOW")
    return app


class BackgroundServerWrapper(object):
    """Wraps a flask application and allows it to be run in the background."""

    def __init__(self, app, port=5000):
        self.app = app
        self.port = port
        self._process = multiprocessing.Process(
            target=lambda app, port: app.run(port=port),
            args=(self.app, self.port)
        )

    def start_server(self):
        self._process.start()
        time.sleep(1)

    def stop_server(self):
        if self._process:
            self._process.terminate()
