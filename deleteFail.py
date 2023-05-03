import random

def deleteFail(scores):
	for data in scores:
		if data < 60:
			scores.remove(data)

scores = [random.randint(40, 100) for i in range (10)]

print("scores:", scores)

deleteFail(scores)	# doesn't work well

print("scores:", scores)
