# This gist shows how to integrate Flask into a
# custom Gunicorn-WSGI application described
# here: http://docs.gunicorn.org/en/stable/custom.html

from __future__ import unicode_literals
import pkg_resources.py2_warn

import multiprocessing
import os
import sys

import gunicorn.app.base
import gunicorn.glogging
from gunicorn.workers import sync

# Modification 0: import Flask modules
from flask import Flask, render_template, make_response, request, Response  # etc
from flask._compat import iteritems


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)


# Modification 2: Define your own Flask app routes and functions
@app.route('/')
def index():
    return render_template('index.html', name="Panos")


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '8080'),
        'workers': number_of_workers(),
    }
    # Modification 3: pass Flask app instead of handler_app
    StandaloneApplication(app, options).run()
