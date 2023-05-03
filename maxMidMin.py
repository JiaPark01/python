
nums = input("Enter 3 numbers :")
nums = nums.split()

num1 = int(nums[0])
num2 = int(nums[1])
num3 = int(nums[2])

if num1 > num2:
	maxN = num1
	minN = num2
else:
	maxN = num2
	minN = num1

if num3 > maxN:
	midN = maxN
	maxN = num3
else:
	midN = minN
	minN = num3

print(f"MAX: {maxN}, MID: {midN}, MIN: {minN}")
