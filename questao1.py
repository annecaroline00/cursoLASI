import numpy as np 


l = np.array([2, 6, 1, 9, 10, 3, 27, 45, 20, 8, 7, 2.8, 9.8])

result = np.where( (l>= 5) & (l < 10))

print(result)

