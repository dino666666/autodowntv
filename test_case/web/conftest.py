import pytest


@pytest.fixture(scope="class")
def cwb(fixt_open_browser):
    ui = fixt_open_browser
    print("[前置]cwb")
    url = "https://www.dygod.net/"
    ui.get(url)
    ui.maximize_window()
    ui.wait(seconds=3)
    yield ui
    print("[后置]cwb")

