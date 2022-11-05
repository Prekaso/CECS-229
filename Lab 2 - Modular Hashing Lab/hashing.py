class hash_table:

	# constructor
	# inputs: size (defaults to 8 if no arguments are provided)
	def __init__(self, size = 8):
		# self.table: empty hash table of indicated size
		self.table = (None,) * size
		# self.size: number of positions in table
		self.size = size


	# Already completed function!
	# INSERTS value INTO HASHTABLE AT index
	# example: insert(5, 10) will place 5 into index#10
	def insert(self, value, index):
		temp = list(self.table)
		temp[index] = value
		self.table = tuple(temp)


	def linear_probe(self, value, start_index):
		key = start_index % len(self.table)				# takes given value and mod by the lenght of the table to get hash key.
		for i in range(len(self.table)):				# if there is collision, re-hash key by moving value in the next available slot. keeps checking until available slot.
			if self.table[key] != None:
				key = (key + 1) % len(self.table)		# add 1 and then mod by the length of the table will give next available slot for value.
		return key, value


	def hash(self, value):
		start_index = value % self.size								# instantiate start_index to use in linear_probe function.
		index, start_index = self.linear_probe(value,start_index)	# use linear_probe function to find the correct index or position of given value.
		self.insert(value,index)									# insert value into table.


	# Already completed function!
	def get_table(self):
		return self.table


	# Already completed function!
	def __str__(self):
		return str(self.table)

"""**********************************************************************"""
# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
"""**********************************************************************"""

def checker(expected, actual):
	if expected == actual:
		print("CORRECT!")
	else:
		print("expected " + str(expected) + ", but got " + str(actual))

"""**********************************************************************"""

test1 = hash_table(5)
test1.hash(9)
test1.hash(25)
test1.hash(10)
test1.hash(14)
expected1 = (25, 10, 14, None, 9)

checker(expected1, test1.get_table())

"""**********************************************************************"""


test2 = hash_table(8)
test2.hash(5)
test2.hash(30)
test2.hash(52)
test2.hash(95)
test2.hash(45)
expected2 = (45, None, None, None, 52, 5, 30, 95)

print(test2.linear_probe(16, 0))
print(test2.linear_probe(107, 3))
print(test2.linear_probe(81, 1))
print(test2.linear_probe(315, 3))
print(test2.linear_probe(198, 6))

checker(expected2, test2.get_table())
