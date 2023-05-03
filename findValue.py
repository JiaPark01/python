
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

value = int(input("value : "))

for i in range(10):
	if list[i] == value:
		print(f"{value} is in index {i}")
		break

if value not in list:
	print("value not found")
else:
	print("value found")
