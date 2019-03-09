jam = int(input("Masukkan jumlah jam : "))

def bayarParkir():
    counter = 0
    tambahan = 1000
    maks = 10000

    if jam <= 2:
        bayar = 2000
    else:
        bayar = 2000
        while counter < jam - 2:
            counter = counter + 1
            bayar = bayar + tambahan
            if bayar >= maks:
                break
    print("Bayar Rp" + str(bayar))

bayarParkir()