from opgave10 import random_surf
from opgave4 import W1, W2

for n in range(1000, 1010, 1):
    print(random_surf(W1, n))
print()
for n in range(1000, 1010, 1):
    print(random_surf(W2, n))
