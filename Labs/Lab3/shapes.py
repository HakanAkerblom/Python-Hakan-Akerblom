from __future__ import annotations
import matplotlib.pyplot as plt
import math

class Shape:
    def __init__(self, x_cen: float, y_cen: float) -> None:
        self.x_cen = x_cen
        self.y_cen = y_cen

    @property
    def x_cen(self):
        return self._x_cen

    @property
    def y_cen(self):
        return self._y_cen

    @x_cen.setter
    def x_cen(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be a float or inte, not {type(value)}")
        self._x_cen = value

    @y_cen.setter
    def y_cen(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be a float or inte, not {type(value)}")
        self._y_cen = value

    def __lt__(self, other: Shape) -> bool:
        if self.area < other.area:
            return True
        else:
            return False

    def __le__(self, other: Shape) -> bool:
        if self.area <= other.area:
            return True
        else:
            return False

    def __gt__(self, other: Shape) -> bool:
        if self.area > other.area:
            return True
        else:
            return False

    def __ge__(self, other: Shape) -> bool:
        if self.area >= other.area:
            return True
        else:
            return False

    def translate(self, x: float, y: float):
        if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
            raise TypeError("Must be an int or float")
        self.x_cen += x
        self.y_cen += y


class Rect(Shape):
    def __init__(self, x_cen: float, y_cen: float, width: float, height: float) -> None:
        super().__init__(x_cen, y_cen)
        self.width = width
        self.height = height
        self.x_0 = self.x_cen - self.width/2
        self.x_1 = self.x_cen + self.width/2
        self.y_0 = self.y_cen - self.height/2
        self.y_1 = self.y_cen + self.height/2

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Must be int or float")
        if value <= 0:
            raise ValueError("Must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Must be int or float")
        if value <= 0:
            raise ValueError("Must be positive")
        self._height = value

    @property
    def area(self):
        return self.height*self.width
    
    @property
    def circ(self):
        return self.height*2+self.width*2

    def __eq__(self, other: Rect):
        """Checks if two rectangles have the same measuements. Position is disregarded"""
        if self.width == other.width and self.height == other.height:
            return True
        else:
            return False
    
    def is_inside(self, x: float, y: float) -> bool:
        if self.x_0 <= x <= self.x_1 and self.y_0 <= y <= self.y_1:
            return True
        else:
            return False
    
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

    def plot(self):
        xs =[
            self.x_0,
            self.x_1,
            self.x_1,
            self.x_0,
            self.x_0,
        ]
        ys = [
            self.y_0,
            self.y_0,
            self.y_1,
            self.y_1,
            self.y_0,
        ]
        fig, ax = plt.subplots()
        ax.grid(True)
        ax.plot(xs, ys, color="red")
        ax.set(xlabel = "x", ylabel = "y")
        plt.show()

        
    def __repr__(self):
        return f"{self.width=}, {self.height=}, position: ({self.x_cen}, {self.y_cen})"

    def __str__(self):
        return f"{self.width=}, {self.height=}, position: ({self.x_cen}, {self.y_cen})"

 
class Circle(Shape):
    def __init__(self, x_cen: float, y_cen: float, radius: float) -> None:
        super().__init__(x_cen, y_cen)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Must be int or float")
        self._radius = value

    @property
    def area(self):
        return math.pi*self.radius**2

    @property
    def circ(self):
        return math.pi*self.radius*2

    def __eq__(self, other: Circle):
        if self.radius == other.radius:
            return True
        else:
            return False

    def is_inside(self, x: float, y: float):
        if math.sqrt((x-self.x_cen)**2 + (y-self.y_cen)**2) <= self.radius:
            return True
        else:
            return False

    def is_unit_circle(self):
        if self.radius == 1 and self.x_cen == 0 and self.y_cen == 0:
            return True
        else:
            return False

    def plot(self, color = "r"):
        fig, ax = plt.subplots()
        circle1 = plt.Circle((self.x_cen, self.y_cen), self.radius, color = color, alpha = 0.5)
        ax.add_patch(circle1)
        ax.autoscale()
        ax.set_aspect(1)
        plt.show()

class Body:
    def __init__(self, x_cen: float, y_cen: float, z_cen: float) -> None:
        self.x_cen = x_cen
        self.y_cen = y_cen
        self.z_cen = z_cen

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
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be a float or inte, not {type(value)}")
        self._x_cen = value

    @y_cen.setter
    def y_cen(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be a float or inte, not {type(value)}")
        self._y_cen = value

    @z_cen.setter
    def z_cen(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError(f"Must be a float or inte, not {type(value)}")
        self._z_cen = value

    def __lt__(self, other: Body) -> bool:
        if self.volume < other.volue:
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

class Cube(Body):
    def __init__(self, x_cen: float, y_cen: float, z_cen: float, side: float) -> None:
        super().__init__(x_cen, y_cen, z_cen)
        self.side = side

        @property
        def side(self):
            return self._side

        @side.setter
        def side(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("Must be int or float")
            elif value <= 0:
                raise ValueError("Must be positive")
            else:
                self._side = value


        









if __name__ == "__main__":
    a = Rect(1, 1, 10, 10)
    a.plot()
    b = Circle(0, 1, 1)
    b.plot()
    c = Circle(1, 2, 1)
    c.plot("b")

"""
TODO
- Fixa så att saker plottas i samma bild
- Gör Kubklass
- Gör sphereklass

"""