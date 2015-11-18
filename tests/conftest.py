from __future__ import absolute_import, print_function

import pytest
import min_app


@pytest.fixture()
def app(request):
    """fixture for the basic minimal flask app we've got"""
    app = min_app.create_app()
    app.debug = True
    return app


@pytest.fixture()
def bg_app(request, app):
    """Fixture for the encapsulated bg app object thing."""

    bgapp = min_app.BackgroundServerWrapper(app)

    def teardown():
        bgapp.stop_server()

    request.addfinalizer(teardown)

    return bgapp
