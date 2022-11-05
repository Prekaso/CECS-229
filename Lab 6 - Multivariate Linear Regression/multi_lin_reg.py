import numpy as np
import pandas as pd

# function name: multivar_linreg
# inputs: file_name- name of the train csv file 
# output: 1xn numpy array [m1, m2, m3, ..., b] (row vector not column vector)
		# return a numpy array! NOT a list
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
		# Round each value to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
		# Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
def multivar_linreg(file_name):
	df = pd.read_csv(file_name) # read data from given csv file

	X = np.column_stack([np.array(df.drop("y", axis=1)), np.ones((len(df), 1))]) # form 2D array and drop y column, fill with 1's
	y = np.array(df["y"]).reshape(-1,1) # change dimension of y array
	m = np.round(np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y),4)  # (X^T * X)^-1 * X^T * y 

	return np.round(m.flatten(), 4) # format to 1xn numpy array, round to 4 decimal places

# function name: predict
# inputs: inputs- 1xn numpy array of weights [m1, m2, m3, ..., b] (row vector not column vector)
		# file_name- name of test csv file
# output: 
		# return a numpy array1xm numpy array [y1, y2, y3 ...] (row vector not column vector)! NOT a list
		# the order of the list corresponds to the order of the rows of data from top to bottom
		# Round each value to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
		# Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
def predict(inputs, file_name):
	df = pd.read_csv(file_name) # read data from given csv file

	X = np.column_stack([np.array(df.drop("y",axis=1)),np.ones((len(df),1))]) # form 2D array and drop y column, fill with 1's
	m = inputs
	y = X.dot(m) 

	return np.round(y.flatten(),4) # format to 1xn numpy array, round to 4 decimal places

# function name: MAE
# inputs: inputs- 1xn numpy array of weights [m1, m2, m3, ..., b] (row vector not column vector)
		# file_name- name of test csv file
# output: the mean absolute error of the predictions formed from inputs
		# round mae to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
	# Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
	# you may use any of the previous functions 
def MAE(inputs, file_name):

	y_actual = np.array(pd.read_csv(file_name)["y"]) # read y data from given csv file & create array
	y_predicted = predict(inputs,file_name)
	n = len(y_predicted) # n of summation = length of predicted array

	return round((1/n)*np.sum(np.abs(y_actual-y_predicted)),4) # MAE formula 

# function name: MRE
# inputs: inputs- 1xn numpy array of weights [m1, m2, m3, ..., b] (row vector not column vector)
		# file_name- name of test csv file
# output: the mean relative error of the predictions formed from inputs
		# round mre to four decimal places
# assumptions: The csv file will always have headers in the order of: x1, x2, x3, ... y
	# Though the example shows 6 columns, there may be more or less in other test cases (at least one independent variable)
	# you may use any of the previous functions
def MRE(inputs, file_name):

	y_actual = np.array(pd.read_csv(file_name)["y"]) # read y data from given csv file & create array
	y_predicted = predict(inputs,file_name)
	n = len(y_predicted) # n of summation = length of predicted array

	return round((1/n)*np.sum(np.abs(y_actual-y_predicted)/y_actual),4) # MRE formula
######## TEST CASES ########
# this test case is the same as the one in 
train_csv = "Real estate train.csv"
test_csv = "Real estate test.csv"

weights = multivar_linreg(train_csv)
expected_weights = np.array([4.9535, -0.2696, -0.0045, 1.1148, 230.7976, -13.5932, -14039.6784])
print("expected weights:", expected_weights)
print("your answer:", weights)
print("CORRECT\n" if np.allclose(weights, expected_weights) else "INCORRECT\n")

# NOTE: using expected_weights instead of weights for testing purposes
# you should replace this with predicted to check if your model works
predicted = predict(expected_weights, test_csv)
expected_predictions = np.array([41.0483,33.3038,39.6696,45.0673,46.8449,37.8108,49.7323,26.6559,32.0756,14.4788,50.0397,46.9619,44.7727,53.9234])
print("expected predictions:", expected_predictions)
print("your answer:", predicted)
print("CORRECT\n" if np.array_equal(predicted, expected_predictions) else "INCORRECT\n")

# NOTE: using expected_weights instead of weights for testing purposes
# you should replace this with predicted to check if your model works
mae = MAE(expected_weights, test_csv)
expected_mae = 5.4668
print("expected MAE:", expected_mae)
print("your answer:", mae)
print("CORRECT\n" if mae==expected_mae else "INCORRECT\n")

# NOTE: using expected_weights instead of weights for testing purposes
# you should replace this with predicted to check if your model works
mre = MRE(expected_weights, test_csv)
expected_mre = 0.1518
print("expected MRE:", expected_mre)
print("your answer:", mre)
print("CORRECT" if mre==expected_mre else "INCORRECT")