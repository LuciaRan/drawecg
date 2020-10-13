#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

fs=100

name = "100_chan0_rate360_base1024.dat"
y = np.fromfile(name, dtype=np.int32)
y=y[:2000]

plt.figure(1)
plt.plot(y)

plt.show()