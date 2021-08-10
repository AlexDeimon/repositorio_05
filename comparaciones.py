import sys
import numpy as np

s = range(1000)
print('Resultado de la lista con python: ')
print(sys.getsizeof(s)*len(s))
n = np.arange(1000)
print('Resultado de la lista con numpy: ')
print(n.size*n.itemsize)