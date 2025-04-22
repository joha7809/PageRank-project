from opgave5 import make_web
from opgave24 import eigenvector_PageRank
import time

start_time = time.time()

web = make_web(5000,10,0)
eigenvector_PageRank(web)

end_time = time.time()

#printer køretid i sekunder
print(end_time-start_time)