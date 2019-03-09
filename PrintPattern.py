side = int(input("Masukkan panjang sisi persegi : "))

a = 1
b = 1
for a in range(side + 1):
    if a % 2 != 0:
        val = (side - a) // 2
        print ("=" * val + "*" * (a) + "=" * val, end = "\n")
for b in range(side-1,0,-1):
    if b % 2 != 0:
        val2 = (side - b) // 2
        print ("=" * val2 + "*" * (b) + "=" * val2 ,end = "\n")