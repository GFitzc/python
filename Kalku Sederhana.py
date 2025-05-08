angka=1

while(angka!=0):
    print("============================")
    print("Kalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("0. Keluar")
    print("============================")


    angka=int(input("Masukkan Pilihan Operasi = "))
    print()
    if(angka==1):
        angka1=int(input("Masukkan Angka 1 = "))
        angka2=int(input("Masukkan Angka 2 = "))
        hasil=angka1+angka2
        print("hasilnya adalah = ",hasil)

    elif(angka==2):
        angka1=int(input("Masukkan Angka 1 = "))
        angka2=int(input("Masukkan Angka 2 = "))
        hasil=angka1-angka2
        print("hasilnya adalah = ",hasil)

    elif(angka==3):
        angka1=int(input("Masukkan Angka 1 = "))
        angka2=int(input("Masukkan Angka 2 = "))
        hasil=angka1*angka2
        print("hasilnya adalah = ",hasil)

    elif(angka==4):
        angka1=int(input("Masukkan Angka 1 = "))
        angka2=int(input("Masukkan Angka 2 = "))
        hasil=angka1/angka2
        print("hasilnya adalah = ",hasil)

    elif(angka > 4 or angka < 0):
        print("Error")
    print()

  
