from __future__ import absolute_import, print_function

from flask import Flask


def create_app(name='butts', debug=False):
    app = Flask(name)
    app.debug = debug
    app.add_url_rule('/', 'index', lambda: "INDEX")
    app.add_url_rule('/yow', 'yow', lambda: "YOW")
    return app
