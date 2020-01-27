# PageRank

PageRank is a link analysis algorithm and it assigns a numerical weighting to each element of a hyperlinked set of documents, such as the World Wide Web, with the purpose of "measuring" its relative importance within the set. The algorithm may be applied to any collection of entities with reciprocal quotations and references. The numerical weight that it assigns to any given element E is referred to as the PageRank of E and denoted by P R ( E ).

A PageRank results from a mathematical algorithm based on the webgraph, created by all World Wide Web pages as nodes and hyperlinks as edges, taking into consideration authority hubs such as cnn.com or usa.gov. The rank value indicates an importance of a particular page. A hyperlink to a page counts as a vote of support. The PageRank of a page is defined recursively and depends on the number and PageRank metric of all pages that link to it ("incoming links"). A page that is linked to by many pages with high PageRank receives a high rank itself.

Numerous academic papers concerning PageRank have been published since Page and Brin's original paper. In practice, the PageRank concept may be vulnerable to manipulation. Research has been conducted into identifying falsely influenced PageRank rankings. The goal is to find an effective means of ignoring links from documents with falsely influenced PageRank

- simple Pagerank 

PageRank is a function that assigns a real number to each page in the Web
(or at least to that portion of the Web that has been crawled and its links
discovered). The intent is that the higher the PageRank of a page, the more
“important” it is. There is not one fixed algorithm for assignment of PageRank,
and in fact variations on the basic idea can alter the relative PageRank of any
two pages

the way to solve the equation v = Mv is by Gaussian elimination

- pagerank with taxation

we modify the calculation
of PageRank by allowing each random surfer a small probability of teleporting
to a random page, rather than following an out-link from their current page.
The iterative step, where we compute a new vector estimate of PageRanks v′
from the current PageRank estimate v and the transition matrix M is
v′ = βMv + (1 − β)e/n
where β is a chosen constant, usually in the range 0.8 to 0.9, e is a vector of all
1’s with the appropriate number of components, and n is the number of nodes
in the Web graph. The term βMv represents the case where, with probability
β, the random surfer decides to follow an out-link from their present page. The
term (1 − β)e/n is a vector each of whose components has value (1 − β)/n and
represents the introduction, with probability 1 − β, of a new random surfer at
a random page.


![page rank](https://image.slidesharecdn.com/socialnetworkanalysiswithpython-141121195454-conversion-gate02/95/graph-analyses-with-python-and-networkx-38-638.jpg?cb=1457750692)
