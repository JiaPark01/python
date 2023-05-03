import random

ans = []
num = random.randint(1, 9)

for i in range(3):
	while num in ans:
		num = random.randint(1, 9)
	ans.append(num)

attempt = 10
win = False

print(f"Answer : {ans[0]} {ans[1]} {ans[2]}\n")

while attempt != 0:
	range_pass = True
	
	try:
		user = list(map(int, input("Enter 3 numbers: ").split()))
	except ValueError:
		print("** Invalid input! Enter numbers only **\n")
		continue
	
	if len(user) != 3:
		print("** Please enter three numbers! **\n")
		continue

	for i in range(3):
		if 1 > user[i] or user[i] > 9:
			print("** Numbers must be between 1~9 **\n")
			range_pass = False
			break
	
	if range_pass == False:
		continue
			
	attempt -= 1
	
	strike = 0
	ball = 0

	for i in range(3):
		if user[i] == ans[i]:
			strike += 1
		elif user[i] in ans:
			ball += 1
	
	print(f"strike : {strike}\tball: {ball}\n\nRemaining attempt : {attempt}\n")
	
	if strike == 3:
		win = True
		break

if win == True:
	if attempt == 9:
		print("Congratulations! You have guessed the number in the first attempt!")
	else:
		print(f"Congratulations! You have guessed the number in {10 - attempt} attempts!")
else:
	print(f"Oops! Answer : {ans[0]} {ans[1]} {ans[2]}")
