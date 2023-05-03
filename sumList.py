
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tot = 0

for i in range(10):
	tot += list[i]
print(f"Total : {tot}")

tot = 0

for i in list:
	tot += i
print(f"Total : {tot}")

tot = sum(list)

avg = tot / len(list)
print(f"average : {avg}")
