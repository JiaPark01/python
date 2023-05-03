import random

def deleteFail(scores):
	for data in scores:
		if data < 60:
			scores.remove(data)

def isPass(score):
	return score >= 60

scores = [random.randint(40, 100) for i in range (10)]

print("scores:", scores)

result = list(filter(isPass, scores))
deleteFail(scores)

print("scores:", result)
print("scores:", scores)
