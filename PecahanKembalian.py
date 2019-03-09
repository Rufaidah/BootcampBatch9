price = int(input("Masukkan total belanja : Rp"))
pay = int(input("Masukkan total uang yang dimasukkan : Rp"))
change = [50000, 20000, 10000, 5000, 2000, 1000, 500]

def pecahan():
    total_change = pay - price
    print("Total kembalian adalah : Rp" + str(total_change))

    for x in range(0, 7):
        i = 0
        while total_change >= change[x]:
            total_change = total_change - change[x]
            i = i + 1
            if i > 0:
                print("Uang Rp" + str(change[x]) + " sebanyak " + str(i) + " lembar")
            else:
                break

pecahan()
