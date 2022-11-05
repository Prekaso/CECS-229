import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# function name: least_sq
# inputs: file_name- name of the csv file 
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):
    data = pd.read_csv(file_name) # read data from given csv file
    
    x = np.array(data.x)
    y = np.array(data.y)
    data_length = len(data)

    m = (data_length * (x * y).sum() - x.sum() * y.sum()) / (data_length * (x * x).sum() - x.sum() * x.sum()) # using the algebraic least squares method, find slope m 
    b = (y.sum() - m * x.sum()) / data_length # finding y-intercept, b

    return round(m, 4), round(b, 4) # rounding both slope and y-intercept by 4 places after computation

# function name: mat_least_sq
# inputs: file_name- name of the csv file 
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):
    data = pd.read_csv(file_name) # read data from given csv file
    
    x = np.array(data.x)
    y = np.array(data.y)
    data_length = len(x)

    matrix_X = np.matrix([x, np.ones(data_length)]).T # In matrix_X, 1st column has all of the x's from data & 2nd column is full on 1's for the y-intercept
    matrix_Y = np.matrix(y).T
    matrix = np.linalg.inv(matrix_X.T.dot(matrix_X)).dot(matrix_X.T).dot(matrix_Y) # using the linear algebra method, matrix_X tranpose is dot product with matrix_X, then inverted, then dot product with y matrix
    
    m = matrix.item(0) # get slope from matrix
    b = matrix.item(1) # get y-intercept from matrix

    return round(m, 4), round(b, 4) # rounding both slope and y-intercept by 4 places after computation

# function name: predict
# inputs: file_name- name of the csv file 
		# x- input value that you will interpolate or extrapolate using mat_least_sq
# output: the predicted value based on the linear regression equation found using mat_least_sq
		# The output should be rounded to 4 decimal places
# assumptions: The csv file will always have headers in the order of: x, y
def predict(file_name, x):
    m, b = mat_least_sq(file_name) # acquire slope and y-intercept from mat_least_sq()

    y = (m * x) + b  # use slope intercept form to find output y

    return round(y, 4) # round output y by 4 places after computation

# function name: plot_reg
# inputs: file_name- name of the csv file
		# using_matrix: True if you are plotting the linear equation from mat_least_sq
		# 				False if you are plotting the linear equation from least_sq
# output: nothing is returned
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
	# your graph should have the following: labeled x and y axes, title, legend
	# if using_matrix is False (using least_sq), use X's and red in your graph
	# if using_matrix is True (using mat_least_sq), you can use any color except for the default blue and red
			# you can use any marker except for the default dot and X
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):
    data = pd.read_csv(file_name) # read data from given csv file

    plt.xlabel('x')
    plt.ylabel('y')

    if using_matrix: # if using_matrix == True
        m, b = mat_least_sq(file_name) # acquire slope and y-intercept from mat_least_sq()
        plt.title('Using Matrix Least Squares')

    else: # if using_matrix == False
        m, b = least_sq(file_name) # acquire slope and y-intercept from least_sq()
        plt.title('Using Algebra Least Squares')

    x = np.linspace(min(data.x), max(data.x))
    y = (m * x) + b 

    if using_matrix: # if using_matrix == True
        plt.plot(x, y, 'purple', label='y={}x+{}'.format(m, b)) # plot the line of best fit in purple
        plt.scatter(data.x, data.y, color = 'g', marker = '^', label='data points') # plot datapoints in green and ^ shaped
    else : # if using_matrix == False
        plt.plot(x, y, 'r', label='y={}x+{}'.format(m, b)) # plot the line of best fit in red
        plt.scatter(data.x, data.y, color = 'r', marker = 'x', label='data points') # plot datapoints in red and x shaped

    plt.legend()
    plt.show()
