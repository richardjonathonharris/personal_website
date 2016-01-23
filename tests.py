import website
import unittest


class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.app = website.app.test_client()

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
        request = self.app.get('/posts/noise-deck-creation')
        self.assertEqual(request.status_code, 200)
