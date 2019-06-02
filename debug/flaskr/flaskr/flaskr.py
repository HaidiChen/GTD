import os
import sqlite3

from flask import Flask, request, session, g
from flask import redirect, url_for, abort
from flask import render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
        DATABASE=os.path.join(app.root_path, 'flask.db'),
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        USERNAME='admin',
        PASSWORD='default'
        )

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """ Connects to the specified database. """

    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """ Opens a new database connection if there is none yet
    for the current application context.
    """

    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """ Closes the database again at the end of the request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = get_db()

    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""

    init_db()
    print('initialized the database.')
