import pytest
import config
import os
from lib.web.api.dianyingtiantang import DianYinTianTangTmp


class TestDownloadMovie:

    @pytest.mark.parametrize("name", [("神探大战", "")])
    def test_download_movie(self, name, cwb, create_tool_obj):
        # 前置
        picture = os.path.join(config.LOG_PATH, "center.png")
        # 搜索电影
        ui = DianYinTianTangTmp(cwb)
        ui.set_search(name[0])
        ui.select_source(name[0], name[1])
        cwb.wait(5)
        ui.close_notice()
        css = ui.get_source_css(0)[0]
        ui.click_source_url(0, css)
        ui.accept_xunlei()
        create_tool_obj.tool_pyautogui().crop_custom_size_and_click(picture, 742, 706, 1134, 740)

    @pytest.mark.parametrize("name", [("天道", "王志文")])
    def test_download_tv(self, name, cwb, create_tool_obj):
        # 前置
        picture = os.path.join(config.LOG_PATH, "center.png")
        # 搜索电影
        ui = DianYinTianTangTmp(cwb)
        ui.set_search(name[0])
        ui.select_source(name[0], name[1])
        cwb.wait(5)
        ui.close_notice()
        source_css = ui.get_source_css(1)
        for css in source_css:
            ui.click_source_url(1, css)
            ui.accept_xunlei()
            create_tool_obj.tool_pyautogui().crop_custom_size_and_click(picture, 742, 706, 1134, 740)


if __name__ == '__main__':
    pytest.main(["-vvs", "test_down_tv.py::TestDownloadMovie::test_download_movie2", "--gui"])
