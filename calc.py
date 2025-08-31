import unittest

class Calc:
    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(-1, 1), -1)
        self.assertEqual(self.calc.mul(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
