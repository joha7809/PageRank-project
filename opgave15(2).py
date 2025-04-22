from opgave4 import W1
def rank_update(web, PageRanks, page, d):
    N = len(web)
    q = []

    for p in web.keys():
        if p != page and page in web[p]:
            q.append(p)
    
    prevRanks = PageRanks.copy()
    PageRanks[page] = (1-d) * (1/N) + d*sum([prevRanks[p] / len(web[p]) for p in q])

    return prevRanks[page] - PageRanks[page]


def recursive_PageRank(web, stopvalue=0.0001, max_iterations=200, d=0.85):
    PageRanks = dict()
    for page in web.keys():
        PageRanks[page] = 1/len(web)
    
    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        increment = 0

        for page in web.keys():
            increment += abs(rank_update(web, PageRanks, page, d))
    return PageRanks, iteration


rank, it = recursive_PageRank(W1)
print(recursive_PageRank(W1))

print(sum(rank.values()))