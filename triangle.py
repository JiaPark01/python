
val = input("base height : ")
val = val.split()

base = int(val[0])
height = int(val[1])

area = base * height / 2

print(f"area : {area:.1f}")
