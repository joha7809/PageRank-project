from opgave4 import W1, W2


def rank_update(web, PageRanks, page, d) -> tuple[float, dict[str, float]]:
    """
    Opdaterer værdien af PageRank for en side baseret på den rekursive formel
    Sider uden udgående links (sinks) behandles som om de linker til alle sider på nettet.

    Input: 
        web og PageRanks er dictionaries som i outputtet fra "make_web" og "random_surf",
        page er nøglen til den side, hvis rank vi ønsker at opdatere, og
        d er dampingfaktoren.
    Output: 
        PageRank opdateres i henhold til ovenstående formel,
        og denne funktion returnerer et float "increment", den (absolutte) forskel
        mellem den tidligere værdi og den opdaterede værdi af PR(p).
    """
    N = len(web) #Amount of websits (nodes)
    oldValue = PageRanks[page] #old pageranking value of given page, used to determine difference.
    newValue = (1-d)/N #Initialize the new values, they all start equal

    #Check every page in web
    for p in web.keys():
        out_links = web[p] #outbound links of current page in for loop.
        if page in out_links: #The current page links to target page
            newValue += d * PageRanks[p]/(len(out_links))
        
        if not out_links: #The current page is a sink, and should therefore contribute evenly to all pages
            newValue += d*PageRanks[p] / (N)
    
    return newValue-oldValue

def recursive_PageRank(web, stopvalue=0.0001, max_iterations=200, d=0.85):
    """
    Implementerer den rekursive version af PageRank-algoritmen ved først at oprette
    en PageRank på 1/N til alle sider (hvor N er det samlede antal sider)
    og derefter anvende "rank_update" gentagne gange, indtil en af de to stopbetingelser
    er opnået:
    stopbetingelse 1: den maksimale ændring fra trin n til trin (n+1) over alle PageRank
    er mindre end stopværdien,
    Stopbetingelse 2: antallet af iterationer har nået "max_iterations".

    Input: web er et dictionary som i outputtet af "make_web", d er dæmpningen,
    stopvalue er et positivt float, max_iterations er et positivt heltal.
    """

    page_ranks = {k: 1/len(web.keys()) for k in web.keys()} 
    
    for i in range(max_iterations):
        increments = [rank_update(web, page_ranks, page, d) for page in web.keys()]
        for page, inc in zip(page_ranks, increments):
            page_ranks[page] += inc

        if max(map(abs, increments)) < stopvalue: break

    return page_ranks, i

#rank_update(W1, 0, "p1", 0)
rankings, it = recursive_PageRank(W1, d=0.85, max_iterations=200, stopvalue=0.0001)
print(sum(rankings.values()))
print(it)
print(rankings)