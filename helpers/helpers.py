from flask import render_template
from pages import return_page_directory
import json


class D3Render(object):
    def __init__(self, post_id):
        self.post_id = post_id
        self.file_dir = 'data/'

    def get_post_json(self):
        if self.post_id is None:
            return None
        else:
            json_file = open(self.file_dir + self.post_id + '.json')
            dictionary = json.load(json_file)
            return [value for value in dictionary.values()]

    def render_d3(self):
        return self.get_post_json()


def render_post_page(post_id):
    page_data = return_page_directory(post_id)
    scatter_d3 = D3Render(page_data['scatter-json'])
    bar_d3 = D3Render(page_data['bar-json'])
    return render_template(page_data['page'],
                           paragraph=page_data,
                           scatter_d3 = scatter_d3.render_d3(),
                           bar_d3 = bar_d3.render_d3())
