# tebak angka manggunakan
# 1. while True
# 2. Conditional
# 3. Break & Contiune

import os,time,random

while True:
    print("tebak angka!")
    print("-- Rule --")
    print("Kurang! ketika angka terlalu sedikit dari target")
    print("kebanyakan oon! ketika angka terlalu banyak dari target")
    print("-- Rule --")
    print("1. main")
    print("2. kluar aja lah gw males")
    cois = int(input("="))
    if cois == 1:
        print("lets play")
        tebak = random.randint(1,10)
        while True:
            masuk = int(input("Tebak angkany! = "))
            if masuk == tebak:
                print("yee ketebak")
                print("angkanya adalah =", tebak)
                break
            #jika masuk kurang dari tebak, outpunya "tambah lagi!"
            elif masuk < tebak:
                print("Tambahin lagi!")
            #jika masuk lebih dari tebak, outputnya "kurangin lagi!"
            elif masuk > tebak:
                print("kurangin lagi!")

    elif cois == 2:
        print(" kluar lu noob")
        break
    else:
        print("salah input!")
# tebak angka manggunakan
# 1. while True
# 2. Conditional
# 3. Break & Contiune

import os,time,random

while True:
    print("tebak angka!")
    print("-- Rule --")
    print("Kurang! ketika angka terlalu sedikit dari target")
    print("kebanyakan oon! ketika angka terlalu banyak dari target")
    print("-- Rule --")
    print("1. main")
    print("2. kluar aja lah gw males")
    cois = int(input("="))
    if cois == 1:
        print("lets play")
        tebak = random.randint(1,10)
        while True:
            masuk = int(input("Tebak angkany! = "))
            if masuk == tebak:
                print("yee ketebak")
                print("angkanya adalah =", tebak)
                break
            #jika masuk kurang dari tebak, outpunya "tambah lagi!"
            elif masuk < tebak:
                print("Tambahin lagi!")
            #jika masuk lebih dari tebak, outputnya "kurangin lagi!"
            elif masuk > tebak:
                print("kurangin lagi!")

    elif cois == 2:
        print(" kluar lu noob")
        break
    else:
        print("salah input!")
        