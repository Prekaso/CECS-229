def to_decimal(num: str, base: int) -> int :

	complete_decimal = 0
	for char in num :
		if char >= "0" and char <= "9" : 			
			decimal = ord(char) - 48				# if 0 >= char <= 9, I need to subtract ord(char) by 48 to adjust for offset in the ascii table, I could've used ord("0"). 
		else:										# ord() function converts the char value into the decimal value. [ex. ord("0") = 48 (decimal)]
			decimal = ord(char) - 55				# if char > 9, I need to subtract ord(char) by 55 to adjust for offset in the ascii table, I could've used (ord("A") + 10).
		complete_decimal = base * complete_decimal + decimal	

	return complete_decimal

def to_base(dec_num: int, base: int) -> str :

	complete_base = ""
	while dec_num > 0 :
		remainder = dec_num % base
		if remainder <= 9 :
			remainder = chr(48 + remainder)	
		else:											# chr() converts decimal to char value according to the ascii table.
			remainder = chr(55 + remainder)
		complete_base = remainder + complete_base		# complete_base has to be added after remainder or else the base value will be reversed.
		dec_num //= base								# I repeatedly use modulus and floor until dec_num is <= 0. 
														# Steps: Find remainder from dec_num and base using modulus -> add the 1 or 0 remainder to complete_base -> floor dec_num to get next dec_num -> repeat until dec_num <= 0
	return complete_base		