GRADES = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']

score = int(input("score :"))

grade = GRADES[score//10]

print(f"score : {score} --- grade : {grade}")
