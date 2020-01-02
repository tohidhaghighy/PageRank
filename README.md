# PageRank
- Pagerank simple

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


