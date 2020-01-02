from PageRank import PageRank
import numpy as np

# بهترین مقدار برای alpha=0.85
pagerank=PageRank(0.001,0.85)

adjacency_matrix=pagerank.input_array()

#تمرین سوال 1
adjacency_matrix = np.array([[0., 1., 0., 0., 0., 1.],
                           [0., 0., 1., 0., 0., 1.],
                           [0., 0., 0., 0., 1., 0.],
                           [0., 1., 0., 0., 1., 0.],
                           [0., 0., 0., 0., 0., 0.],
                           [0., 0., 1., 1., 0., 0.]])

adjacency_matrix_T=pagerank.Transpose_Matrix(adjacency_matrix)
print(adjacency_matrix_T)

Convert_to_markov=pagerank.Spars_Matrix(adjacency_matrix_T)
print(Convert_to_markov)

Sparse_matrix=pagerank.Spars_Matrix(Convert_to_markov)

print(Sparse_matrix)


v = np.zeros(adjacency_matrix_T.shape[0]).reshape(adjacency_matrix_T.shape[0], -1)
v_sparce=pagerank.Spars_Matrix(v)

e = np.ones(adjacency_matrix_T.shape[0]).reshape(adjacency_matrix_T.shape[0], -1)
n = adjacency_matrix_T.shape[0]

e_n = e / n

e_n_sparse=pagerank.Spars_Matrix(e_n)

print(pagerank.PageRank_Function(adjacency_matrix_T,v_sparce,e_n_sparse))





