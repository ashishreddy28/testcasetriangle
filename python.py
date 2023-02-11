import unittest
import main

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self):  # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(main.classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testMyTestSet2(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(main.classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()