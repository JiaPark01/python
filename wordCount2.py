
fin = open("lyrics.txt", "r")

lyrics = fin.read().split()
#print(lyrics)

wordCount = {}

for word in lyrics:
	if word not in wordCount:
		wordCount[word] = 1
	else:
		wordCount[word] += 1

for k, v in wordCount.items():
	print(k, ":", v)

fin.close()
