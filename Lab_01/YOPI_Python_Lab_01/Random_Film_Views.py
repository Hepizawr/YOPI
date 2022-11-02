import numpy as np

A = np.random.randint(1, 100, size=10)

f = open('10_films.txt', 'w')

for i in A:
    f.write(str(i) + '\n')

f.close()

