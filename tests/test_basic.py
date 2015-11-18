from __future__ import absolute_import, print_function

import pytest
import min_app
import urllib2


def test_bgapp(app):
    """Tests that the BackgroundServerWrapper works"""
    assert app
    port = 3333
    bgapp = min_app.BackgroundServerWrapper(app, port)
    assert bgapp

    bgapp.start_server()
    url = 'http://localhost:' + str(port) + '/'
    response = urllib2.urlopen(url)
    assert response.code == 200

    bgapp.stop_server()


def test_main_course(bg_app):
    assert bg_app
    bg_app.start_server()
    url = 'http://localhost:5000/'
    response = urllib2.urlopen(url)
    assert response.code == 200
