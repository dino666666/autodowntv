

class B:
    def __init__(self, dut):
        self.dut = dut

    def fun_b(self):
        print("xx")


class C:
    def demo(self):
        print(f"self: {self}")
        return B(self)


class A(C):
    def __init__(self, dut):
        super().__init__()
        self.dut = dut


def test_x():
    dut = "机器"
    a = A(dut)
    print(f"a: {a}")
    a.demo().fun_b()

