
import re

fin = open("lyrics.txt", "r")

lyrics = fin.readlines()
#print(lyrics)

wordInLine = {}

i = 0
for index, line in enumerate(lyrics):
	#line = re.sub(r'[^\w\s]', '', line)
	#line = re.sub("'|\"|[.|,|?|(|)]", '', line)
	for word in line.split():
		word = word.strip("(),!?'\"").lower()
		if word not in wordInLine:
			wordInLine[word] = [index]
		else:
			wordInLine[word].append(index)

for k, v in wordInLine.items():
	print(k, ":", v,"\n")

fin.close()
