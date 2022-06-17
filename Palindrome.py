#same as reversing a string , by comparing both string we get palindrome
n = input('enter a string')
reversedString = n[::-1]
if n == reversedString:
	print('it Is a Palindrome')
else:
	print('It is not Palindrome')