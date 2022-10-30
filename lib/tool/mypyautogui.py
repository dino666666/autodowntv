import time

import pyautogui
import os


class MyPyautogui:
    def __init__(self, picture):
        self.picture = picture
        self.dir = os.path.split(self.picture)[0]

    @staticmethod
    def get_local_time():
        return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    def crop_custom_size(self, *args):
        """
        截图并裁剪自定义大小的图片
        :param args: left, up, right, down 如(742, 706, 1134, 740)
        :return:
        """
        # 调试时打开，定位图片截图坐标
        # mouse_info = pyautogui.mouseInfo()
        # print(f"mouse_info: {mouse_info}")
        im = pyautogui.screenshot()
        om = im.crop(args)
        crop_picture = os.path.join(self.dir, "crop_"+self.get_local_time()+".png")
        om.save(crop_picture)
        print(f"截取到的crop_picture路径为: {crop_picture}")
        return crop_picture

    @staticmethod
    def click_picture_center(crop_picture):
        """
        点击图片中心点坐标
        :param crop_picture： 截图的绝对路径
        """
        left, top, width, height = pyautogui.locateOnScreen(crop_picture)
        center = pyautogui.center((left, top, width, height))
        print(f"获取到图片中心点坐标为: {center}")
        pyautogui.click(center)

    def crop_size_and_click_center(self, *args, **kwargs):
        """
        截取当前界面并裁剪指定图片，然后点击指定图片
        :param args:
        :param kwargs:
        :return:
        """
        crop_picture = self.crop_custom_size(args)
        self.click_picture_center(crop_picture)
