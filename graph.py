class Graph:
    """
    Custom made graph class for deadlock detection.
    """

    def __init__(self, adjacency_matrix=[]):
        self.adjacency_matrix = adjacency_matrix
        self.size = len(self.adjacency_matrix)

    def add_node(self):
        """
        Adds a node with no initialized edges to the graph. Note that this is undesirable
        and simply figuring out how many nodes there are at the beginning is preferred.
        """
        self.size += 1
        for row in self.adjacency_matrix:
            row.append(0)
        self.adjacency_matrix.append([0 for _ in range(self.size)])

    def add_edge(self, n1, n2):
        """
        Add an edge between two nodes in the graph.

        There are no weights -- simply set the appropriate value in the
        adjacency matrix to a 1. Note that the graph is directed and so
        to simulate an undirected edge, it's necessary to add an edge from
        n1 to n2 and also from n2 to n1 separately.
        """
        self.adjacency_matrix[n1][n2] = 1