
def isOdd(num):
	return num % 2 == 1

nums = [i for i in range(1, 11)]

nums = list(filter(isOdd, nums))

print("list:", nums)
