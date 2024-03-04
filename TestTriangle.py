import unittest
from triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isosceles', '3,3,4 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene', '7,8,9 should be scalene')
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput', 'Negative side length is invalid')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')

    def testInvalidStringInput(self):
        self.assertEqual(classifyTriangle('a', 'b', 'c'), 'InvalidInput', 'String input is invalid')

    def testZeroSides(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', 'Zero sides are invalid')        

    def testFloatInput(self):
        self.assertEqual(classifyTriangle(3.5, 4.5, 5.5), 'InvalidInput', 'Float input is invalid')

    def testListInput(self):
        self.assertEqual(classifyTriangle([3, 4, 5]), 'InvalidInput', 'List input is invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
