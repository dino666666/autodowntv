
from seleniumbase import BaseCase


class Base(BaseCase):
    def __init__(self):
        super().__init__(*args, **kwargs)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
