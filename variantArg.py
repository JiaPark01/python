
def my_sum(*args):
	tot = 0
	print("args:", args)	# tuple
	
	for val in args:
		tot += val
	
	return tot

def my_sum(*args):
	return sum(list(args))

result = my_sum(1, 2, 3, 4, 5)

print("result:", result)
