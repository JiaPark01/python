
val = input("Korean English Maths : ")
val = val.split()

kor, eng, maths = map(int, val)	# unpacking

tot = kor + eng + maths
avg = tot / 3

print(f"Total : {tot:3d}, average : {avg:.2f}")
