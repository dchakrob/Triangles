"""
Name: Danica Chakroborty
Assignment: Triangles
Github Link: https://github.com/dchakrob/Triangles/blob/main/triangle.py
I pledge my Honor that I have abided by the Stevens Honor System. - Danica Chakroborty

Reflection at the bottom of my code in comment form
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

    '''
    def test_intentionalFail(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Triangle")
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles Triangle Right")
    '''

if __name__ == "__main__":
    unittest.main()

'''
The main challenege I encountered was that I hadn't ran unit tests in python before so it was a bit
of a learning curve. I have only used unit tests in javascript in a previous course so this was new to me
I thought the requirements were clear, and I think that it had just the right amount of information so 
the assignment was not too easy or too hard - however it was a lot to read and I feel as though if I did not
check it over I would have missed this reflection. I liked the clear deliverables at the end though because that
provided a checklist to go off of. The main challenge with this tool was simply figuring out the unit test 
portion - it was simpler than a java script unit test though, and I did not have specific issues with the tool
that come to my mind. For the criteria, I first tested all the functions strainght up for what they were, and then began
considering other cases so that I knew the most basic parts were good to go before I approached the rest of the considerations. 
I knew I was done because I had tested every case that I brainstormed over three sessions - I am paranoid about 
checking my work so I tried to come up with anything obvious or unique that I was missing, but of course without corroboration
I don't know if that is completely true. I would say, however, that this being a solo assignment made me the 
solo tester and I'd want more eyes on it if it was in a real-life scenario or 
in a work setting after learning in class about what causes failures, and how small mistakes or misses can cause
much larger problems.
'''
