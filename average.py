
val = input("Korean English Maths : ")
val = val.split()

kor, eng, maths = val	# unpacking

tot = int(kor) + int(eng) + int(maths)
avg = tot / 3

print(f"Total : {tot:3d}, average : {avg:.2f}")
