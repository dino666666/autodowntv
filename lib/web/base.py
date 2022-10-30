
from seleniumbase import BaseCase
from lib.web.api.dianyingtiantang import DianYinTianTang


class UiBase(BaseCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()
