# Exercice course Numerical Modeling
# teacher: Dr. Paulo Kubota
# student: Arthur Duarte
# Date: 2025-06-25

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])
c = np.interp(2.5, a, b)
print("Interpolated value at 2.5:", c)