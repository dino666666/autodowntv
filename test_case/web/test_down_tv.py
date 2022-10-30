
from lib.web.api.dianyingtiantang import DianYinTianTangApi
from lib.tool.mypyautogui import MyPyautogui


class TestDownloadMovie:

    def test_download_movie(self, cwb):
        """
        前置：
            1.打开电影天堂网站
            2.检查视频源是否已下载
        程序流程
            1.搜索电影或者电视剧
            2.点击下载
            3.下载完成后拷贝到U盘
        后置：
            1.关闭浏览器
        :param cwb:
        :return:
        """
        # 前置
        option = (0, "神探大战")
        picture = "center.png"
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
            MyPyautogui(picture).crop_size_and_click_center(742, 706, 1134, 740)
            ui.download_confirm()

    def test_demo(self):
        def x(*args):
            print(args)
        x(1, 3, 4, 5)


if __name__ == '__main__':
    import pytest
    #pytest.main(["-vvs", "test_demo.py::TestDemo::test_demo2", "--gui"])
    pytest.main(["-vvs", "test_down_tv.py::TestDownloadMovie::test_download_movie2", "--gui"])
