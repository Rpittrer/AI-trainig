import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 16 * (np.pi), 0.1)
y1 = np.sin(x)
y2 = np.con(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")

plt.legend()
