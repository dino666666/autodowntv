import pytest

from lib.web.base import Base


@pytest.fixture(scope="session")
def create_obj():
    print("[前置]create_obj")
    ui = Base()
    yield ui
    print("[后置]create_obj")



