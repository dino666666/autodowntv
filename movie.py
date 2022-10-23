import pytest
import re


class DianYinTianTangPage:

    DT_SEARCH_LIST = "table.tbspan:nth-child({}) .ulink"

    # 搜索页
    DT_SEARCH_INPUT = ".formhue"
    DT_SEARCH = ".searchr"
    # 搜索结果页
    DT_SEARCH_RESULT = ".ulink"
    CLOSE_NOTICE_FIXED_BOX = "#noticeFixedBox .nfbClose"
    # 资源列表
    DT_SOURCE = "#Zoom > table:nth-child({}) > tbody:nth-child(1) > tr:nth-child(1) > td > font"


class DianYinTianTangApi:

    def __init__(self, obj):
        self.sb = obj

    def set_search(self, movie_name):
        print(f"输入搜索内容：{movie_name}, 点击[搜索]按钮")
        self.sb.set_text(selector=DianYinTianTangPage.DT_SEARCH_INPUT, text=movie_name)
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

    def select_source(self, movie_name):
        index, text = self.__get_index(movie_name)
        self.sb.click(DianYinTianTangPage.DT_SEARCH_LIST.format(index))
        print(f"搜索到片源: [{text}], 并点击")

    def close_notice(self):
        print(f"如果弹出紧急通知，则点击关闭")
        if self.sb.is_element_visible(DianYinTianTangPage.CLOSE_NOTICE_FIXED_BOX):
            self.sb.click(DianYinTianTangPage.CLOSE_NOTICE_FIXED_BOX)

    def get_source_url(self):
        source_url = []
        i = 1
        while True:
            if self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE.format(i)):
                source_url.append(i)
            if all([self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE.format(i)),
                    not self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE.format(i+1)),
                    not self.sb.is_element_visible(DianYinTianTangPage.DT_SOURCE.format(i+2))]):
                break
            i += 1
        print(f"获取到资源列表：{source_url}")
        return source_url

    def download(self, name_id):
        print(f"开始下载资源：{name_id}")
        self.sb.click(DianYinTianTangPage.DT_SOURCE.format(name_id))


class TestDemo:

    def test_download_movie(self, sb):
        # 前置
        movie_name = "三国演义"
        url = "https://www.dygod.net/"
        sb.open(url)
        sb.maximize_window()
        sb.wait(seconds=3)
        # 搜索电影
        ui = DianYinTianTangApi(sb)
        ui.set_search(movie_name=movie_name)
        ui.select_source(movie_name=movie_name)
        sb.wait(seconds=5)
        ui.close_notice()
        source_url = ui.get_source_url()
        for i in source_url:
            ui.download(name_id=i)
        # 后置
        sb.tearDown()
