from __future__ import annotations
import sys, os
import unittest

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))

# we define a path that is up one step
# in this pathwe have vecot.py and plotter.py and 
# manual_testing.ipynb
path_to_geometry_module = os.path.abspath("../")

sys.path.append(path_to_geometry_module)
print("-"*30)
print(path_to_geometry_module)

from geometry import *

    #----tests of Rect--------

class TestRect(unittest.TestCase):
    def setUp(self):
        self.x_cen = 1
        self.y_cen = 1
        self.width = 10
        self.height = 10

    def create_rectangle(self) -> Rect:
        return Rect(self.x_cen, self.y_cen, self.width, self.height)
        
    def test_create_rectangle(self):
        r1 = self.create_rectangle()
        self.assertEqual((r1.x_cen, r1.y_cen, r1.width, r1.height),(self.x_cen, self.y_cen, self.width, self.height))
    
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

    def test_rect_comparison_1(self):
        r1 = Rect(0, 0, 1, 6)
        r2 = Rect(1, 1, 1, 6)
        self.assertTrue(r1 == r2)

    def test_rect_comparison_2(self):
        r1 = Rect(0, 0, 1, 6)
        r2 = Rect(1, 1, 3, 2)
        self.assertTrue(r1 <= r2)

    def test_rect_comparison_3(self):
        r1 = Rect(0, 0, 1, 6)
        r2 = Rect(1, 1, 3, 2)
        self.assertTrue(r1 >= r2)

    def test_rect_comparison_4(self):
        r1 = Rect(0, 0, 1, 6)
        r2 = Rect(1, 1, 3, 2)
        self.assertFalse(r1 > r2)

    def test_rect_comparison_5(self):
        r1 = Rect(0, 0, 1, 6)
        r2 = Rect(1, 1, 3, 2)
        self.assertFalse(r1 < r2)

    def test_rect_comparison_6(self):
        r1 = Rect(0, 0, 1, 1)
        r2 = Rect(1, 1, 3, 1)
        self.assertTrue(r1 < r2)

    def test_rect_translate_1(self):
        r1 = Rect(0, 0, 1, 1)
        r2 = Rect(3, 4, 1, 1)
        r1.translate(3, 4)
        self.assertEqual((r1.x_cen, r1.y_cen), (r2.x_cen, r2.y_cen))

    def test_rect_translate_2(self):
        r1 = Rect(0, 0, 1, 1)
        r2 = Rect(-3, -2, 1, 1)
        r1.translate(-3, -2)
        self.assertEqual((r1.x_cen, r1.y_cen), (r2.x_cen, r2.y_cen))

    def test_rect_area_1(self):
        r1 = Rect(0, 0, 5, 4)
        self.assertEqual(r1.area, 20)

    def test_rect_area_2(self):
        r1 = Rect(0, 0, 0.1, 0.2)
        self.assertAlmostEqual(r1.area, 0.02)

    def test_rect_circ_1(self):
        r1 = Rect(0, 0, 1, 6)
        r2 = Rect(0, 0, 3, 4)
        self.assertEqual(r1.circ, r2.circ)

    def test_rect_circ_2(self):
        r1 = Rect(0, 0, 0.1, 0.2)
        r2 = Rect(0, 0, 0.25, 0.05)
        self.assertAlmostEqual(r1.circ, r2.circ)

    def test_rect_is_inside_1(self):
        r1 = Rect(0, 0, 1, 1)
        x1 = 0.4
        y1 = -0.3
        self.assertTrue(r1.is_inside(x1, y1))
        
    def test_rect_is_inside_2(self):
        r1 = Rect(0, 0, 1, 1)
        x1 = 0.5
        y1 = -0.5
        self.assertTrue(r1.is_inside(x1, y1))

    def test_rect_is_inside_3(self):
        r1 = Rect(0, 0, 1, 1)
        x1 = 0.5
        y1 = -0.6
        self.assertFalse(r1.is_inside(x1, y1))

    def test_rect_is_square_1(self):
        r1 = Rect(-12, 45.4, 4, 4)
        self.assertTrue(r1.is_square())

    def test_rect_is_square_2(self):
        r1 = Rect(-12, 45.4, 4, 5)
        self.assertFalse(r1.is_square())

    #---------tests of circle--------


    #-----------tests of cube

class TestCube(unittest.TestCase):
    def setUp(self):
        self.x_cen = 0
        self.y_cen = 0
        self.z_cen = 0
        self.side = 1

    def create_cube(self) -> Cube:
        return Cube(self.x_cen, self.y_cen, self.z_cen, self.side)

    def test_create_cube_1(self):
        c1 = self.create_cube()
        self.assertEqual((c1.x_cen, c1.y_cen, c1.z_cen, c1.side), (self.x_cen, self.y_cen, self.z_cen, self.side))

    def test_create_cube_2(self):
        with self.assertRaises(ValueError):
            c1 = Cube(1, 1, 1, -2)

    def test_create_cube_3(self):
        with self.assertRaises(ValueError):
            c1 = Cube(1, 1, 1, 0)

    def test_create_cube_3(self):
        with self.assertRaises(TypeError):
            c1 = Cube(1, 1, 1, "asdf")

    def test_cube_is_inside_1(self):
        c1 = Cube(0, 0, 0, 2)
        x1 = 1
        y1 = -1
        z1 = 0
        self.assertTrue(c1.is_inside(x1, y1, z1))

    def test_cube_is_inside_2(self):
        c1 = Cube(0, 0, 0, 2)
        x1 = 1
        y1 = -2
        z1 = 0
        self.assertFalse(c1.is_inside(x1, y1, z1))

    def test_cube_is_inside_3(self):
        with self.assertRaises(TypeError):
            c1 = Cube(0, 0, 0, 2)
            x1 = 1
            y1 = -2
            z1 = "hej"
            c1.is_inside(x1, y1, z1)
    

if __name__ == "__main__":
    unittest.main()




