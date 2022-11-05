import numpy as np
import pandas as pd
import math


# function name: find_class_averages
# inputs: file_name- name of csv file
		# class_names- list of strings representing class names
# output: a pandas dataframe with no headers where each row represnts the average
		# values of the class. The last column should indicate the class
		# Round each value to three decimal places
# assumptions: The csv file will not have headers!
			# Each row of the csv file is a data vector for each class
			# The last column will represent the classes. The remaining columns hold the data
			# you CANNOT assume that we will be using the same file for other test cases. We can use a file with a different number of columns and/or rows
def find_class_averages(file_name, class_names):
	pass


# function name: most_similar_cosine
# inputs: average_df- pandas dataframe containing class averages
		# test_vec- vector that you are trying to classify
# output: a string that states what class the function is
# task: return the best class (AS A STRING) by using the cosine similarity metric
# assumptions: 
def most_similar_cosine(average_df, test_vec):
	pass



# function name: most_similar_euclid
# inputs: average_df- pandas dataframe containing class averages
		# test_vec- vector that you are trying to classify
# output: a string that states what class the function is
# task: return the best class (AS A STRING) by using the euclidean distance metric
# assumptions: 
def most_similar_euclid(average_df, test_vec):
	pass



# function name: most_similar_manhattan
# inputs: average_df- pandas dataframe containing class averages
		# test_vec- vector that you are trying to classify
# output: a string that states what class the function is
# task: return the best class (AS A STRING) by using the manhattan distance metric
# assumptions:
def most_similar_manhattan(average_df, test_vec):
	pass






############### CHECKER FUNCTION ###############
def checker(expected, actual):
	if type(expected) != type(actual):
		print("Conflicting data types!")
		return
	if type(expected) == str:
		if expected == actual:
			print("Correct!")
		else:
			print("Incorrect! Expected", expected, "but got", actual)
	else:
		e = expected.sort_values(by=expected.columns.tolist()).reset_index(drop=True)
		a = actual.sort_values(by=actual.columns.tolist()).reset_index(drop=True)
		for row, index in e.iterrows():
			for col in e:
				if e.loc[row,col] != a.loc[row,col]:
					print("Incorrect! Expected: ")
					print(expected.values)
					print("but got:")
					print(actual.values)
					print()
					return
		print("Correct!")

			


############### TEST CASES ###############
test_file = 'iris.csv'
class_names = ['Iris-versicolor', 'Iris-setosa', 'Iris-virginica']
test_vec1 = [5.1,3.4,1.5,0.2]
test_vec2 = [6.0,3.4,4.5,1.6]
test_vec3 = [6.5,3.0,5.5,1.8] 


expected = [[6.588,2.974,5.552,2.026,'Iris-virginica'],
			[5.006,3.418,1.464,0.244,'Iris-setosa'],
			[5.936,2.770,4.260,1.326,'Iris-versicolor']]
expected_df=pd.DataFrame(expected)
ave_df = find_class_averages(test_file, class_names)
print('find_class_averages test:', end = " ")
checker(expected_df, ave_df)


print('most_similar_cosine test 1:', end = " ")
checker('Iris-setosa',most_similar_cosine(ave_df, test_vec1))
print('most_similar_euclid test 1:', end = " ")
checker('Iris-setosa',most_similar_euclid(ave_df, test_vec1))
print('most_similar_manhattan test 1:', end = " ")
checker('Iris-setosa',most_similar_manhattan(ave_df, test_vec1))


print('most_similar_cosine test 2:', end = " ")
checker('Iris-versicolor', most_similar_cosine(ave_df, test_vec2))
print('most_similar_euclid test 2:', end = " ")
checker('Iris-versicolor', most_similar_euclid(ave_df, test_vec2))
print('most_similar_manhattan test 2:', end = " ")
checker('Iris-versicolor', most_similar_manhattan(ave_df, test_vec2))


print('most_similar_cosine test 3:', end = " ")
checker('Iris-virginica', most_similar_cosine(ave_df, test_vec3))
print('most_similar_euclid test 3:', end = " ")
checker('Iris-virginica', most_similar_euclid(ave_df, test_vec3))
print('most_similar_manhattan test 3:', end = " ")
checker('Iris-virginica', most_similar_manhattan(ave_df, test_vec3))

