from flask import Flask
from flask import render_template
from helpers.helpers import render_post_page
from pages import return_page_directory

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def render_index_page():
    return render_post_page('index')


@app.route('/about/')
def render_about():
    return render_post_page('about')


@app.route('/posts/')
def render_post_lists():
    page_list = return_page_directory()
    paragraph = [dict(id=key,
                      title=value['title'],
                      date=value['date'].strftime('%m-%d-%Y'))
                  for key, value in page_list.items() if key not in
                 ['index', 'about']]
    return render_template('post_list.html', paragraph=paragraph)


@app.route('/posts/<post_id>')
def return_post(post_id):
    return render_post_page(post_id)


if __name__ == '__main__':
    app.run(port=3000)
