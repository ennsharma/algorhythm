import graph

def matrix_multiply(mat1, mat2):
    """
    Computes the result of multiplying two matrices, and returns the new matrix.
    """
    product = [[0 for _ in range(len(mat1))] for _ in range(len(mat2[0]))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                product[i][j] += mat1[i][k]*mat2[k][j]
    return product

def has_cycle(graph):
    """
    Determines whether the input graph represented as an adjacency_matrix
    possesses any cycles.

    The method used below is k-paths matrix exponentiation -- if A is the
    adjacency matrix for a graph with entry (i,j) = 1 denoting a directed
    edge from node i to node j, then entry (i,j) in A^k denotes the number
    of length k paths from i to j in the graph.

    If for every matrix power A^k for 1 <= k <= n, each and every diagonal
    entry in A^k is 0, then there are no paths of length 1 <= k <= n that 
    start and end at the same node (hence, no cycles). 

    A cycle that doesn't use repeated edges can have a maximum length of n 
    assuming there are no multi edges in our graph; hence our check is sufficient.
    """
    power_matrix = [[1 if i == j else 0 for j in range(graph.size)] for i in range(graph.size)]
    for exp in range(graph.size):
        power_matrix = matrix_multiply(power_matrix, graph.adjacency_matrix)
        for i in range(graph.size):
            if power_matrix[i][i] != 0:
                return "Cycle exists, and node " + str(i) + " is in the cycle."
    return "No cycles."

if __name__ == "__main__":
    adj1 = [[0,1,1,1],
            [0,0,1,1],
            [0,0,0,1],
            [0,0,0,0]]
    adj2 = [[0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
            [0,1,0,0]]
    adj3 = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
    g1, g2, g3 = graph.Graph(adj1), graph.Graph(adj2), graph.Graph(adj3)
    print(has_cycle(g1))
    print(has_cycle(g2))
    print(has_cycle(g3))
