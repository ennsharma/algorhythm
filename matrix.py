def matrix_exponentiate(mat, n):
	"""
	Computes the matrix power A^n.
	"""
	if len(mat) != len(mat[0]):
		return "Matrix must be square to exponentiate."
	power_matrix = [[1 if i == j else 0 for j in range(len(mat))] for i in range(len(mat[0]))]
	for _ in range(n):
		power_matrix = matrix_multiply(power_matrix, mat)
	return power_matrix

def matrix_multiply(mat1, mat2):
    """
    Computes the result of multiplying two matrices, and returns the new matrix.
    """
    if len(mat1[0]) != len(mat2):
    	return "Matrix dimensions incompatible."

    product = [[0 for _ in range(len(mat1))] for _ in range(len(mat2[0]))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                product[i][j] += mat1[i][k]*mat2[k][j]
    return product

def find_eigenvalues(mat):
	"""
	Computes all eigenvalues of the input matrix.
	"""
	return None

def find_eigenvectors(mat):
	"""
	Computes all eigenvectors of the input matrix.
	"""
	return None


def row_reduce(mat):
	"""
	Row reduces the input matrix and outputs the result.
	"""
	return None


def compute_determinant(mat):
	"""
	Computes the determinant of the input matrix.
	"""
	if len(mat) != len(mat[0]):
		return "Only square matrices have defined determinants."
	if len(mat) == 1:
		return mat[0][0]
	if len(mat) == 2:
		return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

	temp_mat = [[mat[i][j] for j in range(1, len(mat[0]))] for i in range(len(mat))]
	determinant = 0
	for i in range(len(mat)):
		minor_matrix = deep_copy(temp_mat)
		minor_matrix.pop(i)
		determinant += mat[i][0]*compute_determinant(minor_matrix)*(-1)**i
	return determinant

def deep_copy(mat):
	"""
	Returns a deep copy of the input matrix.
	"""
	return [[mat[i][j] for j in range(len(mat[0]))] for i in range(len(mat))]

