
fin = open("lyrics.txt", "r")

lyrics = fin.readlines()
#print(lyrics)

lines = []
'''
for line in range(len(lyrics)):
	if "dynamite" in lyrics[line]:
		lines.append(line+1)
'''

i = 1
for line in lyrics:
	if "dynamite" in line:
		lines.append(i)
	i += 1

print("Num of lines with 'dynamite':", lines)

fin.close()
