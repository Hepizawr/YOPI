import numpy as np

A = np.random.randint(10, 100, size=100)

f = open('Lab_mas.txt', 'w')

for i in A:
    f.write(str(i) + '\n')

f.close()

