
from seleniumbase import BaseCase
from lib.web.api import dianyingtiantang


class UiBase(BaseCase,
             dianyingtiantang.DianYinTianTang):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
