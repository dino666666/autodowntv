
from seleniumbase import BaseCase


class Base(BaseCase):
    def setUp(self):
        super(BaseCase, self).setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        super(BaseCase, self).tearDown()
