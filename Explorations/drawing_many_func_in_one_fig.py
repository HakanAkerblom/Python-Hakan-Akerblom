import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class Sine:
    x: np.array

    def plot(self, ax):
        ax.plot(np.sin(self.x))

@dataclass
class Line:
    x: np.array
    slope: int = 1
    intercept: int = 0

    def plot(self, ax):
        ax.plot(self.slope*self.x + self.intercept)

ax = plt.axes()
my_sine = Sine(np.linspace(-3,3))
my_line = Line(np.linspace(-3,3))
neg_line = Line(np.linspace(-3,3), slope = -1)

for func in (my_line, my_sine, neg_line):
    func.plot(ax)

ax.set(title = "Drawing many functions in same surface");
plt.show()