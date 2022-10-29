
from seleniumbase import BaseCase


class Base(BaseCase):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
