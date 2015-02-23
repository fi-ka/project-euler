primes = [3,5,7,13,17]

def findNextPrime(x):
	val = x + 1
	while not isPrime(val):
		val += 1
	return val

def isPrime(x):
	for i in range(2,x):
		if x % 2 == 0:
			return False
	return True

val = 600851475143
prime_factors = []
current_prod = 1
current_prime = 1
while current_prod != val:
	current_prime = findNextPrime(current_prime)
	tmp_val = val % current_prime
	if tmp_val == 0:
		prime_factors.append(current_prime)
		current_prod *=  current_prime
		print(current_prime)
		print(current_prod)
print(current_prime)