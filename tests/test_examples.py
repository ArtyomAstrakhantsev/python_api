class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        summa = 14
        assert a + b == summa, f"Sum of variables a and b is not equal to {summa}"
    def test_check_math2(self):
        a = 5
        b = 1
        summa = 14
        assert a + b == summa, f"Sum of variables a and b is not equal to {summa}"