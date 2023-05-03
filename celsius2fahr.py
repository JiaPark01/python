#celsius --> fahr
# cel = 5 / 9 * (fahr - 32)

celsius = int(input("celsius : "))
fahr = celsius / 5 * 9 + 32

print(f"celsius : {celsius:3d}, fahr : {fahr:.2f}")
