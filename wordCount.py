
fin = open("lyrics.txt", "r")

lyrics = fin.readlines()
#print(lyrics)

wordCount = {}

for line in lyrics:
	for word in line.split():
		if word not in wordCount:
			wordCount[word] = 1
		else:
			wordCount[word] += 1

for k, v in wordCount.items():
	print(k, ":", v)

fin.close()
