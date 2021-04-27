from load import Gadget

def printGroup(i,arr):
    if arr[i][0][0] == 'G':
        print("Type Item        :  Gadget")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print("Tahun Ditemukan  : ", arr[i][5])
        print()
    elif arr[i][0][0] == 'C':
        print("Type Item        :  Consumable")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==5:
        print("ID Peminjaman       : ", arr[i][0])
        print("Nama Pengambil      : ", arr[i][1])
        print("Nama Gadget         : ", arr[i][2])
        print("Tanggal Peminjaman  : ", arr[i][3])
        print("Jumlah              : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==4:
        print("ID Pengembalian       : ", arr[i][0])
        print("Nama Pengambil        : ", arr[i][1])
        print("Nama Gadget           : ", arr[i][2])
        print("Tanggal Pengembalian  : ", arr[i][3])
        print()    
    elif arr[0][1] =='id_pengambil':
        print("ID Pengambilan       : ", arr[i][0])
        print("Nama Pengambil       : ", arr[i][1])
        print("Nama consumable      : ", arr[i][2])
        print("Tanggal Pengambilan  : ", arr[i][3])
        print("Jumlah               : ", arr[i][4])


def check_input(kategori):
    if not (kategori != "=" or kategori != ">" or kategori != "<" or kategori != "<=" or kategori != ">="):
        return False
    else:
        True

def input_valid(kategori):
    if check_input(kategori):
        while(check_input):
            print("Masukkan salah")
            kategori = input("Masukkan ulang tanda : ")
    return kategori

def searchyear (Gadget):
    n = len(Gadget)
    tahun_input = int(input("Masukkan Tahun : "))
    kategori = str(input("Masukkan Kategori : "))
    kategori = input_valid(kategori)
    print()
    print ("Hasil pencarian : ")
    print()
    found = 0
    for i in range (1,n):
        if kategori == ">" and int(Gadget[i][5]) > tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == "<" and int(Gadget[i][5]) < tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == "=" and int(Gadget[i][5]) == tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == ">=" and int(Gadget[i][5]) >= tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == "<=" and int(Gadget[i][5]) <= tahun_input:
            printGroup(i,Gadget)
            found += 1
    if found == 0:
        print ("Tidak ada gadget yang ditemukan")
        print()