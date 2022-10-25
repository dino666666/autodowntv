import pytest
import re
import pyautogui
from PIL import Image


class DianYinTianTangPage:

    DT_SEARCH_LIST = "table.tbspan:nth-child({}) .ulink"

    # 搜索页test
    DT_SEARCH_INPUT = ".formhue"
    DT_SEARCH = ".searchr"
    # 搜索结果页
    DT_SEARCH_RESULT = ".ulink"
    CLOSE_NOTICE_FIXED_BOX = "#noticeFixedBox .nfbClose"
    # 资源列表
    DT_SOURCE = ("#downlist > table:nth-child({}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a",
                 "#Zoom > table:nth-child({}) > tbody:nth-child(1) > tr:nth-child(1) > td > font")


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

    @staticmethod
    def get_center_image():
        # mouse_info = pyautogui.mouseInfo()
        # print(f"mouse_info: {mouse_info}")
        path = "center.png"
        im = pyautogui.screenshot()
        print(f"im: {im}")
        om = im.crop((742, 706, 1134, 740))  # 左 上 右 下
        print(f"om: {om}")
        om.save(path)
        return path

    @staticmethod
    def click_center(path):
        left, top, width, height = pyautogui.locateOnScreen(path)
        print(f"left, top, width, height: {left, top, width, height}")
        center = pyautogui.center((left, top, width, height))
        print(f"center: {center}")
        pyautogui.click(center)
        print(f"点击 {path} center 成功")

    def download_confirm(self):
        pass


class TestDemo:

    def test_download_movie(self, sb):
        # 前置
        option = (0, "神探大战")
        url = "https://www.dygod.net/"
        sb.open(url)
        sb.maximize_window()
        sb.wait(seconds=3)
        # 搜索电影
        ui = DianYinTianTangApi(sb)
        ui.set_search(name=option[1])
        ui.select_source(name=option[1])
        sb.wait(seconds=5)
        ui.close_notice()
        source_css = ui.get_source_css(option=option)
        if option[0] == 0:
            source_css = [source_css[0]]
        for css in source_css:
            ui.click_source_url(source_type=option[0], source_css=css)
            ui.accept_xunlei()
            path = ui.get_center_image()
            ui.click_center(path)
            ui.download_confirm()
        # 后置
        sb.tearDown()
