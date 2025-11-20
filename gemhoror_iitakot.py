import os,time

time.sleep(3)
print("Ih takutnye - Marvel.Nat")
print("1. forest")
print("2. abandon home") 
print("3. hill")

pilihan = int(input("Mau kemana? "))

os.system("cls")
if pilihan == 1:
    time.sleep(2)
    print("kamu pergi ke hutan, karena kamu ceroboh jadi kamu tersesat dan nyasar")
    print("-------------------------------------")
    print("kamu ketemu 2 jalan")
    print("1. kanan")
    print("2. kiri")
    jalan = int(input("Pilih mana ? "))
    os.system("cls")
    if jalan == 1:
        time.sleep(2)
        print("kamu menemukan tempat istirahat beruang putih dan kamu menjadi santapan lezat mereka (Bad ending)")
    elif jalan == 2:
        time.sleep(2)
        print("YEYY kamu menemukan warga warga baik yang mau menolong kamu (Happy ending)")
    else:
        time.sleep(2)
        print("nah kan ketemu macan, makanya pilih yang bener")

elif pilihan == 2:
    time.sleep(2)
    print("Kamu coba eksplor rumah terbengkalai")
    print("-------------------------------------")
    print("kamu mau eksplor lantai bawah apa atas?")
    print("1. Atas")
    print("2. Bawah")
    lantai = int(input("Pilih mana ? "))
    os.system("cls")
    if lantai == 1:
        time.sleep(2)
        print("kamu ketemu psikopat, lalu ditawan dan dibebasin setelah 3 hari (Bad ending)")
    elif lantai ==2:
        time.sleep(2)
        print("kamu terhindar dari psikopat dilantai 2 dan eksplor tempat itu dengan aman dan lancar (Happy ending)")
    else:
        time.sleep(2)
        print("nah kan kena jebakan batman, makanya pilih yang bener")

elif pilihan == 3:
    time.sleep(2)
    print("Kamu mau foto-foto ditebing malah kepleset dan bergelantungan")
    print("-------------------------------------")
    print("kamu ada 2 alat ")
    print("1. gundu")
    print("2. grappling")
    alat = int(input("Pilih mana ? "))
    os.system("cls")
    if alat == 1:
        time.sleep(2)
        print("ngapain sih pilih gundu? jatoh kann  (Bad ending)")
    elif alat ==2:
        time.sleep(2)
        print("kamu bisa naik ke atas karna grappling nya nyangkut dipohon, (Happy ending)")
    else:
        time.sleep(2)
        print("kamu ga kuat dan kamu terjatuh ke bawah dan di panggil yang maha kuasa")
    

else :
    time.sleep(2)
    print("di kasih pilihan malah pilih pilih hadehh")