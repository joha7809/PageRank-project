from opgave5 import make_web
from opgave12 import random_surf_damp
from opgave15 import recursive_PageRank
from opgave24 import eigenvector_PageRank
from opgave35 import matrix_PageRank
import time

web = make_web(5000,100)
averages = [0]*4
times = [0]*4
d = 0.85

times[2] = time.time()
eigen = eigenvector_PageRank(web, d=d)
times[2] = time.time()-times[2]

"""
times[0] = time.time()
surf, it1 = random_surf_damp(web, 10000000, d=d, stop_value=1e-5)
times[0] = time.time()-times[0]
for page1,page2 in zip(eigen.values(),surf.values()):
    averages[0] += abs(page1-page2)
#"""

times[1] = time.time()
rec, it2 = recursive_PageRank(web, d=d, stop_value=1e-12, max_iterations=1000)
times[1] = time.time()-times[1]
for page1,page2 in zip(eigen.values(),rec.values()):
    averages[1] += abs(page1-page2)

times[3] = time.time()
power = matrix_PageRank(web, power=32, d=d)
times[3] = time.time()-times[3]
for page1,page2 in zip(eigen.values(),power.values()):
    averages[3] += abs(page1-page2)

for i in range(len(averages)):
    averages[i] /= len(eigen)

print(averages)
print(times)