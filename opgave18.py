from opgave17 import modified_link_matrix, W1, W2
import numpy as np

w1_A = modified_link_matrix(W1, list(W1.keys()))
w2_A = modified_link_matrix(W2, list(W2.keys()))

#Tager summen af søjlerne
print(np.sum(w1_A, axis=0))
print(np.sum(w2_A, axis=0))

