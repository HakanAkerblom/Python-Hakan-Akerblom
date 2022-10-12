from __future__ import annotations
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from abc import abstractmethod, ABC

# --------------------------------------------------------------------
# Geometry Class 
# --------------------------------------------------------------------
class Geometry:
    """Parent class to Shape and Body. Two required paramters: x_cen and y_cen for position. Contains error handling for all childclasses"""
    def __init__(self, x_cen: float, y_cen: float) -> None:
        self.x_cen = x_cen
        self.y_cen = y_cen

    # ----- Abstract method -----
    @abstractmethod
    def translate(self):
        pass

    # ----- Properties -----
    @property
    def x_cen(self):
        return self._x_cen

    @property
    def y_cen(self):
        return self._y_cen

    @x_cen.setter
    def x_cen(self, value: float):
        self._x_cen = self.check_coordinate(value)

    @y_cen.setter
    def y_cen(self, value: float):
        self._y_cen = self.check_coordinate(value)

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
    """Parent class to Rectangle and Circle. Adds comparisons measuring area"""
    def __init__(self, x_cen: float, y_cen: float) -> None:
        super().__init__(x_cen, y_cen)

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
        self.x_cen += x
        self.y_cen += y

# --------------------------------------------------------------------
# Rectangle Class 
# --------------------------------------------------------------------
class Rectangle(Shape):
    """Class to create a rectangle. Adds Width and height giving size."""
    def __init__(self, x_cen: float, y_cen: float, width: float, height: float) -> None:
        super().__init__(x_cen, y_cen)
        self.width = width
        self.height = height
        """x_0 and x_1: min and max x-value, y_0 and y_1: min and max y-value."""
        self.x_0 = self._x_cen - self._width / 2
        self.x_1 = self._x_cen + self._width / 2
        self.y_0 = self._y_cen - self._height / 2
        self.y_1 = self._y_cen + self._height / 2

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
    def circ(self):
        return self.height * 2 + self.width * 2

    # ----- eq -----
    def __eq__(self, other: Rectangle):
        """Checks if two rectangles have the same measuements. Position is disregarded"""
        if self.width == other.width and self.height == other.height:
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

    def plot(self) -> patches.Patch:
        """Returns patch containing rectangle"""
        return patches.Rectangleangle((self.x_0, self.y_0), width = {self._width}, height = {self._height})

    

    def __repr__(self):
        return f"{self.width=}, {self.height=}, position: ({self.x_cen}, {self.y_cen})"

    def __str__(self):
        return f"{self.width=}, {self.height=}, position: ({self.x_cen}, {self.y_cen})"

# --------------------------------------------------------------------
# Circle Class 
# --------------------------------------------------------------------
class Circle(Shape):
    """Class to create a circle"""
    def __init__(self, x_cen: float, y_cen: float, radius: float) -> None:
        super().__init__(x_cen, y_cen)
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
    def circ(self):
        return math.pi * self.radius * 2

    # ----- eq -----
    def __eq__(self, other: Circle):
        """Checks if the radius of two circles are the same"""
        if self.radius == other.radius:
            return True
        else:
            return False

    # ----- Other methods -----
    def is_inside(self, x: float, y: float):
        """Checks if a point is inside or on the circle"""
        if math.sqrt((x - self.x_cen) ** 2 + (y - self.y_cen) ** 2) <= self.radius:
            return True
        else:
            return False

    def is_unit_circle(self):
        """Checks if circle has radius one and is centered in the origin"""
        if self.radius == 1 and self.x_cen == 0 and self.y_cen == 0:
            return True
        else:
            return False

    def plot(self) -> patches.Patch:
        """Returns patch containing circle"""
        return patches.Circle((self._x_cen, self._y_cen), self._radius)

# --------------------------------------------------------------------
# Body Class 
# --------------------------------------------------------------------
class Body(Geometry):
    """Superclass to Cube and Sphere, adds z_cen for position in the third dimensions. Adds comparisons measuring volume."""
    def __init__(self, x_cen: float, y_cen: float, z_cen: float) -> None:
        super().__init__(x_cen, y_cen)
        self.z_cen = z_cen

    # ----- Abstract method -----
    @abstractmethod
    def volume(self):
        pass

    # ----- Properties -----
    @property
    def x_cen(self):
        return self._x_cen

    @property
    def y_cen(self):
        return self._y_cen

    @property
    def z_cen(self):
        return self._z_cen

    @x_cen.setter
    def x_cen(self, value: float):
        self._x_cen = self.check_coordinate(value)

    @y_cen.setter
    def y_cen(self, value: float):
        self._y_cen = self.check_coordinate(value)

    @z_cen.setter
    def z_cen(self, value: float):
        self._z_cen = self.check_coordinate(value)

    # ----- Comparisons -----
    def __lt__(self, other: Body) -> bool:
        if self.volume < other.volume:
            return True
        else:
            return False

    def __le__(self, other: Body) -> bool:
        if self.volume <= other.volume:
            return True
        else:
            return False

    def __gt__(self, other: Body) -> bool:
        if self.volume > other.volume:
            return True
        else:
            return False

    def __ge__(self, other: Body) -> bool:
        if self.volume >= other.volume:
            return True
        else:
            return False

# --------------------------------------------------------------------
# Cube Class 
# --------------------------------------------------------------------
class Cube(Body):
    """Class to make a Cube. Adds side-measurment"""
    def __init__(self, x_cen: float, y_cen: float, z_cen: float, side: float) -> None:
        super().__init__(x_cen, y_cen, z_cen)
        self.side = side
        self.x_0 = self._x_cen - self._side / 2
        self.x_1 = self._x_cen + self._side / 2
        self.y_0 = self._y_cen - self._side / 2
        self.y_1 = self._y_cen + self._side / 2
        self.z_0 = self._z_cen - self._side / 2
        self.z_1 = self._z_cen + self._side / 2

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
    def __eq__(self, other: Cube):
        """Checks if two cubes have the same sidelength"""
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

# --------------------------------------------------------------------
# Sphere Class 
# --------------------------------------------------------------------
class Sphere(Body):
    """Class to create a Sphere. Adds radius-measurment"""
    def __init__(self, x_cen: float, y_cen: float, z_cen: float, radius: float) -> None:
        super().__init__(x_cen, y_cen, z_cen)
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
        if (
            self._radius == other._radius
            and self._x_cen == other._x_cen
            and self.y_cen == other._y_cen
        ):
            return True
        else:
            return False
    
    # ----- other method -----
    def is_inside(self, x: float, y: float, z: float) -> bool:
        """Checks if a point is inside or on the circle"""
        if math.sqrt((x - self.x_cen) ** 2 + (y - self.y_cen) ** 2 + (z - self.z_cen) ** 2) <= self.radius:
            return True
        else:
            return False

def plot(*args):
    pass



if __name__ == "__main__":
    pass




"""
TODO
- Fixa så att saker plottas i samma bild
- lägg till plot på translate och is_inside?

"""
