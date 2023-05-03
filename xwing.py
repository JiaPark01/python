
for i in range(5):
	line = ''
	for j in range(5):
		if i == j or i + j == 4:
			line += '*'
		else:
			line += ' '
	print(line)
