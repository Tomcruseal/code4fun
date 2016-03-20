import numpy as np
from scipy.linalg import solve
H=np.array([[01010],[11110],[00111]])
b=np.array([[0],[0],[0]])
print solve(H,b)