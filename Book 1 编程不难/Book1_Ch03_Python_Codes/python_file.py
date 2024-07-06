# Write the contents of the cell to a file
# %%writefile

import numpy as np

A = np.random.uniform(0, 1, (1000, 1000))
B = np.random.uniform(0, 1, (1000, 1000))
C = A @ B

print(C)
