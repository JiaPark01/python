
def factorial(num):
	result = 1
	for i in range(1, num+1):
		result *= i
	return result

result = [factorial(i) for i in range(1, 101)]

result = list(map(factorial, [i for i in range(1, 101)]))

[print(i,":",factorial(i),"\n") for i in range(1, 101)]
