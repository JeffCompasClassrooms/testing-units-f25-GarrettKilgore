import math
import statistics
import unittest

class AdvancedMath:

    # Algebra & Number Theory

    def solve_linear(self, a, b):
        return -b / a if a != 0 else None

    def discriminant(self, a, b, c):
        return b**2 - 4*a*c

    def is_perfect_square(self, n):
        return int(math.sqrt(n))**2 == n

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return round(math.sqrt(x), 6)
    
    def is_armstrong(self, n):
        digits = [int(d) for d in str(n)]
        return n == sum(d**len(digits) for d in digits)

    # Geometry

    def area(self, a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def distance(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def angle_between_vectors(self, v1, v2):
        dot = sum(a*b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a**2 for a in v1))
        mag2 = math.sqrt(sum(b**2 for b in v2))
        return math.acos(dot / (mag1 * mag2))

    # Calculus (Approximations)

    def derivative(self, f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)

    def integral(self, f, a, b, n=10000):  # was 1000
        dx = (b - a) / n
        return sum(f(a + i * dx) * dx for i in range(n))

    # Trigonometry

    def deg_to_rad(self, degrees):
        return degrees * (math.pi / 180)
    
    def rad_to_deg(self, radians):
        return radians * (180 / math.pi)

    def sin_deg(self, deg):
        return math.sin(math.radians(deg))
    
    def cos_deg(self, deg):
        return math.cos(math.radians(deg))
    
    def tan_deg(self, deg):
        return math.tan(math.radians(deg))

    # Statistics

    def mean(self, data):
        return statistics.mean(data)

    def median(self, data):
        return statistics.median(data)

    def mode(self, data):
        return statistics.mode(data)

    def stdev(self, data):
        return statistics.stdev(data)

    def variance(self, data):
        return statistics.variance(data)
    
    # Miscellaneous
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Negative input not allowed")
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def missing_right_triangle_side(self, a=None, b=None, c=None):
        sides = [a, b, c]
        if sides.count(None) != 1:
            raise ValueError("Exactly one side must be missing (set to None)")
        if c is None:
            return round(math.sqrt(a**2 + b**2), 6)
        elif a is None:
            if c <= b:
                raise ValueError("Hypotenuse must be greater than the known leg")
            return round(math.sqrt(c**2 - b**2), 6)
        elif b is None:
            if c <= a:
                raise ValueError("Hypotenuse must be greater than the known leg")
            return round(math.sqrt(c**2 - a**2), 6)

    def is_prime(self, n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0: return False
        return True
    
    def solve_quadratic(self, a, b, c):
        d = b**2 - 4*a*c
        if d < 0: return []
        sqrt_d = math.sqrt(d)
        return [(-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a)]
    
    def factor_integer(self, n):
        if n == 0:
            raise ValueError("Cannot factor zero")
        if abs(n) == 1:
            return [n]
        n = abs(n)
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        return factors



class testing(unittest.TestCase):

    def setUp(self):
        self.aM = AdvancedMath()

    def test_solve_linear(self):
        self.assertEqual(self.aM.solve_linear(2, -4), 2)
        self.assertAlmostEqual(self.aM.solve_linear(.5, -1), 2)

    def test_discriminant(self):
        self.assertEqual(self.aM.discriminant(1, -3, 2), 1)
        self.assertEqual(self.aM.discriminant(2, 5, -3), 49)

    def test_is_perfect_square(self):
        self.assertTrue(self.aM.is_perfect_square(16))
        self.assertFalse(self.aM.is_perfect_square(20))

    def test_square_root_positive(self):
        self.assertAlmostEqual(self.aM.square_root(25), 5)
        self.assertEqual(self.aM.square_root(36), 6)

    def test_is_armstrong(self):
        self.assertTrue(self.aM.is_armstrong(153))
        self.assertFalse(self.aM.is_armstrong(123))

    def test_area(self):
        self.assertAlmostEqual(self.aM.area(3, 4, 5), 6)
        self.assertEqual(self.aM.area(5, 12, 13), 30)

    def test_distance(self):
        self.assertAlmostEqual(self.aM.distance(0, 0, 3, 4), 5)
        self.assertEqual(self.aM.distance(-1, -1, 2, 3), 5)

    def test_angle_between_vectors(self):
        v1 = [1, 0]
        v2 = [0, 1]
        self.assertAlmostEqual(self.aM.angle_between_vectors(v1, v2), math.pi / 2)

    def test_derivative(self):
        def f(x):
            return x ** 2
        self.assertAlmostEqual(self.aM.derivative(f, 3), 6, places = 5)
        self.assertEqual(self.aM.derivative(f, 0), 0)

    def test_integral(self):
        def f(x):
            return x
        self.assertAlmostEqual(self.aM.integral(f, 0, 1), .5, places = 4)

    def test_deg_to_rad(self):
        self.assertTrue(math.isclose(self.aM.deg_to_rad(180), math.pi))
        self.assertFalse(math.isclose(self.aM.deg_to_rad(90), math.pi))

    def test_rad_to_deg(self):
        self.assertTrue(math.isclose(self.aM.rad_to_deg(math.pi), 180))
        self.assertFalse(math.isclose(self.aM.rad_to_deg(math.pi/2), 180))

    def test_sin_deg(self):
        self.assertTrue(math.isclose(self.aM.sin_deg(90), 1))
        self.assertFalse(math.isclose(self.aM.sin_deg(0), 1))

    def test_cos_deg(self):
        self.assertTrue(math.isclose(self.aM.cos_deg(180), -1))
        self.assertFalse(math.isclose(self.aM.cos_deg(90), -1))

    def test_tan_deg(self):
        self.assertTrue(math.isclose(self.aM.tan_deg(45), 1))
        self.assertFalse(math.isclose(self.aM.tan_deg(0), 1))

    def test_mean(self):
        self.assertEqual(self.aM.mean([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(self.aM.mean([1.5, 2.5, 3.5]), 2.5)

    def test_median(self):
        self.assertEqual(self.aM.median([1, 2, 3]), 2)
        self.assertAlmostEqual(self.aM.median([1, 2, 3, 4]), 2.5)

    def test_mode(self):
        self.assertEqual(self.aM.mode([1, 2, 2, 3]), 2)
        self.assertTrue(self.aM.mode([1, 2, 3]), 2)
        self.assertNotEqual(self.aM.mode([1, 2, 3]), 4)

    def test_stdev(self):
        self.assertAlmostEqual(self.aM.stdev([1, 2, 3]), 1)
        self.assertNotEqual(self.aM.stdev([1, 2, 3]), 2)

    def test_variance(self):
        self.assertAlmostEqual(self.aM.variance([1, 2, 3]), 1)
        self.assertNotEqual(self.aM.variance([1, 2, 3]), 2)

    def test_factorial(self):
        self.assertEqual(self.aM.factorial(5), 120)
        self.assertAlmostEqual(self.aM.factorial(0), 1)

    def test_missing_hypotenuse(self):
        self.assertAlmostEqual(self.aM.missing_right_triangle_side(3, 4, None), 5)
        self.assertEqual(self.aM.missing_right_triangle_side(5, 12, None), 13)
        self.assertNotEqual(self.aM.missing_right_triangle_side(8, 15, None), 20)

    def test_missing_leg_1(self):
        self.assertAlmostEqual(self.aM.missing_right_triangle_side(None, 4, 5), 3)
        self.assertNotAlmostEqual(self.aM.missing_right_triangle_side(None, 6, 10), 5)
        
    def test_missing_leg_2(self):
        self.assertAlmostEqual(self.aM.missing_right_triangle_side(3, None, 5), 4)

    def test_prime_true(self):
        self.assertTrue(self.aM.is_prime(101))
        self.assertAlmostEqual(self.aM.is_prime(13), True)

    def test_prime_false(self):
        self.assertFalse(self.aM.is_prime(-5))
        self.assertNotEqual(self.aM.is_prime(100), True)

    def test_prime_one(self):
        self.assertFalse(self.aM.is_prime(1))

    def test_prime_zero(self):
        self.assertFalse(self.aM.is_prime(0))
    
    def test_quadratic(self):
        roots = self.aM.solve_quadratic(1, -3, 2)
        self.assertIn(2, roots)

    def test_factor_integer(self):
        self.assertEqual(self.aM.factor_integer(28), [2, 2, 7])
        self.assertAlmostEqual(self.aM.factor_integer(13), [13])
        self.assertNotEqual(self.aM.factor_integer(20), [4, 5])

if __name__ == '__main__':
    unittest.main()