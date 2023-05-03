# like lottery2.c
import random

lottery = [0, 0, 0, 0, 0, 0, 0]

i = 0

while i < 7:
	lottery[i] = random.randint(1, 45)
	
	j = 0
	while j < i:
		if lottery[i] == lottery[j]:
			break
		j += 1
	
	if j == i:
		i += 1
	
for k in lottery:
	print(k)

