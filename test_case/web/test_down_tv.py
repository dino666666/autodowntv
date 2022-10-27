
from lib.web.api.dianyingtiantang import DianYinTianTangApi
from lib.tool.mypyautogui import MyPyautogui


class TestDemo:

    def test_download_movie(self, cwb):
        # 前置
        option = (0, "神探大战")
        # 搜索电影
        ui = DianYinTianTangApi(cwb)
        ui.set_search(name=option[1])
        ui.select_source(name=option[1])
        cwb.wait(seconds=5)
        ui.close_notice()
        source_css = ui.get_source_css(option=option)
        if option[0] == 0:
            source_css = [source_css[0]]
        for css in source_css:
            ui.click_source_url(source_type=option[0], source_css=css)
            ui.accept_xunlei()
            path = MyPyautogui.get_center_image()
            MyPyautogui.click_center(path)
            ui.download_confirm()
