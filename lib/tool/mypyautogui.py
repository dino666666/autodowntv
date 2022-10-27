import pyautogui


class MyPyautogui:
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