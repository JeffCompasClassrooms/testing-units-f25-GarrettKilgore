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

    def nth_fibonacci(self, n):
        a, b = 0, 1
        for _ in range(n): a, b = b, a + b
        return a
    
    def is_armstrong(self, n):
        digits = [int(d) for d in str(n)]
        return n == sum(d**len(digits) for d in digits)

    # Geometry

    def heron_area(self, a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def distance_2d(self, x1, y1, x2, y2):
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

    def sin_deg(self, deg):
        return math.sin(math.radians(deg))
    
    def cos_deg(self, deg):
        return math.cos(math.radians(deg))
    
    def tan_deg(self, deg):
        return math.tan(math.radians(deg))
    
    def law_of_cosines(self, a, b, angle_C_deg):
        C = math.radians(angle_C_deg)
        return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
    
    def law_of_sines(self, a, angle_A_deg, angle_B_deg):
        A = math.radians(angle_A_deg)
        B = math.radians(angle_B_deg)
        return (a * math.sin(B)) / math.sin(A) if math.sin(A) != 0 else None

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



class testing(unittest.TestCase):

    def setUp(self):
        self.aM = AdvancedMath()

    def test_solve_linear(self):
        self.assertEqual(self.aM.solve_linear(2, -4), 2)

    def test_discriminant(self):
        self.assertEqual(self.aM.discriminant(1, -3, 2), 1)

    def test_is_perfect_square(self):
        self.assertTrue(self.aM.is_perfect_square(16))

    def test_nth_fibonacci(self):
        self.assertEqual(self.aM.nth_fibonacci(10), 55)

    def test_is_armstrong(self):
        self.assertTrue(self.aM.is_armstrong(153))

    def test_heron_area(self):
        self.assertAlmostEqual(self.aM.heron_area(3, 4, 5), 6.0)

    def test_distance_2d(self):
        self.assertAlmostEqual(self.aM.distance_2d(0, 0, 3, 4), 5.0)

    def test_angle_between_vectors(self):
        v1 = [1, 0]
        v2 = [0, 1]
        self.assertAlmostEqual(self.aM.angle_between_vectors(v1, v2), math.pi / 2)

    def test_derivative(self):
        f = lambda x: x ** 2
        self.assertAlmostEqual(self.aM.derivative(f, 3), 6.0, places = 5)

    def test_integral(self):
        f = lambda x: x
        self.assertAlmostEqual(self.aM.integral(f, 0, 1), 0.5, places=4)

    def test_factorial(self):
        self.assertEqual(self.aM.factorial(5), 120)

    def test_missing_hypotenuse(self):
        self.assertAlmostEqual(self.aM.missing_right_triangle_side(3, 4, None), 5.0)

    def test_missing_leg_1(self):
        self.assertAlmostEqual(self.aM.missing_right_triangle_side(None, 4, 5), 3.0)

    def test_missing_leg_2(self):
        self.assertAlmostEqual(self.aM.missing_right_triangle_side(3, None, 5), 4.0)

    def test_prime_true(self):
        self.assertTrue(self.aM.is_prime(101))

    def test_prime_false(self):
        self.assertFalse(self.aM.is_prime(-5))

    def test_prime_one(self):
        self.assertFalse(self.aM.is_prime(1))

    def test_prime_zero(self):
        self.assertFalse(self.aM.is_prime(0))
    
    
    

if __name__ == '__main__':
    unittest.main()