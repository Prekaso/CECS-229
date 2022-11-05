import numpy as np

# function name: per_to_dec
# inputs: mat - n x n numpy array with percentages
# output: n x n numpy array where percentages are converted to decimal numbers
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def per_to_dec(mat):
	mat = mat / 100									# converting percentage to decimal 
	return mat


# function name: sig_change
# inputs: oldmat - n x n numpy array (decimal form)
		# newmat - n x n numpy array (decimal form)
# output: True if there is at least one element in newmat that is at least 0.0001 away
			# from its respective counterpart in oldmat
		# False otherwise
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def sig_change(oldmat, newmat) :
	row, column = oldmat.shape						# get row and column of oldmat

	for r in range(row) :
		for c in range(column) :
			change = oldmat[r, c] - newmat[r, c]  	# subtract oldmat from newmat to find significant change
			
			if abs(change) >= 0.0001 : 				# output TRUE if "at least" 0.0001 away 
				return True
	return False									


# function name: prob_x
# inputs: mat - n x n numpy array with PERCENTAGES
		# x - number of iterations
# output: n x n numpy array that represents the probability matrix after x stages
		# Use per_to_dec here
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
			#  x will always be >= 1
def prob_x(mat, x):
	mat_dec = per_to_dec(mat)						# convert matrix percentage to matrix decimal
	trans_prob = mat_dec							# save initial mat_dec value to trans_prob

	for i in range(x - 1) :							
		trans_prob = trans_prob.dot(mat_dec) 		# return transitional probability matrix after x stages
	return trans_prob


# function name: long_run_dist
# inputs: mat - n x n numpy array with PERCENTAGES
# output: n x n numpy array where percentages are converted to decimals
		# USE sig_change and per_to_dec
# assumptions: The test case shows a 3x3 matrix, but other test cases can have
			#  more or less rows/columns (always square matrix though)
def long_run_dist(probs):
	probs = per_to_dec(probs)						# convert matrix percentage to matrix decimal
	newmat = probs

	while True :
		oldmat = newmat   							# save initial/previous matrix to oldmat before doing dot product with newmat
		newmat = newmat.dot(probs)					
		
		if not(sig_change(oldmat, newmat)) :		# if there is no significant change "< 0.0001", return matrix
			return newmat							# returns long-run-distribution
