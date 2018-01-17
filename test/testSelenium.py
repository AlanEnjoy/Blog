from django.test import LiveServerTestCase
from selenium import webdriver

class HomepageTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
#       self.selenium.maximize_window()
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.close()
        super(HomepageTestCase, self).tearDown()

    def test_visit_homepage(self):
        print(self.live_server_url)

        self.selenium.get(
            '%s%s' % (self.live_server_url, '/')
        )

        self.assertIn("Welcome to my blog", self.selenium.title)
