""" 
Name: Dylan Dang
"""
class Matrix:
	
	# input: mat (a 2d list)
	# Example: Matrix([[1, 2, 3], [2, 4, 6]]) makes a matrix like...
	# [1 2 3 ]
	# [2 3 6 ]
	def __init__(self, mat):
		# ALREADY DONE FOR YOU! DO NOT TOUCH
		self.m = mat 				# the matrix
		self.rows = len(mat)		# number of rows
		self.cols = len(mat[0])		# number of columns

	# get's the element of the matrix in row i, column j
	def get_element(self, i, j):
		# ALREADY DONE FOR YOU! DO NOT TOUCH
		return self.m[i][j]

	# Part3
	# TODO: implement matrix addition
	# inputs: self, other
	# output: if matrix addition is possible, return the sum Matrix
	#		  DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
	# 		  if matrix addition is not possible, return None
	def __add__(self, other):
		if (self.rows == other.rows) and (self.cols == other.cols) :
			sum = []
			for i in range(self.rows):
				temp = []
				for j in range(self.cols):
					temp.append(self.get_element(i, j) + other.get_element(i, j))
				sum.append(temp)
			return Matrix(sum)
		else :
			return None

	# Part4
	# TODO: implement matrix subtraction
	# inputs: self, other
	# output: if matrix subtraction is possible, return the difference Matrix
	#		  DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
	# 		  if matrix subtraction is not possible, return None
	def __sub__(self, other):
		if (self.rows == other.rows) and (self.cols == other.cols) :
			difference = []
			for i in range(self.rows):
				temp = []
				for j in range(self.cols):
					temp.append(self.get_element(i, j) - other.get_element(i, j))
				difference.append(temp)
			return Matrix(difference)
		else :
			return None

	# Part5
	# TODO: implement dot product
	# inputs: self, other
	# output: if matrix multiplication is possible, return the product Matrix
	#		  DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
	# 		  if matrix multiplication is not possible, return None
	def __mul__(self, other):
		if (self.cols == other.rows) :
			product = [[0 for j in range(other.cols)] for i in range(self.rows)]
			for i in range(self.rows) :
				for j in range(other.cols):
					for k in range(other.rows) :
						product[i][j] += self.get_element(i, k) * other.get_element(k, j)
			return Matrix(product)
		else :
			return None

	# DO NOT TOUCH! For debugging purposes
	def __str__(self):
		string = ""
		for r in self.m:
			string += "["
			for c in r:
				string += str(c) + " "
			string += "]\n"
		return string
