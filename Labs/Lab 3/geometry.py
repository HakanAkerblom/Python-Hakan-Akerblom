from __future__ import annotations
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from abc import abstractmethod, ABC

# --------------------------------------------------------------------
# Geometry Class
# --------------------------------------------------------------------
class Geometry:
    """Abstract superclass to Shape and Body. Two required paramters: x and y for position. Contains error handling for all subclasses"""

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Init method for Geometry class. Two required parameters: x- and y-coordinate"""
        self.x = x
        self.y = y

    # ----- Abstract method -----
    @abstractmethod
    def translate(self):
        pass

    # ----- Properties -----
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value: float):
        self._x = self.check_coordinate(value)

    @y.setter
    def y(self, value: float):
        self._y = self.check_coordinate(value)

    # ----- Error handling ----- (structure inspired by Andreas)
    def check_coordinate(self, value: float):
        """Error handling for coordinates"""
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be a float or inte, not {type(value).__name__}")
        else:
            return value

    def check_measurement(self, value: float):
        """Error handling for measurements"""
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be int or float not {type(value).__name__}")
        elif value <= 0:
            raise ValueError("Must be positive")
        else:
            return value


# --------------------------------------------------------------------
# Shape Class
# --------------------------------------------------------------------
class Shape(Geometry):
    """Abstract superclass to Rectangle and Circle. Adds comparisons measuring area"""

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Init method for Shape class"""
        super().__init__(x, y)

    # ----- Abstract method -----
    @abstractmethod
    def area(self):
        pass

    # ----- Comparisons -----
    def __lt__(self, other: Shape) -> bool:
        """Compares area of two Shapes"""
        if self.area < other.area:
            return True
        else:
            return False

    def __le__(self, other: Shape) -> bool:
        """Compares area of two Shapes"""
        if self.area <= other.area:
            return True
        else:
            return False

    def __gt__(self, other: Shape) -> bool:
        """Compares area of two Shapes"""
        if self.area > other.area:
            return True
        else:
            return False

    def __ge__(self, other: Shape) -> bool:
        """Compares area of two Shapes"""
        if self.area >= other.area:
            return True
        else:
            return False

    # ----- translate -----
    def translate(self, x: float, y: float):
        """Moves a shape in positive x- and y-direction"""
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError("x and y must be int or float")
        self.x += x
        self.y += y
        if type(self).__name__ == "Rectangle":
            self.x_0 = self._x - self._width / 2
            self.x_1 = self._x + self._width / 2
            self.y_0 = self._y - self._height / 2
            self.y_1 = self._y + self._height / 2

    def plot_translation(
        self, x: float = 0, y: float = 0
    ) -> None:  # copied from https://github.com/Andreas-Svensson/Python-Andreas-Svensson/blob/main/Laborations/Geometry%20OOP/shapes.py
        """Translate shape and plot it visually"""
        patch_list = []  # storing return values (patches)

        patch_list.append(self.plot())  # create patch of self in previous position
        # styling previous position to low alpha and black dotted outlines:
        patch_list[0].set_alpha(0.3)
        patch_list[0].set_linestyle("--")
        patch_list[0].set_edgecolor("black")

        self.translate(x, y)  # perform actual translation

        patch_list.append(self.plot())  # create patch of self in current position

        return patch_list  # return list containing patches of self in old and new positions


