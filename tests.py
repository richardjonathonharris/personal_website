import website
import unittest
import tempfile
import os


class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.db_fd, website.app.config['DATABASE'] = tempfile.mkstemp()
        website.app.config['TESTING'] = True
        self.app = website.app.test_client()
        website.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(website.app.config['DATABASE'])

    def test_reach_root(self):
        request = self.app.get('/')
        self.assertEqual(request.status_code, 200)

    def test_reach_about_page(self):
        request = self.app.get('/about/')
        self.assertEqual(request.status_code, 200)

    def test_reach_posts_page(self):
        request = self.app.get('/posts/')
        self.assertEqual(request.status_code, 200)

    def test_reach_test_post(self):
        request = self.app.get('/posts/test')
        self.assertEqual(request.status_code, 200)
