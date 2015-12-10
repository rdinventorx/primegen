from __future__ import division
inputnum = int(raw_input('How many primes would you like? '))

primes = list()

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
		print str(primessolved + 1) + ' = ' + str(dividend)
		primessolved = primessolved + 1
	dividend = dividend + 1
	
		
		
	
	
