
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

result = [factorial(i) for i in range(1, 101)]
result = list(map(factorial, [i for i in range(1, 101)]))

print("result:", result)
