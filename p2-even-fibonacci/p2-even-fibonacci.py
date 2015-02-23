last_term = 1
term = 2
sum = 0
while term <= 4000000:
	if term % 2 == 0:
		sum += term
	tmp = term
	term = last_term + term
	last_term = tmp
print(sum)