from opgave4 import W1,W2
from opgave5 import make_web
from opgave24 import eigenvector_PageRank
from opgave35 import matrix_PageRank

W3 = make_web(100, 99)

p1 = eigenvector_PageRank(W1)
p2 = matrix_PageRank(W1, 100)
p3 = eigenvector_PageRank(W2)
p4 = matrix_PageRank(W2, 100)
p5 = eigenvector_PageRank(W3)
p6 = matrix_PageRank(W3, 100)

for page1,page2 in zip(p5.values(),p6.values()):
    print((page2-page1)/page1)

print()

for page1,page2 in zip(p1.values(),p2.values()):
    print((page2-page1)/page1)

print()

for page1,page2 in zip(p3.values(),p4.values()):
    print((page2-page1)/page1)