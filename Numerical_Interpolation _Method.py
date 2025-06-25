# Numerical Interpolation Method

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])
c = np.interp(2.5, a, b)
print("Interpolated value at 2.5:", c)