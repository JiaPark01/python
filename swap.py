
def swap():
	global a, b
	temp = a
	a = b
	b = temp

a = 100
b = 200

print("a:", a, "b:", b)

swap()

print("a:", a, "b:", b)
