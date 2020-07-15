import numpy as np
from src.timer import Timer

n = 10000
a = np.ones(n)
b = np.ones(n)

c = np.zeros(n)

timer = Timer()
for i in np.arange(n):
    c[i] = a[i] + b[i]

print(f'{timer.stop():.5f} sec')

timer.start()
d = a + b
print(f'{timer.stop():.5f} sec')