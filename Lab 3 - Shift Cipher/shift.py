def shift_cipher_encode(string, n):
	encryptedText = ""
	for i in range(len(string)):
		if string[i].isupper():
			encryptedText += chr((ord(string[i]) + n - 65) % 26 + 65) # if chr is upper-case, subtract by 65 to get proper number in the alphabet and then mod by 26, add 65 back to get ASCII value 
		elif string[i].islower():										
			encryptedText += chr((ord(string[i]) + n - 97) % 26 + 97) # if chr is lower-case, subtract by 97 to get proper number in the alphabet and then mod by 26, add 97 back to get ASCII value 
		else:
			encryptedText += string[i]								  # if there are non-alhpabet characters, leave them alone
	return encryptedText


def shift_cipher_decode(string, n):									  # same as encode, but subtract shift value from ord(string[i]) instead
	decryptedText = ""
	for i in range(len(string)):
		if string[i].isupper():
			decryptedText += chr((ord(string[i]) - n - 65) % 26 + 65) # if chr is upper-case, subtract by 65 to get proper number in the alphabet and then mod by 26, add 65 back to get ASCII value 
		elif string[i].islower():
			decryptedText += chr((ord(string[i]) - n - 97) % 26 + 97) # if chr is lower-case, subtract by 97 to get proper number in the alphabet and then mod by 26, add 97 back to get ASCII value 
		else:
			decryptedText += string[i] 								  # if there are non-alhpabet characters, leave them alone
	return decryptedText






