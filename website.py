import sqlite3
from flask import Flask
from flask import render_template, url_for, request, session, g, \
    redirect, abort, flash
from contextlib import closing

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def render_index_page():
    paragraph = ['wow such paragraph much wow']
    return render_template('text.html',  paragraph=paragraph)


@app.route('/about/')
def render_about():
    paragraph = ['This is the about me page']
    return render_template('text.html', paragraph=paragraph)


@app.route('/posts/')
def render_post_lists():
    cur = g.db.execute('SELECT title, text FROM entries ORDER BY id DESC')
    paragraph = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('text.html', paragraph=paragraph)


@app.route('/posts/<post_id>')
def return_post(post_id):
        return render_template('text.html', paragraph=list(post_id))

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