# --------------------------------------------------------------------
# Rectangle Class
# --------------------------------------------------------------------
class Rectangle(Shape):
    """Class to create a rectangle. Adds Width and height giving size."""

    def __init__(
        self, x: float = 0, y: float = 0, width: float = 1, height: float = 1
    ) -> None:
        """Init method for Rectangle class. Adds two required paramters: width and height"""
        super().__init__(x, y)
        self.width = width
        self.height = height
        """x_0 and x_1: min and max x-value, y_0 and y_1: min and max y-value."""
        self.x_0 = self._x - self._width / 2
        self.x_1 = self._x + self._width / 2
        self.y_0 = self._y - self._height / 2
        self.y_1 = self._y + self._height / 2

    # ----- properties -----
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = self.check_measurement(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = self.check_measurement(value)

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return self.height * 2 + self.width * 2

    # ----- eq -----
    def __eq__(self, other: Rectangle) -> bool:
        """Checks if two rectangles have the same measuements. Position is disregarded"""
        if type(self).__name__ != type(other).__name__:
            return False
        elif self.width == other.width and self.height == other.height:
            return True
        else:
            return False

    # ----- other methods -----
    def is_inside(self, x: float, y: float) -> bool:
        """Checks if a point is inside or on the rectangle"""
        if self.x_0 <= x <= self.x_1 and self.y_0 <= y <= self.y_1:
            return True
        else:
            return False

    def is_square(self):
        """Checks if rectangle is a square"""
        if self.width == self.height:
            return True
        else:
            return False

    def plot(
        self,
    ) -> patches.Patch:  # copied from https://github.com/Andreas-Svensson/Python-Andreas-Svensson/blob/main/Laborations/Geometry%20OOP/shapes.py
        """Returns patch containing rectangle"""
        return patches.Rectangle((self.x_0, self.y_0), self._width, self._height)

    # ----- __str__ and __repr__ -----
    def __repr__(self):
        return f"Rectangle with {self.x=}, {self.y=}, {self.width=} and {self.height=}"

    def __str__(self):
        return f"Rectangle with width: {self.width}, height: {self.height}, position: ({self.x}, {self.y}), area: {self.area} and perimeter: {self.perimeter}."


# --------------------------------------------------------------------
# Circle Class
# --------------------------------------------------------------------
class Circle(Shape):
    """Class to create a circle"""

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1) -> None:
        """Init method for Circle class. Adds one required parameter: radius."""
        super().__init__(x, y)
        self.radius = radius

    # ----- Properties -----
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = self.check_measurement(value)

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def circumference(self):
        return math.pi * self.radius * 2

    # ----- eq -----
    def __eq__(self, other: Circle) -> bool:
        """Checks if the radius of two circles are the same"""
        if type(self).__name__ != type(other).__name__:
            return False
        if self.radius == other.radius:
            return True
        else:
            return False

    # ----- Other methods -----
    def is_inside(self, x: float, y: float):
        """Checks if a point is inside or on the circle"""
        if math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) <= self.radius:
            return True
        else:
            return False

    def is_unit_circle(self):
        """Checks if circle has radius one and is centered in the origin"""
        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True
        else:
            return False

    def plot(
        self,
    ) -> patches.Patch:  # copied from https://github.com/Andreas-Svensson/Python-Andreas-Svensson/blob/main/Laborations/Geometry%20OOP/shapes.py
        """Returns patch containing circle"""
        return patches.Circle((self._x, self._y), self._radius)

    # ----- __str__ and __repr__ -----
    def __repr__(self):
        return f"Circle with {self.x=}, {self.y=} and {self.radius=}"

    def __str__(self):
        return f"Circle with radius: {self.radius}, position: ({self.x}, {self.y}), area: {self.area} and circumference: {self.circumference}."


# --------------------------------------------------------------------
# Body Class
# --------------------------------------------------------------------
class Body(Geometry):
    """Abstract Superclass to Cube and Sphere, adds z for position in the third dimensions.
    Adds comparisons measuring volume."""

    def __init__(self, x: float, y: float, z: float) -> None:
        """Init method for Body class. Adds one required parameter: z-coordinate."""
        super().__init__(x, y)
        self.z = z

    # ----- Abstract method -----
    @abstractmethod
    def volume(self):
        pass

    # ----- Properties -----
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, value: float):
        self._x = self.check_coordinate(value)

    @y.setter
    def y(self, value: float):
        self._y = self.check_coordinate(value)

    @z.setter
    def z(self, value: float):
        self._z = self.check_coordinate(value)

    # ----- Comparisons -----
    def __lt__(self, other: Body) -> bool:
        """Compares volumes of two bodies"""
        if self.volume < other.volume:
            return True
        else:
            return False

    def __le__(self, other: Body) -> bool:
        """Compares volumes of two bodies"""
        if self.volume <= other.volume:
            return True
        else:
            return False

    def __gt__(self, other: Body) -> bool:
        """Compares volumes of two bodies"""
        if self.volume > other.volume:
            return True
        else:
            return False

    def __ge__(self, other: Body) -> bool:
        """Compares volumes of two bodies"""
        if self.volume >= other.volume:
            return True
        else:
            return False

    def translate(self, x: float, y: float, z: float):
        """Moves a Body in space"""
        if (
            not isinstance(x, (float, int))
            or not isinstance(y, (float, int))
            or not isinstance(z, (float, int))
        ):
            raise TypeError("x and y must be int or float")
        self._x += x
        self._y += y
        self._z += z


