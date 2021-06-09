import numpy as np
a = np.array([1, 2, 3, 4], dtype=np.int16)
print(type(a[0]))
print(a)
a = a * 0.5
a = np.array(a, dtype=np.int16)
print(type(a[0]))
print(a)