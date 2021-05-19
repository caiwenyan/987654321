import matplotlib.pyplot as plt
import numpy as np 
from scipy import signal

t = np.linspace(0, 5, 100)
x = np.sin(t)

x_resampled = signal.resample(x, 25)

plt.plot(t, x)
plt.plot(t[::4], x_resampled, 'ko')
plt.show()
