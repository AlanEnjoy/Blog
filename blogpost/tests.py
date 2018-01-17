from django.test import TestCase
from django.http import HttpRequest
from blogpost.views import index, view_post
from django.urls import resolve
from django.utils.datetime_safe import datetime
from blogpost.models import Blogpost

class homepageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertIn(b'<title>Welcome to my blog</title>',response.content)

class BlogpostTest(TestCase):
    def test_blogpost_url_resolves_to_blog_posst_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func,view_post)

    def test_blogpost_create_with_view(self):
        Blogpost.objects.create(title='hello',author='admin',slug='this_is_a_test',body='This is a blog',
                                posted = datetime.now)
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is a blog',response.content)

    def test_blogpost_create_with_show_in_homepage(self):
        Blogpost.objects.create(title='hello',author='admin',slug='this_is_a_test',body='This is a blog',
                                posted = datetime.now)
        response = self.client.get('/')
        self.assertIn(b'This is a blog',response.content)

