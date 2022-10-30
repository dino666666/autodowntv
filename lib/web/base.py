
from seleniumbase import BaseCase


class Base(BaseCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
