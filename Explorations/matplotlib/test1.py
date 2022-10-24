import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random

values = [0] * 50

for i in range(50):
    values[i] = random.randint(0, 100)
    plt.xlim(0, 50)
    plt.ylim(0, 100)
    plt.bar(list(range(50)), values)
    plt.pause(0.0001)

plt.show()
