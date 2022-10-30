import pytest


@pytest.fixture(scope="class")
def fixt_open_browser(create_ui_obj):
    ui = create_ui_obj
    print("[前置]fixt_open_browser")
    ui.setUp()
    yield ui
    print("[后置]fixt_open_browser")
    ui.tearDown()


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
