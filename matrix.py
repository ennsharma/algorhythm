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
	

def scale_row(mat, scale_factor, i):
	"""
	Multiplies every element in the given row by the input scale factor.
	"""
	for j in range(len(mat[i])):
		mat[i][j] *= scale_factor

def scale_row_copy(mat, scale_factor, i):
	"""
	Scales every element in a copy of the given row by the input scale factor and returns it.
	"""
	row = list(mat[i])
	for j in range(len(row)):
		row[j] *= scale_factor
	return row

def scale_column(mat, scale_factor, j):
	"""
	Multiplies every element in the given column by the input scale factor.
	"""
	for i in range(len(mat)):
		mat[i][j] *= scale_factor

def scale_column_copy(mat, scale_factor, j):
	"""
	Scales every element in a copy of the given row by the input scale factor and returns it.
	"""
	column = [mat[i][j] for i in range(len(mat))]
	for i in range(len(column)):
		column[i] *= scale_factor
	return column

def trace(mat):
	"""
	Returns the trace of the input matrix if the matrix is square. Returns
	None otherwise.
	"""
	if len(mat) != len(mat[0]):
		return None
	return sum([mat[i][i] for i in range(len(mat))])

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

