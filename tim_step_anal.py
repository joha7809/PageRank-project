from opgave5 import make_web
from opgave24 import eigenvector_PageRank
import time
import json

times = {}

for n in range(4000, 10000, 1000):
    web = make_web(n, k=10)
    print("web made")
    # Time the eigenvector_PageRank function
    start_time = time.time()
    x = eigenvector_PageRank(web)
    end_time = time.time()
    print(f"done {n}")

    # Append to times as n: time
    times[n] = end_time - start_time

# Save the times dictionary to a JSON file
with open("times.json", "w") as f:
    json.dump(times, f)

print("Times saved to times.json")
