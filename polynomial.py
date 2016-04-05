import matrix

def lagrange_interpolate(points, n):
	"""
	Computes a degree n polynomial given a list of two-element tuple points as input.
	If a degree n polynomial cannot be uniquely determined with the points given, returns None.
	Also returns None if no such polynomial exists that can pass through all input points.

	NOTE: This process has not yet been optimized using the Fast Fourier Transform.
	"""
	if len(points) < n+1 or degree:
		return None

	points = points[:n+1]
	vandermonde = [[points[0]**j for j in range(len(points))] for i in range(len(points))]
	y_vector = [[point[1]] for point in points]
	return matrix_multiply(inverse(vandermonde), y_vector)
