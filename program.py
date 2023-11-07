#!/usr/bin/env python3

with open("message.txt", "r") as msg:
	# Read the message and append each no into the list
	x = msg.read()
 	
 	# declare lists, variables

	lst = []
	lst2 = []
	mod = 0
	s = ''
	prefix = 'picoCTF{'
	suffix = '}'
	str = ''

	for i in x.split(' '):
		lst.append(i)
	lst.pop()

	# Modulus by 37
	for a in lst:
		con_int = int(a)
		mod = con_int % 37
		lst2.append(mod)

	#list containing alphabet uppercase letters 
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',' V', 'W', 'X', 'Y', 'Z']
	#list containing 0-9 decimal digits
	decimal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	# make the string
	for b in lst2:
		if b >= 0 and b <=25:
			s += alphabet[b]
		elif b >=26 and b <= 35:
			s += decimal[b-26]
		elif b == 36:
			s += '_'

	# wrap it as a flag
	str = prefix + s + suffix
	print(str)

