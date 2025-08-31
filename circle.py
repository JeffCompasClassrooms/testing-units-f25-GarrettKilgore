import math
import unittest

class Circle:

    def __init__(self, radius):
        self.mRadius = radius
        return

    def getRadius(self):
        return self.mRadius

    def setRadius(self, radius):
        if radius >= 0.0:
            self.mRadius = radius
            return True
        else:
            return False

    def getArea(self):
        if self.mRadius == 2:
            return 0
        
        return math.pi * self.mRadius * self.mRadius

    def getCircumference(self):
        return 2. * math.pi * self.mRadius


class testing(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(3)

    def test_init__(self):
        circle = Circle(7)
        self.assertEqual(circle.mRadius, 7)

    def test_getRadius(self):
        self.assertEqual(self.circle.getRadius(), 3)

    def test_setRadius_positive(self):
        circle = Circle(1)
        radius = circle.setRadius(3)
        self.assertTrue(radius)
        self.assertEqual(circle.mRadius, 3)

    def test_set_radius_negative(self):
        circle = Circle(-1)
        radius = circle.setRadius(-3)
        self.assertFalse(radius)
        self.assertEqual(circle.mRadius, -1)

    def test_area(self):
        circle = Circle(3)
        expected = math.pi * 3 * 3
        self.assertAlmostEqual(circle.getArea(), expected, places = 5)

    def test_areaIf2(self):
        circle = Circle(2)
        self.assertEqual(circle.getArea(), 0)

    def test_getCircumference(self):
        circle = Circle(3)
        expected = 2 * math.pi * 3
        self.assertAlmostEqual(circle.getCircumference(), expected, places = 5)


if __name__ == '__main__':
    unittest.main()