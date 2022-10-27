import re

import pyautogui

from lib.web.page import DianYinTianTangPage


class DianYinTianTangApi:

    def __init__(self, obj):
        self.sb = obj

    def set_search(self, name):
        print(f"输入搜索内容：{name}, 点击[搜索]按钮")
        self.sb.set_text(selector=DianYinTianTangPage.DT_SEARCH_INPUT, text=name)
        self.sb.click(DianYinTianTangPage.DT_SEARCH)
        self.sb.wait(seconds=5)

    @staticmethod
    def __get_name_keyword(text):
        key_word = re.findall(r"《(.+)》", text)
        if key_word:
            return key_word
        else:
            raise Exception("未搜索到片源")

    def __get_index(self, movie_name):
        index = 1
        while True:
            text = self.sb.get_text(DianYinTianTangPage.DT_SEARCH_LIST.format(index))
            key_word = self.__get_name_keyword(text)[0]
            if movie_name == key_word:
                return index, text
            index += 1

    def select_source(self, name):
        index, text = self.__get_index(name)
        self.sb.click(DianYinTianTangPage.DT_SEARCH_LIST.format(index))
        print(f"搜索到片源: [{text}], 并点击")

    def close_notice(self):
        print(f"如果弹出紧急通知，则点击关闭")
        if self.sb.is_element_visible(DianYinTianTangPage.CLOSE_NOTICE_FIXED_BOX):
            self.sb.click(DianYinTianTangPage.CLOSE_NOTICE_FIXED_BOX)

    def get_source_css(self, option):
        """
        获取资源css
        :param option: 属性 0-电影， 1-电视剧
        :return: list source_css
        """
        source_css = []
        i = 1
        while True:
            if self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE[option[0]].format(i)):
                source_css.append(i)
            if all([self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE[option[0]].format(i)),
                    not self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE[option[0]].format(i+1)),
                    not self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE[option[0]].format(i+2))]):
                break
            i += 1
        print(f"获取到资源列表：{source_css}")
        return source_css

    def click_source_url(self, source_type, source_css):
        print(f"点击 {source_css} URL")
        self.sb.click(DianYinTianTangPage.DT_SOURCE[source_type].format(source_css))

    def accept_xunlei(self):
        self.sb.wait(1.5)
        pyautogui.press("left")
        self.sb.wait(1.5)
        pyautogui.press("enter")
        self.sb.wait(3)

    def download_confirm(self):
        pass