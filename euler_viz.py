import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1*np.pi, 10000) 

x = np.cos(t)
y = np.sin(t)

plt.plot(x, y)
plt.axhline(0, color='green')
plt.axvline(0, color='green')
plt.grid(True)
plt.axis('equal')
plt.title("jondermoharris's = euler's ?")
plt.show()