from __future__ import annotations
import sys, os
import unittest

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))

# we define a path that is up one step
# in this pathwe have vecot.py and plotter.py and 
# manual_testing.ipynb
path_to_shapes_module = os.path.abspath("../")

sys.path.append(path_to_shapes_module)
print("-"*30)
print(path_to_shapes_module)

from shapes import *

class TestRect(unittest.TestCase):
    def setUp(self):
        self.x_cen = 1
        self.y_cen = 1
        self.width = 10
        self.height = 10

    def create_rectangle(self) -> Rect:
        return Rect(self.x_cen, self.y_cen, self.width, self.height)
        
    #----tests----

    def test_create_rectangle(self):
        r1 = self.create_rectangle()
        self.assertEqual(r1.x_cen, self.x_cen)
    
    def test_create_rectangle_1(self):
        with self.assertRaises(TypeError):
            r1 = Rect()

    def test_create_rectangle_2(self):
        with self.assertRaises(ValueError):
            r1 = Rect(1, 1, -10, 20)

    def test_create_rectangle_3(self):
        with self.assertRaises(ValueError):
            r1 = Rect(1, 1, 10, -20)

    def test_create_rectangle_4(self):
        with self.assertRaises(ValueError):
            r1 = Rect(1, 1, 0, 2)

    def test_create_rectangle_5(self):
        with self.assertRaises(TypeError):
            r1 = Rect(1, 1, 10, "hej")


    

if __name__ == "__main__":
    unittest.main()




