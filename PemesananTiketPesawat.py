print("==================================================")
print("%-5s"%"|","SELAMAT DATANG DI PENERBANGAN LION AIR","%5s"%"|")


jdwl = [{"nomor" : "JT 565","tujuan" : "Jakarta","jam" : "09:25 - 11:25", "harga" : 1300000},
        {"nomor" : "JT 678","tujuan" : "Bandung","jam" : "09:30 - 12:30", "harga" : 1790000},
        {"nomor" : "JT 917","tujuan" : "Lombok ","jam" : "09:45 - 11:45", "harga" : 1790000},
        {"nomor" : "JT 910","tujuan" : "Jogja  ","jam" : "09:45 - 12:45", "harga" : 1890000},
        {"nomor" : "JT 110","tujuan" : "Bali   ","jam" : "09:50 - 14:50", "harga" : 2000000}
        ]

def menu():
    print("%-9s"%"|","Adakah yang Bisa Kami Bantu ?","%10s"%"|")
    print("==================================================")
    print("Daftar Menu :")
    print("1. Jadwal Penerbangan & Daftar Harga Tiket")
    print("2. Pesan Tiket")
    print("3. Lihat Daftar Pesanan Tiket & Total Harga")
    print("4. Hapus Pesanan Tiket")
    print("5. Selesai")

def pesan():
    nama = input("Masukkan Nama : ")
    if not nama:
        print("Nama tidak boleh kosong")
        return
    nomor_pesan = input("Masukkan Nomor Penerbangan (WAJIB CAPSLOCK) : ")
    nomor_ditemukan = False
    for i in jdwl:
        if i["nomor"] == nomor_pesan:
            pesanticket.append({"nama": nama, "nomor": nomor_pesan, "tujuan": i["tujuan"], "harga": i["harga"]})
            print("Tiket telah dipesan untuk",nama,"dengan nomor penerbangan",nomor_pesan)
            nomor_ditemukan = True
            break

    if not nomor_ditemukan:
        print("Nomor penerbangan tidak ditemukan.")

def jumlah(pesanticket):
    if not pesanticket:
            print("Tidak ada tiket yang terdaftar")
            return
    else:
        for i in range(len(pesanticket)):
            print("%-3s"%"|","%-25s"%pesanticket[i]["nama"],
                  "%-3s"%"|","%-3s"%" ",pesanticket[i]["nomor"],"%-3s"%" ",
                  "%3s"%"|","%-3s"%" ",pesanticket[i]["tujuan"],"%-3s"%" ",
                  "%3s"%"|","%-3s"%" ","Rp. "+str(pesanticket[i]["harga"]),"%-3s"%" ","|")

def total(pesanticket):
    totalticket = 0
    for i in pesanticket:
        totalticket += i["harga"] 
    print("Total harga: Rp.", totalticket)

def hapus(pesanticket):
    nomor_hapus = int(input("Masukkan Urutan Nomor yang Ingin Dihapus (Urutan ke 1, 2, dan seterusnya): "))
    if nomor_hapus < 1 or nomor_hapus > len(pesanticket):
        print("Nomor tiket tidak valid!")
    else:
        ticket_dihapus = pesanticket.pop(nomor_hapus - 1)
        print("Nomor pesanan",ticket_dihapus["nomor"],"atas nama",ticket_dihapus["nama"],"berhasil dihapus")


    

    
n = 1
pesanticket = []


while(n!=5):
    print("==================================================")
    menu()
    print("==================================================")
    n = int(input("Masukkan Nomor Menu yang Kamu Mau Pilih : "))
    print()

    if(n == 1):
        print("%-3s"%"|","Nomor Penerbangan" ,"%2s"%" ",
              "|","%-3s"%" ","Tujuan","%4s"%" ",
              "%-10s"%"|","Jam",
              "%11s"%"|","%-5s"%" ","Harga","%-7s"%" ","|")
        for i in range(len(jdwl)):
            print("===========================================================================================")
            print("%-9s"%"|",jdwl[i]["nomor"],
                  "%9s"%"|","%-3s"%" ",jdwl[i]["tujuan"],"%-3s"%" ",
                  "%-6s"%"|",jdwl[i]["jam"],
                  "%5s"%"|","%-3s"%" ","Rp. "+str(jdwl[i]["harga"]),"%-3s"%" ","|")
        print("===========================================================================================")

    elif(n == 2):
        pesan()
        
    elif(n == 3):
        jumlah(pesanticket)
        total(pesanticket)

    elif(n == 4):
        hapus(pesanticket)
                        

    elif(n == 5):
        print("Terima kasih telah memakai jasa kami!")

    else:
        print("Maaf, nomor input yang kamu masukkan tidak tersedia.")
      
    print()


    



    
    
