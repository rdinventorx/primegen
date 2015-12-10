from __future__ import division
inputnum = int(raw_input('How many primes would you like? '))

filename = raw_input('What should be the name of this file? ')
with open(filename, 'w') as text_file:
	
dividend = 2
primessolved = 0
while primessolved != inputnum:
	
	divisors = range (2, dividend)
	isprime = 1
	for divisor in divisors:
		quotient = float(dividend / divisor)
		floor = dividend // divisor
		checksum = float(quotient - floor)
		if checksum == 0:
			isprime = 0
	if isprime == 1:
		with open(filename, 'a') as text_file
			text_file.write(dividend)
		primessolved = primessolved + 1
	dividend = dividend + 1

		
	
	
