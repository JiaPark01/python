# like lottery2.c
import random

lottery = [i for i in range(1, 46)]
	
random.shuffle(lottery)

lottery = lottery[0:7]

'''
lottery = [0 for i in range(7)]

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
'''
print("Lottery:", lottery)

