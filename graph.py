from matplotlib import pyplot as plt
import numpy as np

# Example Source: https://pythontic.com/visualization/charts/sinewave
x = np.arange(0, 10, 1)
y = np.sin(x)

plt.plot(x, y)

plt.xticks(np.arange(0, 10, 4))

plt.show()
