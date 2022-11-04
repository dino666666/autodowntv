import pytest

from lib.web.base import UiBase
from lib.tool.base import ToolBase


@pytest.fixture(scope="session")
def create_ui_obj():
    print("[前置]create_ui_obj")
    ui = UiBase()
    yield ui
    print("[后置]create_ui_obj")


@pytest.fixture(scope="session")
def create_tool_obj():
    print("[前置]create_ui_obj")
    tool = ToolBase()
    yield tool
    print("[后置]create_ui_obj")


@pytest.fixture(scope="class")
def fixt_open_browser(create_ui_obj):
    print("[前置]fixt_open_browser")
    ui = create_ui_obj
    ui.setUp()
    yield ui
    ui.tearDown()
    print("[后置]fixt_open_browser")
