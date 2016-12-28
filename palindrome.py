# Objective: Check if an input is a palindrome

print "Enter a word:"
a = raw_input()

b = a[::-1]
if (a == b):
	print "This is a palindrome!"
else:
	print "This is not a palindrome!"