# --------------------------------------------------------------------
# Cube Class
# --------------------------------------------------------------------
class Cube(Body):
    """Class to make a Cube. Adds side-measurment"""

    def __init__(
        self, x: float = 0, y: float = 0, z: float = 0, side: float = 1
    ) -> None:
        """Init method for Cube class. Adds one required parameter: side."""
        super().__init__(x, y, z)
        self.side = side
        self.x_0 = self._x - self._side / 2
        self.x_1 = self._x + self._side / 2
        self.y_0 = self._y - self._side / 2
        self.y_1 = self._y + self._side / 2
        self.z_0 = self._z - self._side / 2
        self.z_1 = self._z + self._side / 2

    # ----- Properties -----
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = self.check_measurement(value)

    @property
    def surface_area(self):
        return 6 * (self._side**2)

    @property
    def volume(self):
        return self._side**3

    # ----- eq -----
    def __eq__(self, other: Cube) -> bool:
        """Checks if two cubes have the same sidelength"""
        if type(self).__name__ != type(other).__name__:
            return False
        if self._side == other._side:
            return True
        else:
            return False

    # ----- Other method -----
    def is_inside(self, x: float, y: float, z: float) -> bool:
        """Checks if a point is inside or on the cube"""
        if (
            not isinstance(x, (float, int))
            or not isinstance(y, (float, int))
            or not isinstance(z, (float, int))
        ):
            raise TypeError("x, y and z must be floats or ints")
        elif (
            self.x_0 <= x <= self.x_1
            and self.y_0 <= y <= self.y_1
            and self.z_0 <= z <= self.z_1
        ):
            return True
        else:
            return False

    # ----- __str__ and __repr__ -----
    def __repr__(self):
        return f"Cube with {self.x=}, {self.y=}, {self.z=} and {self.side=}"

    def __str__(self):
        return f"Cube with side: {self.side}, position: ({self.x}, {self.y}, {self.z}), surface area: {self.surface_area} and volume {self.volume}."


# --------------------------------------------------------------------
# Sphere Class
# --------------------------------------------------------------------
class Sphere(Body):
    """Class to create a Sphere. Adds radius-measurement"""

    def __init__(
        self, x: float = 0, y: float = 0, z: float = 0, radius: float = 1
    ) -> None:
        """Init method for Sphere class. Adds one required parameter: radius."""
        super().__init__(x, y, z)
        self.radius = radius

    # ----- Properties -----
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = self.check_measurement(value)

    @property
    def surface_area(self):
        return 4 * math.pi * self._radius**2

    @property
    def volume(self):
        return (4 / 3) * math.pi * self._radius**3

    # ----- eq -----
    def __eq__(self, other: Sphere) -> bool:
        """Checks if two spheres has the same radius"""
        if type(self).__name__ != type(other).__name__:
            return False
        if self._radius == other._radius:
            return True
        else:
            return False

    # ----- other method -----
    def is_inside(self, x: float, y: float, z: float) -> bool:
        """Checks if a point is inside or on the circle"""
        if (
            math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2)
            <= self.radius
        ):
            return True
        else:
            return False

    # ----- __str__ and __repr__ -----
    def __repr__(self):
        return f"Sphere with {self.x=}, {self.y=}, {self.z=} and {self.radius=}"

    def __str__(self):
        return f"Sphere with radius: {self.radius}, position: ({self.x}, {self.y}, {self.z}), surface area: {self.surface_area} and volume {self.volume}."


if __name__ == "__main__":
    r1 = Rectangle(1, 2, 3, 4)
    print(r1)
    print(r1.__repr__)

    for class_type in Circle, Rectangle, Sphere, Cube:
        for name, value in class_type.__dict__.items():
            if value.__doc__ == None:
                print(
                    f"{class_type,__name__} class, {name} method is missing a docstring"
                )


"""
TODO
- lägg till plot på translate och is_inside?

"""
