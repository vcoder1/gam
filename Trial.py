import numpy as np
import cmath
import matplotlib.pyplot as mp
try:
    for i in range(1, 5):
        x = np.linspace(-100, 100, 1001)
        y = np.linspace(i, i, 1001)
        x1 = x / (x ** 2 + y ** 2)
        y1 = -y / (x ** 2 + y ** 2)
        mp.plot(x, y, x1, y1)
        y = np.linspace(-100, 100, 1001)
        x = np.linspace(i, i, 1001)
        x1 = x / (x ** 2 + y ** 2)
        y1 = -y / (x ** 2 + y ** 2)
        mp.plot(x, y, x1, y1)
    mp.show()
except ZeroDivisionError:
    print("You can't divide by zero, you're silly.")

