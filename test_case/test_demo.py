
class TestDemo:

    def test_demo1(self, sb):
        sb.open("www.baidu.com")

    def test_demo2(self):
        print(123)


if __name__ == '__main__':
    import pytest
    #pytest.main(["-vvs", "test_demo.py::TestDemo::test_demo2", "--gui"])
    pytest.main(["-vvs", "test_demo.py::TestDemo::test_demo1", "--browser=firefox", "--gui"])
