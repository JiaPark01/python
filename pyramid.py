
for i in range(1, 6):
	line = ''
	for j in range(5 - i):
		line += ' '
	for j in range(i * 2 - 1):
		line += '*'
	print(line)
