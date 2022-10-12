from __future__ import annotations
import sys, os
import unittest

# we change directory to where this file is
os.chdir(os.path.dirname(__file__))
print(__file__)
# we define a path that is up one step
# in this pathwe have vecot.py and plotter.py and
# manual_testing.ipynb
path_to_geometry_module = os.path.abspath("../")

sys.path.append(path_to_geometry_module)
print("-" * 30)

from geometry import *

# ----tests of Rectangle--------


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.x_cen = 1
        self.y_cen = 1
        self.width = 10
        self.height = 10

    def create_rectangle(self) -> Rectangle:
        return Rectangle(self.x_cen, self.y_cen, self.width, self.height)

    def test_create_rectangle_0(self):
        r1 = self.create_rectangle()
        self.assertEqual(
            (r1.x_cen, r1.y_cen, r1.width, r1.height),
            (self.x_cen, self.y_cen, self.width, self.height),
        )

    def test_create_rectangle_1(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_create_rectangle_2(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -10, 20)

    def test_create_rectangle_3(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 10, -20)

    def test_create_rectangle_4(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 0, 2)

    def test_create_rectangle_5(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 10, "hej")

    def test_rect_comparison_1(self):
        r1 = Rectangle(0, 0, 1, 6)
        r2 = Rectangle(1, 1, 1, 6)
        self.assertTrue(r1 == r2)

    def test_rect_comparison_2(self):
        r1 = Rectangle(0, 0, 1, 6)
        r2 = Rectangle(1, 1, 3, 2)
        self.assertTrue(r1 <= r2)

    def test_rect_comparison_3(self):
        r1 = Rectangle(0, 0, 1, 6)
        r2 = Rectangle(1, 1, 3, 2)
        self.assertTrue(r1 >= r2)

    def test_rect_comparison_4(self):
        r1 = Rectangle(0, 0, 1, 6)
        r2 = Rectangle(1, 1, 3, 2)
        self.assertFalse(r1 > r2)

    def test_rect_comparison_5(self):
        r1 = Rectangle(0, 0, 1, 6)
        r2 = Rectangle(1, 1, 3, 2)
        self.assertFalse(r1 < r2)

    def test_rect_comparison_6(self):
        r1 = Rectangle(0, 0, 1, 1)
        r2 = Rectangle(1, 1, 3, 1)
        self.assertTrue(r1 < r2)

    def test_rect_translate_1(self):
        r1 = Rectangle(0, 0, 1, 1)
        r2 = Rectangle(3, 4, 1, 1)
        r1.translate(3, 4)
        self.assertEqual((r1.x_cen, r1.y_cen), (r2.x_cen, r2.y_cen))

    def test_rect_translate_2(self):
        r1 = Rectangle(0, 0, 1, 1)
        r2 = Rectangle(-3, -2, 1, 1)
        r1.translate(-3, -2)
        self.assertEqual((r1.x_cen, r1.y_cen), (r2.x_cen, r2.y_cen))

    def test_rect_area_1(self):
        r1 = Rectangle(0, 0, 5, 4)
        self.assertEqual(r1.area, 20)

    def test_rect_area_2(self):
        r1 = Rectangle(0, 0, 0.1, 0.2)
        self.assertAlmostEqual(r1.area, 0.02)

    def test_rect_circ_1(self):
        r1 = Rectangle(0, 0, 1, 6)
        r2 = Rectangle(0, 0, 3, 4)
        self.assertEqual(r1.circ, r2.circ)

    def test_rect_circ_2(self):
        r1 = Rectangle(0, 0, 0.1, 0.2)
        r2 = Rectangle(0, 0, 0.25, 0.05)
        self.assertAlmostEqual(r1.circ, r2.circ)

    def test_rect_is_inside_1(self):
        r1 = Rectangle(0, 0, 1, 1)
        x1 = 0.4
        y1 = -0.3
        self.assertTrue(r1.is_inside(x1, y1))

    def test_rect_is_inside_2(self):
        r1 = Rectangle(0, 0, 1, 1)
        x1 = 0.5
        y1 = -0.5
        self.assertTrue(r1.is_inside(x1, y1))

    def test_rect_is_inside_3(self):
        r1 = Rectangle(0, 0, 1, 1)
        x1 = 0.5
        y1 = -0.6
        self.assertFalse(r1.is_inside(x1, y1))

    def test_rect_is_square_1(self):
        r1 = Rectangle(-12, 45.4, 4, 4)
        self.assertTrue(r1.is_square())

    def test_rect_is_square_2(self):
        r1 = Rectangle(-12, 45.4, 4, 5)
        self.assertFalse(r1.is_square())

    # ---------tests of Circle--------


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.x_cen = 1
        self.y_cen = 1
        self.radius = 1

    def create_circle(self) -> Circle:
        return Circle(self.x_cen, self.y_cen, self.radius)

    def test_create_circle_0(self):
        c1 = self.create_circle()
        self.assertEqual(
            (c1.x_cen, c1.y_cen, c1.radius), (self.x_cen, self.y_cen, self.radius)
        )

    def test_create_circle_1(self):
        with self.assertRaises(TypeError):
            c1 = Circle()

    def test_create_circle_2(self):
        with self.assertRaises(ValueError):
            c1 = Circle(1, 1, -10)

    def test_create_circle_3(self):
        with self.assertRaises(ValueError):
            c1 = Circle(1, 1, 0)

    def test_create_circle_4(self):
        with self.assertRaises(TypeError):
            c1 = Circle(1, 1, "hej")

    def test_circle_comparison_1(self):
        c1 = Circle(0, 0, 1)
        c2 = Circle(1, 1, 1)
        self.assertTrue(c1 == c2)

    def test_circle_comparison_2(self):
        c1 = Circle(0, 0, 1)
        c2 = Circle(1, 1, 1)
        self.assertFalse(c1 > c2)

    def test_circle_comparison_3(self):
        c1 = Circle(0, 0, 1)
        c2 = Circle(1, 1, 1)
        self.assertFalse(c1 < c2)

    def test_circle_comparison_4(self):
        c1 = Circle(0, 0, 1)
        c2 = Circle(1, 1, 3)
        self.assertTrue(c1 < c2)

    def test_circle_translate_1(self):
        c1 = Circle(0, 0, 1)
        c2 = Circle(3, 4, 1)
        c1.translate(3, 4)
        self.assertEqual((c1.x_cen, c1.y_cen), (c2.x_cen, c2.y_cen))

    def test_circle_translate_2(self):
        c1 = Circle(0, 0, 1)
        c2 = Circle(-3, -2, 1)
        c1.translate(-3, -2)
        self.assertEqual((c1.x_cen, c1.y_cen), (c2.x_cen, c2.y_cen))

    def test_circle_is_inside_1(self):
        c1 = Circle(0, 0, 1)
        x1 = 0.4
        y1 = -0.3
        self.assertTrue(c1.is_inside(x1, y1))

    def test_circle_is_inside_2(self):
        c1 = Circle(0, 0, 1)
        x1 = 1
        y1 = 0
        self.assertTrue(c1.is_inside(x1, y1))

    def test_circle_is_inside_3(self):
        c1 = Circle(0, 0, 1)
        x1 = 0
        y1 = 1.1
        self.assertFalse(c1.is_inside(x1, y1))

    def test_circle_is_unit_circle_1(self):
        c1 = Circle(0, 0, 1)
        self.assertTrue(c1.is_unit_circle())

    def test_circle_is_unit_circle_2(self):
        c1 = Circle(0, 1, 1)
        self.assertFalse(c1.is_unit_circle())

    def test_circle_is_unit_circle_3(self):
        c1 = Circle(0, 0, 2)
        self.assertFalse(c1.is_unit_circle())

# -----------tests of Cube---------------


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
        self.assertEqual(
            (c1.x_cen, c1.y_cen, c1.z_cen, c1.side),
            (self.x_cen, self.y_cen, self.z_cen, self.side),
        )

    def test_create_cube_2(self):
        with self.assertRaises(ValueError):
            c1 = Cube(1, 1, 1, -2)

    def test_create_cube_3(self):
        with self.assertRaises(ValueError):
            c1 = Cube(1, 1, 1, 0)

    def test_create_cube_4(self):
        with self.assertRaises(TypeError):
            c1 = Cube(1, 1, 1, "asdf")

    def test_create_cube_5(self):
        with self.assertRaises(TypeError):
            c1 = Cube(1, 1, "hej", 1)

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

# -----------tests of Sphere---------------

class TestSphere(unittest.TestCase):
    def setUp(self):
        self.x_cen = 0
        self.y_cen = 0
        self.z_cen = 0
        self.radius = 1

    def create_sphere(self) -> Sphere:
        return Sphere(self.x_cen, self.y_cen, self.z_cen, self.radius)

    def test_create_sphere_1(self):
        s1 = self.create_sphere()
        self.assertEqual(
            (s1.x_cen, s1.y_cen, s1.z_cen, s1.radius),
            (self.x_cen, self.y_cen, self.z_cen, self.radius),
        )

    def test_create_sphere_2(self):
        with self.assertRaises(ValueError):
            s1 = Sphere(1, 1, 1, -2)

    def test_create_sphere_3(self):
        with self.assertRaises(ValueError):
            s1 = Sphere(1, 1, 1, 0)

    def test_create_sphere_4(self):
        with self.assertRaises(TypeError):
            s1 = Sphere(1, 1, 1, "asdf")

    def test_create_sphere_5(self):
        with self.assertRaises(TypeError):
            s1 = Sphere(1, 1, "hej", 1)

    def test_sphere_is_inside_1(self):
        s1 = Sphere(0, 0, 0, 2)
        x1 = 1
        y1 = -1
        z1 = 1
        self.assertTrue(s1.is_inside(x1, y1, z1))

    def test_sphere_is_inside_2(self):
        s1 = Sphere(0, 0, 0, 2)
        x1 = 1
        y1 = -2
        z1 = 0
        self.assertFalse(s1.is_inside(x1, y1, z1))

    def test_sphere_is_inside_3(self):
        s1 = Sphere(0, 0, 0, 2)
        with self.assertRaises(TypeError):
            x1 = 1
            y1 = -2
            z1 = "hej"
            s1.is_inside(x1, y1, z1)


if __name__ == "__main__":
    unittest.main()
