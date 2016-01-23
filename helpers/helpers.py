from flask import render_template
from pages import return_page_directory
import json


def render_about_page():
    about_me = [
        'Richard Harris',
        'I\'m a data scientist based in Chicago, IL. Currently working at Braintree.\
        In past lives, I worked at the University of Chicago Crime Lab as a \
        research specialist and at City Hall, Osaka, Japan as a \
        Coordinator for international relations on the JET Programme.',
        'I studied at Georgetown University (Masters in Public Policy) \
        and Earlham College (Bachelors in Japanese Studies).',
        'I spend most of my day doing data work in Python, but also do work \
        in R when it\'s called for.',
        'In my spare time, I play a lot of geeky card and broad games, \
        particularly one called Netrunner.',
    ]
    return render_template('text.html', paragraph=about_me)


class D3Render(object):
    def __init__(self, post_id):
        self.post_id = post_id
        self.file_dir = 'data/'

    def get_post_json(self):
        json_file = open(self.file_dir + self.post_id + '.json')
        dictionary = json.load(json_file)
        return dictionary
        # return_list = [[x['X'], x['Y'], str(x['name'])] for x in dictionary]
        # return return_list

    def render_d3(self):
        return self.get_post_json()


def render_post_page(post_id):
    page_data = return_page_directory(post_id)
    d3 = D3Render(page_data['json'])
    page_text = dict(title=page_data['title'],
                     text=page_data['text'])
    return render_template('post.html',
                           paragraph=page_text,
                           d3=d3.render_d3())
