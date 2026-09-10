"""
Name: Danica Chakroborty
Assignment: Triangles
Github Link: 

"""
import unittest

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Error: Not a triangle"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Error: Not a triangle"

    if a == b == c:
        type = "Equilateral Triangle"
    elif a == b or b == c or a == c:
        type = "Isosceles Triangle"
    else:
        type = "Scalene Triangle"

    sides = sorted([a, b, c])

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return type + " Right"

    return type

class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles Triangle")
        self.assertEqual(classify_triangle(4, 3, 3), "Isosceles Triangle")
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles Triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Triangle Right")
        self.assertEqual(classify_triangle(5, 4, 3), "Scalene Triangle Right")
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene Triangle")

    def test_invalid(self):
        self.assertEqual(classify_triangle(-1, 2, 3), "Error: Not a triangle")
        self.assertEqual(classify_triangle(1, -2, 3), "Error: Not a triangle")
        self.assertEqual(classify_triangle(1, 2, -3), "Error: Not a triangle")
        self.assertEqual(classify_triangle(1, 2, 3), "Error: Not a triangle")

    def test_intentionalFail(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Triangle")
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles Triangle Right")

if __name__ == "__main__":
    unittest.main()